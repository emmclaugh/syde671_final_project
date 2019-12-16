## SYDE 671 Final Project

This repository contains the code used by group 8 to test the robustness of the [depth from videos in the wild](https://github.com/google-research/google-research/tree/master/depth_from_video_in_the_wild) paper. Note that the depth from videos in the wild code is not included in the repository.

The first step to use this code is to run:
git clone https://github.com/robot-love/depth_from_video_in_the_wild.git

### mask_generation 
This folder contains Nick's code (`annotator.m`) to generate possibly moving object masks

### odom_results
This folder contains example odometry results. The python code `read_odom.py` can be run to view the group's replication of the results of the original paper.

### optical_flow_testing
This folder contains code for testing the limitations of optical flow. That is, how many frames can be skipped until optical flow breaks down.

### struct2depth
This folder contains code from the [struct2depth](https://github.com/tensorflow/models/tree/master/research/struct2depth) repository for generating training data from the kitti raw dataset. The code in this folder was augmented by group 8 to allow for skipping a specific number of frames.

### `depth_prediction_test.py` and `transfrom_prediciton_test.py`
These two python scripts are set up to be run to inference the depth estimation and odometry estimation networks on a single example. To run code in this repo, first be sure that the depth from videos in the wild repository has been cloned. Then download the following data into the example_model directory:
[Example Model](https://www.googleapis.com/download/storage/v1/b/gresearch/o/depth_from_video_in_the_wild%2Fcheckpoints%2Fkitti_odometry_learned_intrinsics.zip?generation=1568245497722898&alt=media)
You can then inference depth or transformation on the data example provided.
