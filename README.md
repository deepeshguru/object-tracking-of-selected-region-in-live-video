# Object-tracking-of-selected-region-in-live-video 

In this project we can track interested object in live video or in saved video using opencv and python.


Hi, everyone this is the easiest way to track any object in live video or saved video. In this we first calculated histogram and back projection of selected region.
After that we apply meanshift algorithm.

## Necessary software
python and opencv

## How to run
Run code in python then live video window open, for track something in this video press 'b' and select that region and press enter after that press 'c' for track that region and press 'q' for quit.

If you want to run code with saved video. So you store video in same directory where code is store. And you have to do slight change in code replace 0 with 'filename' in line 10.

### References
https://docs.opencv.org/3.4/db/df8/tutorial_py_meanshift.html
https://docs.opencv.org/3.4/df/d9d/tutorial_py_colorspaces.html
https://docs.opencv.org/3.4/df/d9d/tutorial_py_colorspaces.html
