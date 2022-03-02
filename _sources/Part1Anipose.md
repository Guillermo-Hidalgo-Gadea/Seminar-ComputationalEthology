# 3D triangulation with Anipose

The good news is, we won't need to do anything in python this time. Anipose is nicely rounded up with a set of console commands to run the entire analysis pipeline without having to code anything ourselves.

<div style="overflow: auto; height:300pt; width:100%;">Terminal Output:

```console
(anipose) C:\Users\hidalggc>anipose
Usage: anipose [OPTIONS] COMMAND [ARGS]...

Options:
  --version      Show the version and exit.
  --config FILE  The config file to use instead of the default "config.toml" .
  --help         Show this message and exit.

Commands:
  analyze
  angles
  calibrate
  calibration-errors
  convert-videos
  draw-calibration
  extract-frames
  filter
  filter-3d
  label-2d
  label-2d-filter
  label-2d-proj
  label-3d
  label-3d-filter
  label-combined
  label-filter-compare
  project-2d
  run-all
  run-data
  run-viz
  summarize-2d
  summarize-2d-filter
  summarize-3d
  summarize-errors
  tracking-errors
  train-autoencoder
  triangulate
  visualizer
```

</div>

## Starting a new Project

Before we get started with Anipose, we will assume you already have behavioral video data recorded with multiple synchronized cameras. Furthermore, you will need to have a DeepLabCut model trained on this data or in some other way able to analyze your videos. For more information on how to synchronize multiple cameras refer to the anipose [website](https://anipose.readthedocs.io/en/latest/) as well as [syncFLIR](https://gitlab.ruhr-uni-bochum.de/ikn/syncflir) or [VideoPyToolbox](https://github.com/Guillermo-Hidalgo-Gadea/VideoPyToolbox).  
For this tutorial we will use facial expression data from [here](https://ruhr-uni-bochum.sciebo.de/s/v63Pwp8R9Ci5Ctd).

### Create a new project directory

When you create a new project, start by giving your folder a clear name. Descriptions such as `aniposeProject` will be meaningless if you have several 3D projects, and your project name may be not enough if you need to have separate directories for DeepLabCut and Anipose.

#### Before

Your new anipose project directory should look something like this:
<div style="overflow: auto; height:300pt; width:100%;">

```yaml
AniposeFacialExpression_20220112
├── config.toml
├── subject_1
│   └── calibration
│       └── Video1_calibration_camA.avi
│       └── Video1_calibration_camB.avi
│       └── Video1_calibration_camC.avi
│       └── [...]
│   └── videos-raw
│       └── Video1_recording_camA.avi
│       └── Video1_recording_camB.avi
│       └── Video1_recording_camC.avi
│       └── [...]
├── subject_2
│   └── calibration
│       └── Video2_calibration_camA.avi
│       └── Video2_calibration_camB.avi
│       └── Video2_calibration_camC.avi
│       └── [...]
│   └── videos-raw
│       └── Video2_recording_camA.avi
│       └── Video2_recording_camB.avi
│       └── Video2_recording_camC.avi
│       └── [...]
├── [...]
└── subject_n
```

</div>

#### After

After the analysis, new directories will be added to your project and the result of each analysis step can be found in the respective folder:
<div style="overflow: auto; height:300pt; width:100%;">

```yaml
AniposeFacialExpression_20220112
├── config.toml
├── subject_1
│   └── calibration
│       └── Video1_calibration_camA.avi
│       └── Video1_calibration_camB.avi
│       └── Video1_calibration_camC.avi
│       └── [...]
│       └── calibration.toml
│       └── detections.pickle
│   └── pose-2d
│       └── Video1_recording_camA.h5
│       └── Video1_recording_camA.pickle
│       └── [...]
│   └── pose-2d-filtered
│       └── Video1_recording_camA.h5
│       └── [...]
│   └── pose-3d
│       └── Video1_recording.csv
│   └── pose-3d-filtered
│       └── Video1_recording.csv
│   └── videos-3d
│       └── Video1_recording.mp4
│   └── videos-3d-filtered
│       └── Video1_recording.mp4
│   └── videos-labeled
│       └── Video1_recording_camA.mp4
│       └── Video1_recording_camB.mp4
│       └── Video1_recording_camC.mp4
│       └── [...]
│   └── videos-labeled-filtered
│       └── Video1_recording_camA.mp4
│       └── Video1_recording_camB.mp4
│       └── Video1_recording_camC.mp4
│       └── [...]
│   └── videos-raw
│       └── Video1_recording_camA.avi
│       └── Video1_recording_camB.avi
│       └── Video1_recording_camC.avi
│       └── [...]
└── subject_n
```

</div>
  
### Edit the config.toml file

Unfortunately Anipose does not create a template configuration file, and you will need to create the `config.toml` file yourself, while taking into account the intended structure and and parameters. I recommend using the same configuration file from a previous project and editing the respective parts. Specifically the `model_folder`, as well as `[labeling]` and `[triangulation]` parameters.

<div style="overflow: auto; height:300pt; width:100%;"> config.toml file:

```toml
project = 'FacialExpression_20210414'

model_folder = 'D:\3DBHVR\FacialExpression_20210414\DLC-Guillermo-2021-04-14' 

nesting = 1
video_extension = 'avi'

[calibration]
# checkerboard / charuco / aruco
board_type = "charuco"

# width and height of grid
board_size = [10, 7]

# number of bits in the markers, if aruco/charuco
board_marker_bits = 4

# number of markers in dictionary, if aruco/charuco
board_marker_dict_number = 50

# length of marker side
board_marker_length = 31 # mm

# If charuco or checkerboard, square side length
board_square_side_length = 41 # mm

animal_calibration = false

fisheye = false # depends on the zoom level...

[manual_verification]
# true / false
manually_verify = false

[labeling]
scheme = [
   ["lefteye1", "lefteye3", "lefteye2", "lefteye4", "lefteye1"], ["righteye1", "righteye3", "righteye2", "righteye4", "righteye1"],
   ["nose1", "nose3", "nose2","nose4",  "nose1", "nose2"],
   ["lefteyebrow1", "lefteyebrow2", "lefteyebrow3"],["righteyebrow1", "righteyebrow2", "righteyebrow3"],
   ["mouth1", "mouth3", "mouth2", "mouth4", "mouth1"],
   ["leftear", "chin", "rightear"] 
 ]

[filter]
enabled = true
medfilt = 13 # length of median filter
offset_threshold = 25 # offset from median filter to count as jump
score_threshold = 0.4 # score below which to count as bad
spline = true # interpolate using cubic spline instead of linear

[triangulation]
triangulate = true
cam_regex = 'cam-([A-Z])$'
optim = true
constraints = [  # set of constant limb length constraints written out as pairs
   ["leftear", "rightear"]]
axes = [ #An axis is specified as a pair of points, with the axis going from the first to the second point.
    ["z", "chin", "nose1"],
    ["x", "rightear", "chin"]]

reference_point = "chin" # Furthermore, it is often useful to set the zero to a standard reference point. Anipose allows this too.

scale_smooth = 50 # strength of smoothness constraint, higher gives smoother trajectory
scale_length = 50 # strength of length constraint, higher enforces less variability in limb lengths
reproj_error_threshold = 5 # in pixels, for robust triangulation
score_threshold = 0.6 # score threshold for triangulation
n_deriv_smooth = 2 # derivative to minimize for smoothness
```

</div>

## Analyzing videos

Once the project directory and config.toml files are ready, you should proceed to analyze all your behavioral videos. Anipose will use the DeepLabCut model specified in `model_folder` to track 2D coordinates of all videos in the `videos-raw` directory of every subject. 

* use the terminal command: `anipose analyze`

## 3D Triangulation

To move from 2D labeled videos to a full 3D reconstruction you will need to triangulate each coordinate from all the different camera angles.

### Calibrating cameras

First calibrate your cameras with the calibration videos in `calibration`. Make sure to have identical labels for each video recording with a distinctive `cam_regex`such as `_cam[A-Z]`. Only calibration videos with the same name will be considered for each calibration.  
If camera calibration is successful, proceed to filtering and triangulation.

* use the terminal command: `anipose calibrate`

### Filter tracking errors

Anipose provides a set of different filters to correct for tracking errors from DeepBalCut. The filtered data show smoother results and is often easier to interpret. You can filter the original 2D tracked coordinates as well as the final 3D triangulated coordinates

* use the terminal command: `anipose filter` and `anipose filter-3d`

### Triangulate coordinates

Once cameras are calibrated and videos are analyzed, you can proceed to triangulate the 2D coordinates in three dimensions.

* use the terminal command: `anipose triangulate`

## Visualize tracking in 2D and 3D

After analysis and triangulation it is necessary to visualize the labeling and filtering results to inspect the tracking accuracy both of the 2D videos and of the final 3D model. You could run each step separately (i.e., `label-2d`, `label-2d-filter`, etc.) or use the `run-viz` command to run all the visualizations at once.

* use the terminal command: `anipose run-viz`
