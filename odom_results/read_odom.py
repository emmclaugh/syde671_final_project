import csv
import numpy as np
import matplotlib.pyplot as plt
import math


def generate_scale(to_traj, from_traj):
    num_rows1,_ = to_traj.shape
    num_rows2,_ = from_traj.shape
    num_rows = np.minimum(num_rows1,num_rows2)
    scale = np.divide(to_traj[0:num_rows,:],from_traj[0:num_rows,:]+0.000001)
    scale.flatten()
    scale = np.median(scale)

    return scale

if __name__ == '__main__':
    ## reading in files
    ground_truth_reader = csv.reader(open("09_odom_ground_truth.txt"), delimiter=" ")
    ground_truth = np.asarray([[float(value) for value in row] for row in ground_truth_reader])

    retrained_reader = csv.reader(open("paper_results.txt"), delimiter=" ")
    retrained = np.asarray([[float(value) for value in row] for row in retrained_reader])

    before_retrain_reader = csv.reader(open("d1_odometry_09-image_2.txt"), delimiter=" ")
    before_retrain = np.asarray([[float(value) for value in row] for row in before_retrain_reader])

    # downscale odom
    num_rows,_ = ground_truth.shape
    num_rows1,_ = retrained.shape
    num_rows2,_ = before_retrain.shape
    sampling_rate1 = round(num_rows / num_rows1)
    sampling_rate2 = round(num_rows / num_rows2)
    ind = range(0,num_rows,sampling_rate1)
    ground_truth1 = ground_truth[ind,:]
    ind = range(0,num_rows,sampling_rate2)
    ground_truth2 = ground_truth[ind,:]

    scale1 = generate_scale(ground_truth1, retrained)
    scale2 = generate_scale(ground_truth2, before_retrain)

    retrained = retrained * scale1
    before_retrain = before_retrain * scale2

    ## plotting
    # show on the same plot
    plt.figure()
    plt.plot(ground_truth[:,0],ground_truth[:,2],'--b',
             retrained[:,0],retrained[:,2],'-r',
             before_retrain[:,0],before_retrain[:,2],'--g')
    plt.title("Kitti Sequence 09 Trajectory")
    plt.legend(['Ground Truth','Results from Paper','Our Results'])
    plt.show()