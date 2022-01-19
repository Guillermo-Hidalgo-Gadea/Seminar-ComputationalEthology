# Hands on Tutorials

During the seminar you will get a first impression on how to work with methods for computational ethology such as  [DeepLabCut](https://github.com/DeepLabCut/DeepLabCut) to track body parts, [Anipose](https://github.com/lambdaloop/anipose) to triangulate coordinated, and [VAME](https://github.com/LINCellularNeuroscience/VAME) to classify behavior motifs.  
These methods are **not always easy** to use, and sometimes require a little programming with Python and basic understanding of machine learning and data science. Your goal should be to understand the value of these tools for computational ethology and try to get your hands dirty with a little code.

:::{note}
The following tutorials were created as user friendly as possible, but feel free to approach the lecturer with any questions or use the **Suggestion Box** to give feedback.
:::


## [DeepLabCut](DemoDeepLabCut.md)
DeepLabCut is a toolbox for markerless pose estimation of animals performing various tasks. DeepLabCut is an open source package for markerless pose estimation based on transfer learning with deep neural networks ([Mathis et al., 2018](https://www.nature.com/articles/s41593-018-0209-y)). It uses algorithms from [DeeperCut](https://link.springer.com/chapter/10.1007/978-3-319-46466-4_3), and an extremely deep neural network pre-trained on a dataset for object detection ([ImageNet](https://openaccess.thecvf.com/content_cvpr_2016/html/He_Deep_Residual_Learning_CVPR_2016_paper.html)). DeepLabCut was originally developed for animal pose estimation, which does not exclude humans, see [Namba et al. (2021)](https://www.nature.com/articles/s41598-021-83077-4), and can also be used to track inanimate objects.

## [Anipose](DemoAnipose.md)
Anipose is an open-source Python toolkit for robust, markerless 3D pose estimation of animal behavior from multiple camera views. Anipose is built on DeepLabCut for markerless tracking, and can be used to expand existing 2D projects with multiple cameras. It consists of a 3D camera calibration module, triangulation of 2D tracked coordinates, and a set of filters to resolve tracking errors both in 2D and 3D models. Synchronized cameras are needed to record behavior from multiple views, and calibration boards such as [ChArUco](https://docs.opencv.org/3.4/df/d4a/tutorial_charuco_detection.html) are used to calculate camera parameters such as relative position and orientation in space. 

## [VAME](DemoVAME.md)
VAME is a framework to cluster behavioral signals obtained from pose-estimation tools with unsupervised machine learning. Variational Animal Motion Embedding (VAME) is a probabilistic machine learning framework developed by Luxem et al., 2022 for discovery of the latent structure of animal behavior given an input time series obtained from markerless pose estimation tools. It is a PyTorch based deep learning framework which leverages the power of recurrent neural networks (RNN) to model sequential data. In order to learn the underlying complex data distribution we use the RNN in a variational autoencoder setting to extract the latent state of the animal in every step of the input time series.

## Literature
Karashchuk, P., Rupp, K. L., Dickinson, E. S., Walling-Bell, S., Sanders, E., Azim, E., Brunton, B. W., & Tuthill, J. C. (2021). Anipose: A toolkit for robust markerless 3D pose estimation. Cell Reports, 36(13), 109730. https://doi.org/10.1016/j.celrep.2021.109730

```{toggle}
<iframe width="800" height="500" src="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8498918/pdf/nihms-1744538.pdf"></iframe>
```

Luxem, K., Mocellin, P., Fuhrmann, F., Kürsch, J., Remy, S., & Bauer, P. (2022). Identifying Behavioral Structure from Deep Variational Embeddings of Animal Motion. https://doi.org/10.1101/2020.05.14.095430

```{toggle}
<iframe width="800" height="500" src="https://www.biorxiv.org/content/10.1101/2020.05.14.095430v3.full.pdf"></iframe>
```

Mathis, A., Mamidanna, P., Cury, K. M., Abe, T., Murthy, V. N., Mathis, M. W., & Bethge, M. (2018). DeepLabCut: Markerless pose estimation of user-defined body parts with deep learning. Nature Neuroscience, 21(9), 1281–1289. https://doi.org/10.1038/s41593-018-0209-y

```{toggle}
<iframe width="800" height="500" src="https://sci-hub.mksa.top/10.1038/s41593-018-0209-y"></iframe>
```

Nath, T., Mathis, A., Chen, A. C., Patel, A., Bethge, M., & Mathis, M. W. (2019). Using DeepLabCut for 3D markerless pose estimation across species and behaviors. Nature Protocols, 14(7), 2152–2176. https://doi.org/10.1038/s41596-019-0176-0

```{toggle}
<iframe width="800" height="500" src="https://sci-hub.mksa.top/10.1038/s41596-019-0176-0"></iframe>
```