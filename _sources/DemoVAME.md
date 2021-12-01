# Introduction to VAME

VAME is a framework to cluster behavioral signals obtained from pose-estimation tools.

**Documentation:** https://github.com/LINCellularNeuroscience/VAME/wiki  
**Sourcecode:** https://github.com/LINCellularNeuroscience/VAME/

Variational Animal Motion Embedding (VAME) is a probabilistic machine learning framework for discovery of the latent structure
of animal behavior given an input time series obtained from markerless pose estimation tools. It is a PyTorch based deep learning framework which leverages the power of recurrent neural networks (RNN) to model sequential data. In order to learn the underlying complex data distribution we use the RNN in a variational autoencoder setting to extract the latent state of the animal in every step of the input time series.


```{figure} content/vame.png
---
width: 800px
name: vame
---
Architecture of machine learning model in VAME, from Luxem et al., 2020.
```

## Installation

Unfortunately, you will need a GPU to install and run VAME locally on your computer. If that is the case, and you have Anaconda already installed, follow the steps below: 

1. `git clone https://github.com/LINCellularNeuroscience/VAME.git`

2. `cd VAME`

3. `conda env create -f VAME.yaml`

4. `python setup.py install`

5. install PyTorch from here: https://pytorch.org/get-started/locally/

If you have no access to a local GPU, you can always use cloud computing solutions (e.g., Google Colab) to run a test project on a virtual GPU. See Part 2 of todays tutorial to run VAME on Colab.

## Documentation

Luxem, K., Fuhrmann, F., Kürsch, J., Remy, S., & Bauer, P. (2020). Identifying Behavioral Structure from Deep Variational Embeddings of Animal Motion. https://doi.org/10.1101/2020.05.14.095430


<iframe width="800" height="500" src="https://www.biorxiv.org/content/10.1101/2020.05.14.095430v2.full.pdf"></iframe>
