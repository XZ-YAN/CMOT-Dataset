# coding=UTF-8
# Code Author: Xuzhong Yan
import os, sys, time, glob, math, cv2, turtle, ast, random, imageio, base64
from tqdm import tqdm
from functools import reduce
from imgaug.augmentables.bbs import BoundingBox, BoundingBoxesOnImage
from matplotlib import pyplot, transforms, cm
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from matplotlib.patches import Circle
import mpl_toolkits.mplot3d.art3d as art3d
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.gridspec import GridSpec
from ast import literal_eval
from copy import deepcopy
import seaborn as sns
from shapely.geometry import box, Polygon
from imantics import Mask
import numpy as np
from io import StringIO
from mpl_toolkits.mplot3d import Axes3D
from PIL import Image, ImageDraw
from scipy.optimize import fsolve
from scipy.stats import multivariate_normal, gaussian_kde
from scipy import stats
from matplotlib.ticker import LinearLocator
from scipy.interpolate import griddata, RegularGridInterpolator
from scipy.ndimage import gaussian_filter
import matplotlib.colors as cor
from collections import Counter

''' Convert class_id to class name '''
def class_id_to_class_name(class_id):
    class_id = int(class_id)
    if class_id == 1: class_name = 'people-helmet'
    elif class_id == 2: class_name = 'people-no-helmet'
    elif class_id == 3: class_name = 'PC'
    elif class_id == 4: class_name = 'PC-truck'
    elif class_id == 5: class_name = 'dump-truck'
    elif class_id == 6: class_name = 'mixer'
    elif class_id == 7: class_name = 'excavator'
    elif class_id == 8: class_name = 'wheel-loader'
    elif class_id == 9: class_name = 'dozer'
    elif class_id == 10: class_name = 'roller'
    return class_name

''' Calculate total number of frames '''
def total_frame():
    total_frame = 0
    for subset in ['videos/train/', 'videos/val/', 'videos/test/']:
        all_video_name = glob.glob(glob.escape(subset)+'/*.mp4')
        for video_name in all_video_name:
            video = cv2.VideoCapture(video_name)
            frame = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
            total_frame += frame
    print('\nTotal number of frames: ', total_frame)
    return total_frame

''' Calculate total number of instances '''
def total_instance():
    total_instance = 0
    all_annotation_file = []
    for subset in ['annotations/CMOT-train/*/*.txt','annotations/CMOT-val/*/*.txt','annotations/CMOT-test/*/*.txt']:
        all_annotation_file += glob.glob(subset)
    for annotation in all_annotation_file:
        with open(annotation, 'r') as f:
            for line in f: total_instance += 1
    print('\nTotal number of instances: ', total_instance)
    return total_instance

