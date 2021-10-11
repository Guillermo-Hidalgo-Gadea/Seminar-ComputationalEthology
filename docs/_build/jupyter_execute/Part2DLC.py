#!/usr/bin/env python
# coding: utf-8

# # Part 2: Edit a DeepLabCut Project

# ## Editing DeepLabCut Models
# 

# In[1]:


try:
    import deeplabcut
    import tkinter
    from tkinter import filedialog

    print(f'Using DeepLabCut version: {deeplabcut. __version__}')

except:
    print("Please run the notebook in in your local environment")


# Load existing model by selecting the corresponding config.yaml file:

# In[2]:


config_path = filedialog.askopenfilename(title='Choose the config.yaml file of your DeepLabCut project:')

print(f'Using project path: {config_path}')


# Load new videos to analyze and or merge to the project:

# In[ ]:


video_files = filedialog.askopenfilenames(title='Choose new video files to analyze in DeepLabCut:')
new_videos = list(video_files)

print(f'{len(new_videos)} videos selected:')
for i in range(len(new_videos)): 
    print(new_videos[i])


# Analyze new videos with the previously trained model:

# In[ ]:


deeplabcut.analyze_videos(config_path, new_videos, shuffle=1, save_as_csv=True, videotype='mp4' )


# In[ ]:


deeplabcut.filterpredictions(config_path, new_videos, shuffle=1, save_as_csv=True, videotype='mp4')


# In[ ]:


deeplabcut.extract_outlier_frames(config_path, new_videos, automatic=True)


# In[ ]:


deeplabcut.create_labeled_video(config_path, new_videos, videotype = 'mp4', save_frames=False)


# In[ ]:





# In[ ]:





# In[ ]:


deeplabcut.refine_labels(config_path)


# In[ ]:





# In[ ]:


deeplabcut.merge_datasets(config_path)


# In[ ]:





# In[ ]:


deeplabcut.create_training_dataset(config_path, net_type='resnet_50', augmenter_type='imgaug')


# In[ ]:





# In[ ]:


# change init_weights to use a pre-trained model
deeplabcut.train_network(config_path, shuffle=1, displayiters=100, saveiters=1000)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




