# Classification of Animal Behavior


As discussed in the previous lecture on *Quantification of Animal Behavior*, one of the most common methods to measure behavior is the segmentation of time series data into discrete units and clustering or embedding the data into motifs or actions. This lecture will give you a better insight into the classification of animal behavior. Other statistical methods to quantify behavior such as feature distributions will be discussed at a later stage during data analysis exercises in python.

## What is an Ethogram

An *Ethogram* is a list of behavior descriptions that aims to cover the repertoire of species-typical behavior, typically in the wild, or a pre-defined set of behaviors of interest in experimental or animal welfare settings.  

Typically, researchers observe animal behavior either live on-site, via live-stream from a cozy chair, or asynchronously from large datasets of pre-recorded video material. A scoring sheet of pre-defined behaviors of interest, together with a stopwatch or computer, allow to manually log the occurrence and duration of these behaviors at a given temporal resolution, e.g., every 15 seconds. 

<iframe src="https://www.zsl.org/sites/default/files/media/2015-10/KS2%20Behaviour%20study%20booklet%20-%202015_EDUCATION_0.pdf" frameborder="1" width="800" height="600"></iframe>

**Following the instructions above, try to create your own scoring sheet and measure the behavior in the live-stream below:**

* https://nationalzoo.si.edu/webcams/panda-cam
* https://zoo.sandiegozoo.org/cams/ape-cam

## Supervised or Unsupervised, thats is the question

A manual scoring sheet as used in the exercise above would represent a supervised method for behavior classification. For one thing, you hopefully had an idea of what each behavior should look like, to be included in or excluded from a given category. Thus, you created, implicit or explicitly, a set of rules you used to supervise yourself during every classification. In addition, by using a pre-defined set of categories you probably missed some unexpected behaviors. 

Were you to expand your scoring sheet on the fly by every new behavior you observe, that would represent a somewhat more unsupervised approach. But detecting the new behavior, logging it, and giving it a name (i.e., a category with a set of descriptive qualities) all at once would get messy, quick.   

Machine learning models can help us classify the stream of behavior data in a more objective way, but the considerations above still apply to clarify the difference between supervised and unsupervised methods. 

```{figure} content/terminologyML.png
---
width: 800px
name: recapterminologyML
---
Key ML terminology, from Anderson & Perona (2014).
```

## About DeepEthogram
DeepEthogram is a machine learning pipeline for supervised behavior classification from raw pixels. This approach, together with several other methods such as JAABA, SimBA, MARS, MotionMapper, Behave-Net, B-SOiD and VAME, certainly represents an important milestone in computational ethology. For one thing, they apply an ingenious combination of machine learning models to analyze and classify behavior from video data; for another, they bring sophisticated machine learning methods closer to the public with intuitive graphical user interfaces and clear user instructions.  

The methods chosen for this seminar (DeepLabCut, VAME, Anipose) are rather selected due to practical experience within our research group and constitute only a very small selection out of the many methods coming out every few months. The paper below by Bohnslav et al., (2021) presenting DeepEthogram was chosen to show some crucial differences with the methods used in our *Hands on Tutorials*.

```{figure} content/deepethogram.png
---
width: 800px
name: deepethogram
---
Schematic of DeepEthogram pipeline, from Bohnslav et al., (2021).
```

Unlike **DeepLabCut**, DeepEthogram does not use tracking and skeleton-based action detection. In contrast, it uses the raw pixel data of video recordings to analyze the degree of motion, change, or flow, between frames, as well as spatial features of single images. These features are then used to classify actions, instead of body part tracking coordinates. 

Given the spatial and optical flow features extracted from raw videos, a training dataset needs to be manually classified with pre-defined behaviors of interest. This becomes a problem for research in which entire behavioral sequences are analyzed without prior expectations on specific behaviors of interest, e.g., in idle or waiting time during delayed response experiments. In contrast, supervised classification may be an advantage in situations in which very specific behaviors are investigated, such as different types of grooming, while ignoring the rest of the behavioral sequence. 

Furthermore, DeepEthogram is a self sufficient tool for behavior classification, while other methods need more or less pre- or post-processing steps. In contrast, **VAME** works with body part coordinates extracted with DeepLabCut, thus separating the tracking and classification into two distinct models. VAME for example is an unsupervised classification method (see bonus material) that segments and clusters time series tracking data based on statistical thresholds rather than pre-defined descriptions. These motifs need to be interpreted at a later stage to reach a sufficient level of description, but the time segmentation itself provides useful information on the variability or entropy of behavior.

**Important:** Note the separation of spatial and temporal features in {numref}`deepethogram`!  
DeepEthogram uses three different models to classify behavior. First, it extracts *optic flow features* from 11 frames. Then, it analyses *spatial features* from static frames. Lastly, it analyzes both sets of features on longer time sequence to include history and the future  to classify behavior for a given frame. 


## Literature
Bohnslav, J. P., Wimalasena, N. K., Clausing, K. J., Dai, Y. Y., Yarmolinsky, D. A., Cruz, T., Kashlan, A. D., Chiappe, M. E., Orefice, L. L., Woolf, C. J., & Harvey, C. D. (2021). DeepEthogram, a machine learning pipeline for supervised behavior classification from raw pixels. ELife, 10, e63377. https://doi.org/10.7554/eLife.63377

```{toggle}
<iframe width="800" height="500" src="Bohnslavetal.2021.pdf"></iframe>
```

## Bonus: Kevin Luxem (University of Magdeburg)

Unsupervised Quantification of Animal Behavior

<div><div style="left: 0; width: 100%; height: 0; position: relative; padding-bottom: 56.25%;"><figure style="left: 0; width: 100%; height: 0; position: relative; padding-bottom: 56.25%; margin-block-end: 0; margin-block-start: 0; margin-inline-start: 0; margin-inline-end: 0;" ><iframe src="https://media.publit.io/file/KevinLuxemUnsupervisedQuantification.html" scrolling="no" style="border: 0; top: 0; left: 0; width: 100%; height: 100%; position: absolute; overflow:hidden;" allowfullscreen=""></iframe></figure></div></div>