''' Visualize number of frames per category '''
def number_of_frames_per_category(save_path):
    train_video_name = [name[-8:-4] for name in glob.glob('videos/train/*.mp4')]
    val_video_name = [name[-8:-4] for name in glob.glob('videos/val/*.mp4')]
    test_video_name = [name[-8:-4] for name in glob.glob('videos/test/*.mp4')]

    all_category = []
    all_annotation_file = []
    for subset in ['annotations/CMOT-train/*/*.txt','annotations/CMOT-val/*/*.txt','annotations/CMOT-test/*/*.txt']:
        all_annotation_file += glob.glob(subset)
    for annotation in all_annotation_file:
        if annotation[-11:-7] in val_video_name:
            with open(annotation, 'r') as f:
                for line in f:
                    class_id = line.strip().split(', ')[-2]
                    class_name = class_id_to_class_name(class_id)
                    all_category.append(class_name)            
    all_category = list(set(all_category)) # remove duplicates    

    number_of_frames_per_category_all = {}
    number_of_frames_per_category_train = {}
    number_of_frames_per_category_val = {}
    number_of_frames_per_category_test = {}
    for category in all_category:
        number_of_frames_per_category_all[category] = 0
        number_of_frames_per_category_train[category] = 0
        number_of_frames_per_category_val[category] = 0
        number_of_frames_per_category_test[category] = 0

    for annotation in all_annotation_file:
        # calculate number of frames per category for all subsets
        with open(annotation, 'r') as f:
            for line in f:
                class_name = class_id_to_class_name(line.strip().split(', ')[-2])
                number_of_frames_per_category_all[class_name] += 1

        # calculate number of frames per category for train subset
        if annotation[-11:-7] in train_video_name:
            with open(annotation, 'r') as f:
                for line in f:
                    class_name = class_id_to_class_name(line.strip().split(', ')[-2])
                    number_of_frames_per_category_train[class_name] += 1

        # calculate number of frames per category for val subset
        elif annotation[-11:-7] in val_video_name:
            with open(annotation, 'r') as f:
                for line in f:
                    class_name = class_id_to_class_name(line.strip().split(', ')[-2])
                    number_of_frames_per_category_val[class_name] += 1

        # calculate number of frames per category for test subset
        elif annotation[-11:-7] in test_video_name:
            with open(annotation, 'r') as f:
                for line in f:
                    class_name = class_id_to_class_name(line.strip().split(', ')[-2])
                    number_of_frames_per_category_test[class_name] += 1
    
    # reorder keys
    desired_order = ['people-helmet', 'people-no-helmet', 'PC', 'PC-truck', 'dump-truck', 'mixer', 'excavator', 'roller', 'dozer', 'wheel-loader']
    number_of_frames_per_category_all = {k: number_of_frames_per_category_all[k] for k in desired_order}
    number_of_frames_per_category_train = {k: number_of_frames_per_category_train[k] for k in desired_order}
    number_of_frames_per_category_val = {k: number_of_frames_per_category_val[k] for k in desired_order}
    number_of_frames_per_category_test = {k: number_of_frames_per_category_test[k] for k in desired_order}
    print('\nNumber of frames per category:\n', number_of_frames_per_category_all)

    # plot
    fig, ax = plt.subplots(figsize=(12,6), dpi=1000)
    plt.rcParams['font.size'] = '22'
    plt.rcParams['font.family'] = 'Times New Roman'
    for label in (ax.get_xticklabels() + ax.get_yticklabels()): label.set_fontsize(22)

    x_categories = list(number_of_frames_per_category_all.keys())
    x_axis = np.arange(len(number_of_frames_per_category_all))
    y_1 = list(number_of_frames_per_category_all.values())
    y_2 = list(number_of_frames_per_category_train.values())
    y_3 = list(number_of_frames_per_category_val.values())
    y_4 = list(number_of_frames_per_category_test.values())

    ax.bar(x_axis-0.3, y_1, 0.2, label='ALL')
    ax.bar(x_axis-0.1, y_2, 0.2, label='Train')
    ax.bar(x_axis+0.1, y_3, 0.2, label='Val')
    ax.bar(x_axis+0.3, y_4, 0.2, label='Test')
    ax.set_ylabel('Number of Frames', fontsize=22, font='Times New Roman')
    plt.xticks(range(len(number_of_frames_per_category_all)), list(number_of_frames_per_category_all.keys()), rotation=30, ha='right', font='Times New Roman')
    plt.yscale('log', base=10)
    plt.ylim([1, 200000])
    plt.yticks([1, 10, 100, 1000, 10000, 100000], font='Times New Roman')
    #ax.set_title("Number of Frames per Category", fontsize=24, weight='bold', font='Times New Roman')
    ax.legend(ncol=4)
    plt.savefig(save_path + '1-number_of_frames_per_category.jpg', bbox_inches='tight')

