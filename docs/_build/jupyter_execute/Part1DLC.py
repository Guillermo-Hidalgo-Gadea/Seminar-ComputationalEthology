#!/usr/bin/env python
# coding: utf-8

# # Part 1: Create a DeepLabCut Project

# Note: Open this jupyter notebook in your DeepLabCut environment.

# ## Create new Project

# Import python libraries needed for this notebook

# In[1]:


try:
    import deeplabcut
    import tensorflow
    import tkinter
    from tkinter import filedialog

    print(f'Using DeepLabCut version: {deeplabcut. __version__}')
    print(f'Using TensorFlow version: {tensorflow. __version__}')   

except:
    print("Please run the notebook in in your local environment")


# Start by selecting the list of videos to be included in the model. You could manually type the full path of each video in a python list as argument of the deeplabcut.create_new_project() function, like so:

# In[2]:


['C:\\Users\\computername\\Videos\\reachingvideo1.avi', 
 'C:\\Users\\computername\\Videos\\reachingvideo2.avi', 
 'C:\\Users\\computername\\Videos\\reachingvideo3.avi']


# :::{note}
# Windows users need to use the double backslash for path directories or a python raw filestring.
# :::

# Instead, we use ```tkinter``` to open a file dialoge and save the file paths in a python list called ```videolist```: 

# In[3]:


video_files = filedialog.askopenfilenames(title='Choose new video files to analyze in DeepLabCut:')
videolist = list(video_files)

print(f'{len(videolist)} videos selected:')
for i in range(len(videolist)): 
    print(videolist[i])


# Now we create a new project using the video paths in ```videolist```, give the project a name and set a few parameters:

# In[ ]:


config_path = deeplabcut.create_new_project('Name of project', 'Name of Experimenter', videolist, working_directory='path working directory', copy_videos=True, multianimal=False)


# :::{note}
# You can load existing DeepLabCut projects by specifying the config_path as below:
# :::

# In[ ]:


config_path = filedialog.askopenfilename(title='Choose DeepLabCut config.yaml file:')


# ## Configure Project

# Now that a new project has been created with a specific directory structure and configuration file, we need to tweak some parameters to tailor the bodyparts we want to track:

# In[ ]:


import webbrowser
webbrowser.open(config_path)
print('Please edit bodyparts list to be tracked')


# Once happy with all ```bodyparts```, ```skeleton:``` and ```numframes2pick:``` settings, start extracting frames to label:
# 

# In[ ]:


deeplabcut.extract_frames(config_path, mode='automatic', algo='kmeans', userfeedback=False, crop=False)


# ## Label Frames

# In[ ]:


deeplabcut.label_frames(config_path)


# You can plot your labeled frames to check your annotation accuracy.

# In[ ]:


deeplabcut.check_labels(config_path)


# ## Train Model

# In[ ]:


deeplabcut.create_training_dataset(config_path, num_shuffles=1, net_type='resnet_50', augmenter_type='imgaug')


# In[ ]:


deeplabcut.train_network(config_path, shuffle=1, trainingsetindex=0, max_snapshots_to_keep=5, displayiters=200, saveiters=20000, maxiters=1030000, allow_growth=True)


# ## Evaluate Model

# In[ ]:


deeplabcut.evaluate_network(config_path,Shuffles=[1], plotting=True)


# ## Analyze Videos

# In[ ]:


deeplabcut.analyze_videos(config_path, videolist, shuffle=1, save_as_csv=True, videotype='mp4' )


# In[ ]:


deeplabcut.filterpredictions(config_path,videolist, videotype='.mp4',filtertype= 'arima',ARdegree=5,MAdegree=2)


# In[ ]:


deeplabcut.analyzeskeleton(config_path, videolist, videotype='.mp4', shuffle=1, trainingsetindex=0, save_as_csv=False, destfolder=None)


# ## Create labeled videos

# In[ ]:


deeplabcut.create_labeled_video(config_path, videolist, videotype='.mp4', filtered=False, trailpoints=10, draw_skeleton = True)


# In[ ]:


deeplabcut.create_labeled_video(config_path, videolist, videotype='.mp4', filtered=True, trailpoints=10, draw_skeleton = True, keypoints_only=True)


# In[ ]:


deeplabcut.plot_trajectories(config_path, videolist)

