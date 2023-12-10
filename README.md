# CMOT-Dataset
## Introduction
The Construction Multi-Object Tracking (CMOT) dataset contains 100 videos with more than 77k annotated frames and 155k instances.  

## Construction Object Categories
* 2 categories of workers: workers wearing & not wearing safety helmets.
* 1 categories of materials: precast components (PCs).  
* 7 categories of machines: PC delivery trucks, dump trucks, concrete mixer trucks, excavators, rollers, dozers & wheel loaders.
![Categories](https://github.com/XZ-YAN/CMOT-Dataset/blob/main/demo/categories.jpg)  

## Download the CMOT Dataset  
* [CMOT Videos](https://www.aliyundrive.com/s/bJnzTju4Ra8)  

## Annotation Visualization
* To visualize the dataset annotations, move the downloaded folder into the root directory of this repo and run:  
  `$ python CMOT_annotations_visualizer.py`  
* CMOT annotation samples:
![Annotations](https://github.com/XZ-YAN/CMOT-Dataset/blob/main/demo/samples.gif)  

## Dataset Statistics
* To visualize the dataset statistics, run:  
  `$ python CMOT_statistics_visualizer.py`  
* CMOT statistics:  
![Statistics](https://github.com/XZ-YAN/CMOT-Dataset/blob/main/demo/statistics.jpg)

* CMOT Training Set Overview
  | Name     |FPS	       |Resolution|	Frames    |	Camera   |Viewpoints |Conditions|	IDs       |Categories|
  | ---      | ---       | ---      | ---       | ---      | ---       | ---      | ---       | ---      |
  |0002|  20| 2560*1240| 820|	Static| High|	Rainy|	1|	mixer|
  |0007|  25| 1920*980|	800|	Static|	High|	Sunny|	2	|dump-truck|
  |0008|  25|	1920*980| 850|	Static| High|	Cloudy|	2	|people-helmet|
  |0009|  25|	1920*980| 800| Static| High|	Cloudy|	2	|people-helmet|
  |0011|  25|	1920*780|	800|	Static|	High| Sunny|	4|	people-helmet, people-no-helmet|
  |0013|  25|	1920*880|	800|	Static|	High|	Sunny	|6|	people-helmet, people-no-helmet|
  |0015|  25|	1180*520|750| Static|	Medium| Cloudy	|2|	people-helmet|
  |0017|  25|	1720*730|	750| Static| High| Cloudy|	4|	dump-truck, excavator|
  |0020|  25|	1080*560|	750| Static| Low| Sunny|	2	|dump-truck, excavator|
  |0021|  25|	1280*720|	800|	Static|	Low| Sunny|	2	|dump-truck, mixer|
  |0023|  29|	1820*980|	1009|	Static|	High| Night|	2|	dump-truck, excavator|
  |0024|  25|	1820*780|	750| Static| Medium|	Sunny	|2|	excavator, wheel-loader|
  |0025|  25|	1620*780|	750| Static| High|	Sunny	|1|	wheel-loader|
  |0027|  25|	1820*780|750|	Static|	High| Sunny|	2|	dump-truck, excavator|
  |0030|  25|	1820*780|750|	Static|	High|	Sunny|	4|	dump-truck, excavator|
  |0031|  29|	1870*980|	1000|	Static| High| Night|	2	|dump-truck, excavator|
  |0032|  29|	1870*980|	928| Static| High|	Night|	2|	dump-truck, excavator|
  |0033|  25|	1280*720|	750| Moving| Low|	Sunny|	1| 	roller|
  |0035|	25|	1280*720|	750| Moving| Low|	Sunny|	1| 	roller|
  |0038|	25|	1720*770|	750| Static| Medium|	Sunny|	1	|people-helmet|
  |0039|	25|	2460*1130| 800|	Static|	High|	Sunny|	2	|people-helmet, people-no-helmet|
  |0040|	25|	1130*520|	925| Static|	High|	Cloudy|	2	|people-helmet, mixer|
  |0041|	25|	1820*680|	800| Static|	High|	Sunny|	2|	people-helmet|
  |0043|	25|	1920*780|	750| Shaky|	High|	Sunny	|1|	dozer|
  |0044|	25|	1920*780|	750| Shaky|	High|	Sunny	|2|	dump-truck, dozer|
  |0045|	25|	1920*780|	750| Static|	High|	Sunny	|3	|dump-truck, dozer|
  |0048|	25|	1820*980|	750| Static|	Medium|	Sunny|	4|	people-helmet, dump-truck, excavator|
  |0049|	25|	1820*980|	750| Static|	Medium|	Sunny	|3	|excavator|
  |0050|	25|	1820*980|	750| Static|	Medium|	Sunny|	1|	excavator|
  |0054|	25| 1420*880|	750| Static|	High|	Rainy|	9|	people-helmet, PC|
  |0056|	25|	1820*980|	750| Static|	Medium|	Cloudy	|3|	mixer, excavator|
  |0057|	25|	1820*880|	750| Static|	High|	Cloudy|	4|	people-helmet|
  |0060|	25|	1820*880|	750| Shaky|	High|	Cloudy|	2|	PC-truck|
  |0062|	25|	1480*550|	750| Static|	High|	Cloudy|	6	|people-helmet, PC-truck|
  |0063|	25|	1820*780|	750| Static|	High|	Cloudy|	3	|people-helmet, wheel-loader|
  |0069|	25|	1120*780|	950| Static|	High|	Night|	2	|PC, PC-truck|
  |0071|	25|	1020*880|	750| Static|	High|	Night|	2	|PC, PC-truck|
  |0074|	25|	1820*780|	800| Static|	High|	Sunny|	1|	dozer|
  |0075|	25|	1960*1140| 750|	Static|	Medium|	Cloudy|	2	|dump-truck|
  |0077|	25|	1870*980|	750| Shaky|	High|	Cloudy|	2|	people-helmet, people-no-helmet|
  |0078|	25|	2460*1040| 800|	Static|	Medium|	Cloudy|	2|	people-helmet, roller|
  |0080|	20|	1180*620|	630| Static|	Medium|	Sunny	|3|	people-helmet, mixer|
  |0084|	25|	1870*1010| 800|	Shaky|	Medium|	Night|	1	|excavator|
  |0085|	25|	1820*880|	750| Static|	Medium|	Cloudy|	1|	excavator|
  |0088|	25|	554*476|	750| Static|	High|	Cloudy|	1|	mixer|
  |0090|	25|	1820*780|	800| Moving|	Medium|	Sunny|	1|	dozer|
  |0091|	25|	1620*680|	750| Shaky|	High|	Sunny|	2|	dump-truck, dozer|
  |0092|	25|	1820*980|	750| Static|	Medium|	Cloudy|	5|	people-helmet|
  |0093|	25|	1770*680|	800| Static|	Medium|	Sunny	|2|	mixer|
  |0097|	25|	1920*860|	750| Static|	High|	Sunny|	4|	people-helmet|



## License
* The CMOT dataset is licensed under a [Creative Commons Attribution-NonCommercial 4.0 International License](http://creativecommons.org/licenses/by-nc/4.0/) to promote the open use of the dataset and future improvements.
* Without permission, the CMOT dataset should only be used for non-commercial scientific research purposes.  

## Citing the CMOT Dataset
If you find this repo useful in your research, please consider citing: (To be updated)