''' Visualize number of instances/categories per frame '''
def number_of_instances_and_categories_per_frame(total_frame, save_path):
    instances_per_frame = {}
    categories_per_frame = {}
    for i in range(5):
        instances_per_frame[i+1] = 0
        categories_per_frame[i+1] = 0
    instances_per_frame['>5'] = 0
    categories_per_frame['>5'] = 0

    all_annotation_file = []
    for subset in ['annotations/CMOT-train/*/*.txt','annotations/CMOT-val/*/*.txt','annotations/CMOT-test/*/*.txt']:
        all_annotation_file += glob.glob(subset)
    for annotation in all_annotation_file:
        # calculate number of instances per frame
        with open(annotation, 'r') as f:
            frame = []
            for line in f: frame.append(line.strip().split(', ')[0])
            instance_num = {i:frame.count(i) for i in frame}
            for i, (k, v) in enumerate(instance_num.items()):
                if v < 5: instances_per_frame[v] += 1
                else: instances_per_frame['>5'] += 1
        
        # calculate number of categories per frame
        with open(annotation, 'r') as f:
            category_num = {i:[] for i in frame}
            for line in f:
                class_name = class_id_to_class_name(line.strip().split(', ')[-2])
                category_num[line.strip().split(', ')[0]].append(class_name)
            for i, (k, v) in enumerate(category_num.items()):
                if len(list(set(v))) < 5: categories_per_frame[len(list(set(v)))] += 1
                else: categories_per_frame['>5'] += 1
            
    for i, (k, v) in enumerate(instances_per_frame.items()): instances_per_frame[k] = round(v/total_frame, 2)
    for i, (k, v) in enumerate(categories_per_frame.items()): categories_per_frame[k] = round(v/total_frame, 2)
    print('\nNumber of instances per frame:\n', instances_per_frame)
    print('\nNumber of categories per frame:\n', categories_per_frame)

    # plot
    fig, ax = plt.subplots(figsize=(12,6), dpi=1000)
    plt.rcParams['font.size'] = '22'
    plt.rcParams['font.family'] = 'Times New Roman'
    for label in (ax.get_xticklabels() + ax.get_yticklabels()): label.set_fontsize(22)
  
    x_categories = list(instances_per_frame.keys())
    x_axis = np.arange(len(instances_per_frame))
    y_1 = list(instances_per_frame.values())
    y_2 = list(categories_per_frame.values())

    ax.plot(x_categories, y_1, linewidth='2', marker='.', markersize=15, label='Instances')
    ax.plot(x_categories, y_2, linewidth='2', marker='^', markersize=10, label='Categories')
    plt.xticks(font='Times New Roman')
    plt.yticks(font='Times New Roman')
    #ax.set_title("Instances/Categories per Image", fontsize=24, weight='bold', font='Times New Roman')
    ax.set_xlabel('Number of Instances/Categories', fontsize=22, font='Times New Roman')
    ax.set_ylabel('Percentage of Frames', fontsize=22, font='Times New Roman')
    ax.legend()

    for l in [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]: ax.axhline(y=l, linewidth=0.1, color='gray')
    ax.set_yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
    plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1.0))
    plt.savefig(save_path + '2-instances-categories-per-frame.jpg', bbox_inches='tight')
    
                
''' Visualize percentage of frame size '''              
def percentage_of_image_size(save_path):
    percentage_of_size = {'(0%, 10%]':0,'(10%, 20%]':0,'(20%, 30%]':0,'(30%, 40%]':0,'(40%, 100%]':0}
    
    for subset in ['videos/train/', 'videos/val/', 'videos/test/']:
        all_video_name = glob.glob(glob.escape(subset)+'/*.mp4')
        for video_name in all_video_name:
            video = cv2.VideoCapture(video_name)
            frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
            frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
            frame_area = frame_width * frame_height

            with open('annotations/CMOT-'+subset[7:-1]+'/'+video_name[-8:-4]+'/gt.txt', 'r') as f:
                for line in f:
                    bbox_area = int(line.strip().split(', ')[4]) * int(line.strip().split(', ')[5])
                    area_ratio = bbox_area / frame_area

                    if area_ratio>0 and area_ratio<=0.1: percentage_of_size['(0%, 10%]']+=1
                    elif area_ratio>0.1 and area_ratio<=0.2: percentage_of_size['(10%, 20%]']+=1
                    elif area_ratio>0.2 and area_ratio<=0.3: percentage_of_size['(20%, 30%]']+=1
                    elif area_ratio>0.3 and area_ratio<=0.4: percentage_of_size['(30%, 40%]']+=1
                    elif area_ratio>0.4 and area_ratio<=1: percentage_of_size['(40%, 100%]']+=1

    percentage_of_size = {i: round(percentage_of_size[i] / sum(percentage_of_size.values()), 2) for i in percentage_of_size}              
    print('\nPercentage of size:\n', percentage_of_size)

    # plot
    fig, ax = plt.subplots(figsize=(12,6), dpi=1000)
    plt.rcParams['font.size'] = '22'
    plt.rcParams['font.family'] = 'Times New Roman'
    for label in (ax.get_xticklabels() + ax.get_yticklabels()): label.set_fontsize(22)
    
    x_categories = list(percentage_of_size.keys())
    x_axis = np.arange(len(percentage_of_size))
    y = list(percentage_of_size.values())
    ax.bar(x_categories, y, 0.4)
    plt.xticks(font='Times New Roman')
    plt.yticks(font='Times New Roman')
    #ax.set_title("Instance Size", fontsize=24, weight='bold', font='Times New Roman')
    ax.set_xlabel('Percentage of Image Size', fontsize=22, font='Times New Roman')
    ax.set_ylabel('Percentage of Instances', fontsize=22, font='Times New Roman')

    for l in [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]: ax.axhline(y=l, linewidth=0.1, color='gray')
    ax.set_yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
    plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1.0))
    plt.savefig(save_path + '3-percentage-of-size.jpg', bbox_inches='tight')

