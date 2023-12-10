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
  |0002|  20| 2560*1240| 820| Static| High|	Rainy| 1|	mixer|
  |0007|  25| 1920*980|	800| Static| High| Sunny|	2| dump-truck|
  |0008|  25|	1920*980| 850| Static| High| Cloudy| 2| people-helmet|
  |0009|  25|	1920*980| 800| Static| High| Cloudy| 2| people-helmet|
  |0011|  25|	1920*780|	800| Static| High| Sunny|	4| people-helmet, people-no-helmet|
  |0013|  25|	1920*880|	800| Static| High| Sunny| 6| people-helmet, people-no-helmet|
  |0015|  25|	1180*520|750| Static|	Medium| Cloudy| 2| people-helmet|
  |0017|  25|	1720*730|	750| Static| High| Cloudy| 4|	dump-truck, excavator|
  |0020|  25|	1080*560|	750| Static| Low| Sunny| 2| dump-truck, excavator|
  |0021|  25|	1280*720|	800| Static| Low| Sunny| 2| dump-truck, mixer|
  |0023|  29|	1820*980|	1009|	Static|	High| Night| 2|	dump-truck, excavator|
  |0024|  25|	1820*780|	750| Static| Medium| Sunny|2|	excavator, wheel-loader|
  |0025|  25|	1620*780|	750| Static| High| Sunny|1|	wheel-loader|
  |0027|  25|	1820*780|750|	Static|	High| Sunny| 2|	dump-truck, excavator|
  |0030|  25|	1820*780|750|	Static|	High|	Sunny| 4|	dump-truck, excavator|
  |0031|  29|	1870*980|	1000|	Static| High| Night| 2| dump-truck, excavator|
  |0032|  29|	1870*980|	928| Static| High| Night|	2| dump-truck, excavator|
  |0033|  25|	1280*720|	750| Moving| Low|	Sunny| 1| roller|
  |0035|	25|	1280*720|	750| Moving| Low|	Sunny| 1| roller|
  |0038|	25|	1720*770|	750| Static| Medium| Sunny|	1| people-helmet|
  |0039|	25|	2460*1130| 800|	Static|	High|	Sunny|	2| people-helmet, people-no-helmet|
  |0040|	25|	1130*520|	925| Static| High| Cloudy|	2| people-helmet, mixer|
  |0041|	25|	1820*680|	800| Static| High| Sunny|	2| people-helmet|
  |0043|	25|	1920*780|	750| Shaky|	High|	Sunny|1| dozer|
  |0044|	25|	1920*780|	750| Shaky|	High|	Sunny|2| dump-truck, dozer|
  |0045|	25|	1920*780|	750| Static| High| Sunny|3| dump-truck, dozer|
  |0048|	25|	1820*980|	750| Static| Medium| Sunny|	4| people-helmet, dump-truck, excavator|
  |0049|	25|	1820*980|	750| Static| Medium| Sunny| 3| excavator|
  |0050|	25|	1820*980|	750| Static| Medium| Sunny|	1| excavator|
  |0054|	25| 1420*880|	750| Static| High| Rainy|	9| people-helmet, PC|
  |0056|	25|	1820*980|	750| Static| Medium| Cloudy|3| mixer, excavator|
  |0057|	25|	1820*880|	750| Static| High| Cloudy| 4| people-helmet|
  |0060|	25|	1820*880|	750| Shaky|	High|	Cloudy|	2| PC-truck|
  |0062|	25|	1480*550|	750| Static| High| Cloudy| 6| people-helmet, PC-truck|
  |0063|	25|	1820*780|	750| Static| High| Cloudy| 3| people-helmet, wheel-loader|
  |0069|	25|	1120*780|	950| Static| High| Night|	2| PC, PC-truck|
  |0071|	25|	1020*880|	750| Static| High| Night|	2| PC, PC-truck|
  |0074|	25|	1820*780|	800| Static| High| Sunny|	1| dozer|
  |0075|	25|	1960*1140| 750|	Static|	Medium|	Cloudy|	2| dump-truck|
  |0077|	25|	1870*980|	750| Shaky|	High|	Cloudy|	2| people-helmet, people-no-helmet|
  |0078|	25|	2460*1040| 800|	Static|	Medium|	Cloudy|	2| people-helmet, roller|
  |0080|	20|	1180*620|	630| Static| Medium| Sunny| 3| people-helmet, mixer|
  |0084|	25|	1870*1010| 800|	Shaky| Medium| Night|	1| excavator|
  |0085|	25|	1820*880|	750| Static| Medium| Cloudy| 1|	excavator|
  |0088|	25|	554*476|	750| Static| High| Cloudy|	1| mixer|
  |0090|	25|	1820*780|	800| Moving| Medium| Sunny|	1| dozer|
  |0091|	25|	1620*680|	750| Shaky|	High|	Sunny| 2| dump-truck, dozer|
  |0092|	25|	1820*980|	750| Static| Medium| Cloudy| 5| people-helmet|
  |0093|	25|	1770*680|	800| Static| Medium| Sunny| 2| mixer|
  |0097|	25|	1920*860|	750| Static| High| Sunny|	4| people-helmet|

