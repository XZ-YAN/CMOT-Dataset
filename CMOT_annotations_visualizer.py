# coding=UTF-8
# Code Author: Xuzhong Yan
import os, sys, time, glob, math, cv2, turtle, ast, random, imageio, base64, json, shutil
from tqdm import tqdm
from functools import reduce
from imgaug.augmentables.bbs import BoundingBox, BoundingBoxesOnImage
import matplotlib.pyplot as plt
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
import mpl_toolkits.mplot3d.art3d as art3d
import pycocotools.mask as rletools
import moviepy.video.io.ImageSequenceClip

''' Convert images to a video '''
def pic2video(image_folder, video_output_name, fps):
    print('converting pic to video')
    for i in [image_folder]:
        all_file_name = glob.glob(os.path.join(i, '*.jpg'))
    clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(all_file_name, fps)
    clip.write_videofile(image_folder + '/' +video_output_name+'_annotation.mp4')

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

''' Visualize annotations in videos '''
def annotation_visualizer():
    for subset in ['videos/test/']: #'videos/train/', 'videos/val/', 
        all_video_name = [name[-8:-4] for name in glob.glob(glob.escape(subset)+'/*.mp4')]
        for video_name in all_video_name:
            save_path = subset+'frame/'
            if not os.path.exists(save_path): os.mkdir(save_path)

            # load video
            video = cv2.VideoCapture(subset+video_name+'.mp4')
            width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
            FPS = video.get(cv2.CAP_PROP_FPS)
            num_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
            print('* processing '+video_name)
            
            # load bbox annotation
            bbox_annotation_file = open('annotations/CMOT-'+subset[7:-1]+'/'+video_name+'/gt.txt', 'r')
            bbox_annotation = []
            for line in bbox_annotation_file: # frame, ID, xmin, ymin, box_width, box_height, confidence_score, class_id, visibility_level
                bbox_annotation.append(line.strip().split(', '))
           
            i = 1
            pbar = tqdm(desc='while loop', total = num_frames)
            while i <= num_frames:
                hasFrame, frame = video.read()                
                image = frame.copy()
                
                # draw bbox
                for bbox in bbox_annotation:
                    if int(bbox[0]) == i:
                        ID = int(bbox[1])
                        # bbox color 
                        if ID == 1: fill = (255,0,0,150)
                        elif ID == 2: fill = (0,255,0,150)
                        elif ID == 3: fill = (0,0,225,150)
                        elif ID == 4: fill = (255,153,18,150)
                        elif ID == 5: fill = (160,32,240,150)
                        elif ID == 6: fill = (255,225,0,150)
                        elif ID == 7: fill = (0,255,255,150)
                        elif ID == 8: fill = (128,128,0,150)
                        elif ID == 9: fill = (255,0,255,150)
                        elif ID == 10: fill = (255,127,80,150)
                        elif ID == 11: fill = (138,43,226,150)
                        elif ID == 12: fill = (139,69,19,150)
                        elif ID == 13: fill = (112,128,144,150)
                        elif ID == 14: fill = (248,248,255,150)
                        elif ID == 15: fill = (65,105,225,150)
                        elif ID == 16: fill = (25,25,112,150)
                        elif ID == 17: fill = (139,69,19,150)
                        elif ID == 18: fill = (128,128,128,150)
                        elif ID == 19: fill = (255,69,0,150)
                        elif ID == 20: fill = (124,252,0,150)
                        
                        xmin = int(bbox[2])
                        ymin = int(bbox[3])
                        xmax = int(bbox[2]) + int(bbox[4])
                        ymax = int(bbox[3]) + int(bbox[5])
                        image = Image.fromarray(np.uint8(image))
                        ImageDraw.Draw(image,'RGBA').rectangle([xmin, ymin, xmax, ymax], outline=fill, width=5)
                        class_name = class_id_to_class_name(bbox[7])
                        # draw class & ID
                        x, y = int((xmin + xmax)/2), int((ymin + ymax)/2)
                        image = np.array(image)
                        cv2.putText(image, class_name, (x-10, y-12), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), 2)
                        cv2.putText(image, 'id: '+str(ID), (x-10, y+12), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), 2)

                        if len(str(i)) == 1: dst = '000000000'+str(i)
                        elif len(str(i)) ==2: dst ='00000000'+str(i)
                        elif len(str(i)) ==3: dst ='0000000'+str(i)
                        elif len(str(i)) ==4: dst ='000000'+str(i)
                        elif len(str(i)) ==5: dst ='00000'+str(i)
                        elif len(str(i)) ==6: dst ='0000'+str(i)                    
                        cv2.imwrite(save_path+str(dst)+'.jpg', image)
                i+=1
                pbar.update(1)
                            
            video.release()
            cv2.destroyAllWindows()
            
            pic2video(subset+'frame/', video_name, FPS)
            shutil.move(subset+'frame/'+video_name+'_annotation.mp4', subset+video_name+'_annotation.mp4')
            shutil.rmtree(subset+'frame/')     
    
if __name__ == '__main__':
    annotation_visualizer()