def log_tick_formatter(val, pos=None):
    return f'$10^{{{int(val)}}}$'
    # return f'{10**val:.2e}' # e-Notation

''' Visualize frame number v.s. instance number v.s. category number '''
def video_vs_frames_vs_category(total_frame, save_path):
    # [number of videos, number of annotated frames, number of annotated categories]
    CMOT = [math.log10(100), math.log10(total_frame), math.log10(10)]
    EO = [math.log10(10), math.log10(89066), math.log10(2)]
    MOT17 = [math.log10(14), math.log10(11235), math.log10(11)]
    MOT20 = [math.log10(8), math.log10(13410), math.log10(13)]
    KITTI = [math.log10(21), math.log10(8008), math.log10(2)]
    
    # plot
    fig = plt.figure(figsize=(10,6), dpi=600)
    ax = fig.add_subplot(projection='3d')

    plt.rcParams['font.size'] = '14'
    plt.rcParams['font.family'] = 'Times New Roman'
    plt.rcParams["figure.autolayout"] = True
    for label in (ax.get_xticklabels() + ax.get_yticklabels()): label.set_fontsize(12)

    ''' CMOT '''
    ax.scatter(np.array([CMOT[0]]), np.array([CMOT[1]]), np.array([CMOT[2]]), c='red', s=200)
    ax.text(CMOT[0]*1.03, CMOT[1]*1.01, CMOT[2]*1.05, 'CMOT', fontsize = 14)

    p = Circle((CMOT[0], CMOT[1]), 0.08, edgecolor='black', facecolor='red')
    ax.add_patch(p)
    art3d.pathpatch_2d_to_3d(p, z=0, zdir="z")

    p = Circle((CMOT[1], CMOT[2]), 0.08, edgecolor='black', facecolor='red')
    ax.add_patch(p)
    art3d.pathpatch_2d_to_3d(p, z=0, zdir="x")

    #p = Circle((CMOT[0], CMOT[2]), 0.08, edgecolor='black', facecolor='red')
    #ax.add_patch(p)
    #art3d.pathpatch_2d_to_3d(p, z=6.1, zdir="y")
    
    ''' EO '''
    ax.scatter(np.array([EO[0]]), np.array([EO[1]]), np.array([EO[2]]), c='blue', s=200)
    ax.text(EO[0]*1, EO[1]*1.05, EO[2]*0.9, 'EO', fontsize = 14)

    p = Circle((EO[0], EO[1]), 0.08, edgecolor='black', facecolor='blue')
    ax.add_patch(p)
    art3d.pathpatch_2d_to_3d(p, z=0, zdir="z")

    p = Circle((EO[1], EO[2]), 0.08, edgecolor='black', facecolor='blue')
    ax.add_patch(p)
    art3d.pathpatch_2d_to_3d(p, z=0, zdir="x")

    #p = Circle((EO[0], EO[2]), 0.08, edgecolor='black', facecolor='blue')
    #ax.add_patch(p)
    #art3d.pathpatch_2d_to_3d(p, z=6.1, zdir="y")
    
    ''' MOT17 '''
    ax.scatter(np.array([MOT17[0]]), np.array([MOT17[1]]), np.array([MOT17[2]]), c='purple', s=200)
    ax.text(MOT17[0]*1.05, MOT17[1]*1.03, MOT17[2]*1, 'MOT17', fontsize = 14)

    p = Circle((MOT17[0], MOT17[1]), 0.08, edgecolor='black', facecolor='purple')
    ax.add_patch(p)
    art3d.pathpatch_2d_to_3d(p, z=0, zdir="z")

    p = Circle((MOT17[1], MOT17[2]), 0.08, edgecolor='black', facecolor='purple')
    ax.add_patch(p)
    art3d.pathpatch_2d_to_3d(p, z=0, zdir="x")

    #p = Circle((MOT17[0], MOT17[2]), 0.08, edgecolor='black', facecolor='purple')
    #ax.add_patch(p)
    #art3d.pathpatch_2d_to_3d(p, z=6.1, zdir="y")

    ''' MOT20 '''
    ax.scatter(np.array([MOT20[0]]), np.array([MOT20[1]]), np.array([MOT20[2]]), c='green', s=200)
    ax.text(MOT20[0]*1.06, MOT20[1]*1.02, MOT20[2]*1.02, 'MOT20', fontsize = 14)

    p = Circle((MOT20[0], MOT20[1]), 0.08, edgecolor='black', facecolor='green')
    ax.add_patch(p)
    art3d.pathpatch_2d_to_3d(p, z=0, zdir="z")

    p = Circle((MOT20[1], MOT20[2]), 0.08, edgecolor='black', facecolor='green')
    ax.add_patch(p)
    art3d.pathpatch_2d_to_3d(p, z=0, zdir="x")

    #p = Circle((MOT20[0], MOT20[2]), 0.08, edgecolor='black', facecolor='green')
    #ax.add_patch(p)
    #art3d.pathpatch_2d_to_3d(p, z=6.1, zdir="y")

    ''' KITTI '''
    ax.scatter(np.array([KITTI[0]]), np.array([KITTI[1]]), np.array([KITTI[2]]), c='pink', s=200)
    ax.text(KITTI[0]*1.06, KITTI[1]*1.02, KITTI[2]*0.9, 'KITTI-MOT', fontsize = 14)

    p = Circle((KITTI[0], KITTI[1]), 0.08, edgecolor='black', facecolor='pink')
    ax.add_patch(p)
    art3d.pathpatch_2d_to_3d(p, z=0, zdir="z")

    p = Circle((KITTI[1], KITTI[2]), 0.08, edgecolor='black', facecolor='pink')
    ax.add_patch(p)
    art3d.pathpatch_2d_to_3d(p, z=0, zdir="x")

    #p = Circle((KITTI[0], KITTI[2]), 0.08, edgecolor='black', facecolor='pink')
    #ax.add_patch(p)
    #art3d.pathpatch_2d_to_3d(p, z=6.1, zdir="y")

    # plot
    #ax.set_title("Number of Frames V.S. Number of Instances", fontsize=12, weight='bold', font='Times New Roman')
    ax.set_xlabel('Number of Videos', fontsize=14, font='Times New Roman')
    ax.set_ylabel('Number of Frames', fontsize=14, font='Times New Roman')
    ax.set_zlabel('Number of Categories', fontsize=14, font='Times New Roman')

    ax.set_xlim(0, 2.1)
    ax.set_ylim(3.5, 6.1)
    ax.set_zlim(0, 1.5)

    ax.xaxis.set_major_formatter(mtick.FuncFormatter(log_tick_formatter))
    ax.xaxis.set_major_locator(mtick.MaxNLocator(integer=True))
    ax.yaxis.set_major_formatter(mtick.FuncFormatter(log_tick_formatter))
    ax.yaxis.set_major_locator(mtick.MaxNLocator(integer=True))
    ax.zaxis.set_major_formatter(mtick.FuncFormatter(log_tick_formatter))
    ax.zaxis.set_major_locator(mtick.MaxNLocator(integer=True))
    
    ax.view_init(10, -60)
    plt.savefig(save_path + '4-frame-vs-instance.jpg', bbox_inches='tight')