* CMOT Validation Set Overview  
  | Name     |FPS	       |Resolution|	Frames    |	Camera   |Viewpoints |Conditions|	IDs       |Categories|
  | ---      | ---       | ---      | ---       | ---      | ---       | ---      | ---       | ---      |
  |0004	|25	|1920*820	|825	|Static	|High	|Sunny	|1	|people-helmet, people-no-helmet|
  |0022	|25	|1720*780	|750	|Static	|High	|Sunny	|3	|dump-truck, excavator, wheel-loader|
  |0028	|29	|1920*980	|900	|Static	|High	|Night	|2	|dump-truck, excavator|
  |0034	|25	|1280*720	|750	|Moving	|Low	|Sunny	|1 	|roller|
  |0046	|25	|1920*780	|750	|Static	|High	|Sunny	|1	|dozer|
  |0047	|25	|1920*780	|750	|Static	|High	|Sunny	|1	|dump-truck|
  |0070	|25	|1420*780	|850	|Static	|High	|Night	|1	|PC|
  |0087	|25	|554*476	|750	|Static	|High	|Cloudy	|1	|mixer|
  |0089	|25	|1820*880	|739	|Static	|Medium	|Rainy	|2	|people-helmet|
  |0096	|25	|620*370	|300	|Static	|Medium	|Cloudy	|1	|PC-truck|

* CMOT Test Set Overview
  | Name     |FPS	       |Resolution|	Frames    |	Camera   |Viewpoints |Conditions|	IDs       |Categories|
  | ---      | ---       | ---      | ---       | ---      | ---       | ---      | ---       | ---      |
  |0001	|25	|1710*810	|1450	|Static	|High|	Cloudy|	2|	mixer|
  |0003	|25	|1820*780	|800	|Static	|Medium|	Sunny|	2|	people-helmet, people-no-helmet|
  |0005	|25	|1920*980	|850	|Static	|Medium|	Sunny|	1|	dump-truck|
  |0006	|25	|1920*980	|850	|Static	|High|	Sunny|	3|	people-helmet, dump-truck|
  |0010	|25	|1920*980	|800	|Static	|Medium|	Sunny|	1|	excavator|
  |0012	|25	|1920*980	|750	|Static	|Medium|	Cloudy|	1|	excavator|
  |0014	|25	|1280*420	|800	|Static	|High|	Cloudy|	2|	people-helmet, people-no-helmet|
  |0016	|25	|1720*730	|750	|Shaky	|High|	Cloudy|	3|	people-no-helmet, wheel-loader|
  |0018	|25	|1720*730	|750	|Shaky	|High|	Cloudy|	4|	dump-truck, excavator|
  |0019	|25	|1720*780	|750	|Static	|High|	Sunny|	1|	wheel-loader|
  |0026	|25	|1820*780	|750	|Shaky	|High|	Sunny|	1|	dozer|
  |0029	|25	|1280*600	|750	|Static	|High|	Sunny|	3|	people-helmet, PC, PC-truck|
  |0036	|25	|1280*720	|750	|Moving	|Low|	Sunny|	1|	roller|
  |0037	|25	|1280*720	|750	|Moving	|Low|	Sunny|	1|	roller|
  |0042	|25	|1820*850	|750	|Static	|High|	Cloudy|	2|	people-helmet|
  |0051	|25	|1820*980	|750	|Static	|Medium|	Cloudy|	1|	excavator|
  |0052	|25	|1820*980	|750	|Static	|Medium|	Cloudy|	1|	excavator|
  |0053	|15	|720*304	|528	|Static	|High|	Cloudy|	7|	people-helmet, people-no-helmet, PC-truck|
  |0055	|25	|640*210	|750	|Static	|High|	Sunny|	2|	PC-truck|
  |0058	|25	|1070*870	|750	|Static	|High|	Night|	2|	PC, PC-truck|
  |0059	|25	|1770*780	|750	|Static	|High|	Night|	2|	mixer|
  |0061	|25	|1820*870	|750	|Static	|High|	Sunny|	19|	people-helmet, PC-truck|
  |0064	|25	|1420*780	|750	|Shaky	|High|	Cloudy|	1|	wheel-loader|
  |0065	|25	|1170*780	|800	|Shaky	|High|	Cloudy|	1|	wheel-loader|
  |0066	|25	|1820*780	|1150	|Shaky	|High|	Cloudy|	1|	dozer|
  |0067	|25	|1870*880	|800	|Shaky	|High|	Sunny|	2|	people-helmet, people-no-helmet|
  |0068	|25	|1820*780	|750	|Static	|High|	Sunny|	5|	people-helmet|
  |0072	|25	|1920*980	|750	|Static	|High|	Sunny|	4|	people-helmet|
  |0073	|25	|1820*780	|750	|Static	|High|	Sunny|	1|	dozer|
  |0076	|25	|1770*840	|750	|Static	|Low|	Rainy|	2|	people-helmet, mixer|
  |0079	|25	|1820*780	|850	|Shaky	|High|	Sunny|	1|	dozer|
  |0081	|25	|620*370	|234	|Static	|Medium|	Cloudy|	1|	PC-truck|
  |0082	|25	|1180*620	|750	|Static	|Medium|	Sunny|	3|	people-helmet, mixer|
  |0083	|25	|570*210	|800	|Static	|High|	Sunny|	3|	people-helmet, PC-truck|
  |0086	|25	|1780*940	|750	|Static	|High|	Sunny|	7|	people-helmet|
  |0094	|25	|1670*730	|750	|Static	|Medium|	Sunny|	1|	excavator|
  |0095	|25	|620*370	|300	|Static	|Medium|	Cloudy|	2|	people-helmet, PC-truck|
  |0098	|25	|1820*980	|750	|Static	|High|	Night|	2|	people-helmet|
  |0099	|25	|1720*880	|750	|Static	|High|	Night|	8|	people-helmet|
  |0100	|25	|1520*780	|1000	|Static	|Low|	Sunny|	1|	people-helmet|

## License
* The CMOT dataset is licensed under a [Creative Commons Attribution-NonCommercial 4.0 International License](http://creativecommons.org/licenses/by-nc/4.0/) to promote the open use of the dataset and future improvements.
* Without permission, the CMOT dataset should only be used for non-commercial scientific research purposes.  

## Citing the CMOT Dataset
If you find this repo useful in your research, please consider citing: (To be updated)
