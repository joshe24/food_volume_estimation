# Fast 3D Reconstruction of Food Surface and Volume Estimation

This repo includes the code for my diploma thesis.


## Abstract
The purpose of this diploma thesis is the implementation of a system capable of
computing food volume by capturing a short video from an arbitrary device that has
a digital camera. For this reason, food’s three dimensional surface is reconstructed.
Camera’s intrinsic and extrinsic parameters are estimated by using a specially designed
placemat, which is also used to detect the food in an image through a process that
was designed for this thesis. There are two different reconstruction methods presented,
one aiming to track the food pixels in consecutive frames while the other to estimate a
depth map. Finally, both methods are evaluated through a dataset of 28 different meals
with known volumes, by calculating the volume error and measuring the time needed for
volume estimation and camera calibration.

## How to use
First of all, print the placemat ('aruco_board.jpg') in A3 paper (29.7x42.0 cm).

The plate that will be used must be plain with no patterns or weird textures.

The placemat must remain fully visible around the plate while recording. For pixel tracking, record one video:

1. Move the camera slowly around the stationary food in a complete circle, keeping a roughly constant distance. Keep the placemat visible and the camera high enough to see its markers. Aim for about 15 seconds.
2. A separate video recorded directly above the plate is used only by the stereo-matching method. Move horizontally from left to right (preferably in landscape mode) for about 8 seconds.

## Run the code
Install dependencies from setup.py by typing

```bash
pip install -e .
```

To calculate the volume run the functions volume_with_pixel_tracking and volume_with_stereo_matching 
by passing the path to the first and second video respectively as parameters. 

```python
from volume_calculation import volume_with_stereo_matching, volume_with_pixel_tracking

measurement = volume_with_pixel_tracking('path_to_circular_video')
print(measurement['volume_ml'], measurement['dimensions_cm'])
volume2 = volume_with_stereo_matching('path_to_video_2')
```

The pixel-tracking result contains `volume_ml` and `dimensions_cm` in width, depth, and height order. The stereo-matching function retains its original volume-only result.

## Placemat
![](aruco_board.jpg)