''' Visualize location distribution of all categories '''
def all_location_distribution(save_path):
    center_coordinates_x, center_coordinates_y = [], []
    for subset in ['videos/train/','videos/val/','videos/test/']:
        all_video_name = glob.glob(glob.escape(subset)+'/*.mp4')
        for video_name in all_video_name:
            video = cv2.VideoCapture(video_name)
            frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
            frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
            with open('annotations/CMOT-'+subset[7:-1]+'/'+video_name[-8:-4]+'/gt.txt', 'r') as f:
                for line in f:
                    center_x = int(line.strip().split(', ')[2]) + int(line.strip().split(', ')[4])/2
                    center_y = int(line.strip().split(', ')[3]) + int(line.strip().split(', ')[5])/2
                    norm_center_x = (center_x-0) / (frame_width-0) # min-max normalization
                    norm_center_y = (center_y-0) / (frame_height-0)
                    center_coordinates_x.append(norm_center_x)
                    center_coordinates_y.append(norm_center_y)                                    
    # plot
    fig, ax = plt.subplots(figsize=(6,6), dpi=1000)
    divider = make_axes_locatable(ax)
    cax = divider.append_axes('right', size='5%', pad=0.05)
    plt.rcParams['font.family'] = 'Times New Roman'
    sigma = 16
    bins = 100
    heatmap, xedges, yedges = np.histogram2d(center_coordinates_x,center_coordinates_y, bins=bins)
    heatmap = gaussian_filter(heatmap, sigma)
    im = ax.imshow(heatmap, origin='upper', cmap=cm.viridis) # 'upper' indicates (0,0) at the left upper corner
    ax.get_xaxis().set_ticks([])
    ax.get_yaxis().set_ticks([])
    ax.axis('off')
    fig.colorbar(im, cax=cax, orientation='vertical')
    plt.savefig(save_path + '5-location-distribution.jpg', bbox_inches='tight')


