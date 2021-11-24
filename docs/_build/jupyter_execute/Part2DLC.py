#!/usr/bin/env python
# coding: utf-8

# # Part 2: Edit an existing DeepLabCut Project

# Note: Open this jupyter notebook in your DeepLabCut environment.

# ## Load existing DeepLabCut Models

# Import python libraries needed for this notebook

# In[ ]:


try:
    import deeplabcut
    import tkinter
    from tkinter import filedialog

    print(f'Using DeepLabCut version: {deeplabcut. __version__}')

except:
    print("Please run the notebook in in your local environment")


# Load existing model by selecting the corresponding config.yaml file:

# In[ ]:


config_path = filedialog.askopenfilename(title='Choose the config.yaml file of your DeepLabCut project:')

print(f'Using project path: {config_path}')


# Load new videos to analyze and/or merge to the project:

# In[ ]:


video_files = filedialog.askopenfilenames(title='Choose new video files to analyze in DeepLabCut:')
new_videos = list(video_files)

print(f'{len(new_videos)} videos selected:')
for i in range(len(new_videos)): 
    print(new_videos[i])


# ## Analyze new videos with the previously trained model

# The analysis results in this step will most probably not look as desired, but this is to be expected. Bare in mind, that we are trying to analyze new, unseen videos with a model trained on different data (i.e., either other individuals, other sessions and maybe even different light conditions or camera angles). The goal of this step is to find out where the model fails to generalize and cover this shortcomings.

# In[ ]:


deeplabcut.analyze_videos(config_path, new_videos, shuffle=1, save_as_csv=True, videotype='mp4' )


# In[ ]:


deeplabcut.filterpredictions(config_path, new_videos, shuffle=1, save_as_csv=True, videotype='mp4')


# In[ ]:


deeplabcut.create_labeled_video(config_path, new_videos, filtered=True, videotype = 'mp4', save_frames=False)


# ## Extract outlier frames

# Now this is the interesting part. Instead of including more videos to the project directly, and extracting frames as usual with kmeans, we are taking advantage of the previous model to tell us what frames exactly to label. This active learning step helps us recognize the shortcomings of our model and correct it in a targeted manner.

# In[ ]:


deeplabcut.extract_outlier_frames(config_path, new_videos, automatic=True)


# Now that we have extracted new frames, we need to go back and start labeling. Instead of starting from the beginning, though, we are provided the model predictions and have to drag and drop them in place. **Note:** Make sure to remove labels that are not visible, the model will often guess the expected position based on learned geometric constraints. 

# In[ ]:


deeplabcut.refine_labels(config_path)


# You can again plot your labeled frames to check annotation accuracy.

# In[ ]:


deeplabcut.check_labels(config_path)


# At this point you could get an error message like [this](https://github.com/DeepLabCut/DeepLabCut/issues/232) telling you that saving the video path failed. In this case, you need to add the new video paths manually for DLC to include these in the new training set. You can either add them by hand, writing in the config.yaml file in the same format as the first video paths (see [here](https://github.com/DeepLabCut/DeepLabCut/issues/663#issuecomment-619274975)), or you can run the following command to add the list of videos to your config file:

# In[ ]:


deeplabcut.add_new_videos(config_path, new_videos, copy_videos=False)


# If the permission error persists, try starting a new anaconda terminal as administrator (right click > run as administrator) and then starting jupyter notebook with elevated privileges.

# ## Merge Datasets

# After refining all outlier frames extracted above, merge the datasets to combine old and new labels in your project. 

# In[ ]:


deeplabcut.merge_datasets(config_path)


# In[ ]:


deeplabcut.create_training_dataset(config_path, net_type='resnet_50', augmenter_type='imgaug')


# **Note:** Make sure that the new videos have been included in the config.yaml file without permission issues (see above).

# ## Re-Train Network

# When training a new model with an expanded dataset, you could either choose to start fresh with new data, or use the previous model as pre-trained network for your next model. Although not yet extensively verified, lets belief that transfer learning at least won't harm the new model. 

# In[ ]:


pose_cfg =  filedialog.askopenfilename(title='Choose DeepLabCut pose_cfg.yaml file from dlc-models:')
import webbrowser
webbrowser.open(pose_cfg)
print('Please edit init_weights to include the path to the last pre-trained model...')


# In[ ]:


# Example of own pre-trained model
init_weights: D:\FacialExpression\old-DLC-Project\dlc-models\iteration-0\DLCApr14-trainset95shuffle1\train\snapshot-1030000


# In[ ]:



deeplabcut.train_network(config_path, shuffle=1, displayiters=100, saveiters=1000)


# ## Analyze your new model starting with Part 1

# In[ ]:


videolist = ...
config_path = ...


# In[ ]:


deeplabcut.analyze_videos(config_path, videolist, shuffle=1, save_as_csv=True, videotype='mp4' )


# In[ ]:


deeplabcut.filterpredictions(config_path,videolist, videotype='.mp4',filtertype= 'arima',ARdegree=5,MAdegree=2)


# In[ ]:


deeplabcut.create_labeled_video(config_path, videolist, videotype='.mp4', filtered=False, trailpoints=10, draw_skeleton = True)


# ...
