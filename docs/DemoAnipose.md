# Introduction to Anipose
Anipose is an open-source Python toolkit for robust, markerless 3D pose estimation of animal behavior from multiple camera views.

**Documentation:** https://anipose.readthedocs.io/en/latest/  
**Sourcecode:** https://github.com/lambdaloop/anipose


Anipose is built on DeepLabCut for markerless tracking, and can be used to expand existing 2D projects with multiple cameras. It consists of a 3D camera calibration module, triangulation of 2D tracked coordinates, and a set of filters to resolve tracking errors both in 2D and 3D models. Synchronized cameras are needed to record behavior from multiple views, and calibration boards such as [ChArUco](https://docs.opencv.org/3.4/df/d4a/tutorial_charuco_detection.html) are used to calculate camera parameters such as relative position and orientation in space. 


```{figure} content/anipose.PNG
---
width: 600px
name: anipose
---
Anipose workflow from Karashchuk et al. 2021.
```

## Installation

Unfortunately, the installation of Anipose is still a bit tricky, but checking similar [Github issues](https://github.com/lambdaloop/anipose/issues) often helps. Anipose will will be installed on top of your DeepLabCut environment, but I recommend having a new environment with a new DeepLabCut installation.
Anipose will analyze your videos using a pre-trained DeepLabCut project, and a GPU will be faster but is not strictly necessary.  
If you have Anaconda already installed, follow the steps below: 

1. Download the yaml [installation file](http://www.mackenziemathislab.org/s/DEEPLABCUT.yaml) 

2. `cd Downloads`

3. `conda env create -f DEEPLABCUT.yaml`

4. `conda activate DEEPLABCUT`

5. `pip install -U wxPython`

6. `pip uninstall opencv-python`

7. install Anipose with `pip install anipose`

8. `conda install mayavi ffmpeg`

9. `pip install --upgrade apptools`

10. check if Anipose was installed with `anipose` 

:::{note}
When you encounter errors (not if, when...), please check the console output carefully and refer to the known [Github issues](https://github.com/lambdaloop/anipose/issues).
:::



## Documentation

Karashchuk, P., Rupp, K. L., Dickinson, E. S., Walling-Bell, S., Sanders, E., Azim, E., Brunton, B. W., & Tuthill, J. C. (2021). Anipose: A toolkit for robust markerless 3D pose estimation. Cell Reports, 36(13), 109730. https://doi.org/10.1016/j.celrep.2021.109730


<iframe width="800" height="500" src="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8498918/pdf/nihms-1744538.pdf"></iframe>