''' Visualize location distribution of each category '''
def location_distribution_per_category(save_path):
    all_category = []
    val_video_name = [name[-8:-4] for name in glob.glob('videos/test/*.mp4')]
    all_annotation_file = []
    for subset in ['annotations/CMOT-train/*/*.txt','annotations/CMOT-val/*/*.txt','annotations/CMOT-test/*/*.txt']:
        all_annotation_file += glob.glob(subset)
    for annotation in all_annotation_file:
        if annotation[-11:-7] in val_video_name:
            with open(annotation, 'r') as f:
                for line in f:
                    class_name = class_id_to_class_name(line.strip().split(', ')[-2])
                    all_category.append(class_name)            
    all_category = list(set(all_category))

    for category in all_category:
        center_coordinates_x, center_coordinates_y = [], []
        for subset in ['videos/train/','videos/val/','videos/test/']:
            all_video_name = glob.glob(glob.escape(subset)+'/*.mp4')
            for video_name in all_video_name:
                video = cv2.VideoCapture(video_name)
                frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
                frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

                with open('annotations/CMOT-'+subset[7:-1]+'/'+video_name[-8:-4]+'/gt.txt', 'r') as f:
                    for line in f:
                        class_name = class_id_to_class_name(line.strip().split(', ')[-2])
                        if class_name == category:
                            center_x = int(line.strip().split(', ')[2]) + int(line.strip().split(', ')[4]) / 2
                            center_y = int(line.strip().split(', ')[3]) + int(line.strip().split(', ')[5]) / 2
                            norm_center_x = center_x / frame_width # min-max normalization
                            norm_center_y = center_y / frame_height
                            center_coordinates_x.append(norm_center_x)
                            center_coordinates_y.append(norm_center_y)     
        # plot
        fig, ax = plt.subplots(figsize=(6,6), dpi=1000)
        plt.rcParams['font.family'] = 'Times New Roman'  
        sigma = 16
        bins = 100
        heatmap, xedges, yedges = np.histogram2d(center_coordinates_x,center_coordinates_y, bins=bins)
        heatmap = gaussian_filter(heatmap, sigma)
        im = ax.imshow(heatmap, origin='upper', cmap=cm.viridis) # 'upper' indicates (0,0) at the left upper corner
        ax.get_xaxis().set_ticks([])
        ax.get_yaxis().set_ticks([])
        ax.axis('off')
        plt.savefig(save_path + '6-location-distribution_'+class_name+'.jpg', bbox_inches='tight')    

        
if __name__ == '__main__':
    save_path = 'statistics/'
    if not os.path.exists(save_path): os.makedirs(save_path)
    total_frame = total_frame() 
    total_instance = total_instance() 
    number_of_frames_per_category(save_path) 
    number_of_instances_and_categories_per_frame(total_frame, save_path) 
    percentage_of_image_size(save_path)
    video_vs_frames_vs_category(total_frame, save_path)
    all_location_distribution(save_path)
    location_distribution_per_category(save_path)
