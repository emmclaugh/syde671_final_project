from matplotlib import pyplot as plt
import cv2 # used for resize. if you dont have it, use anything else
import numpy as np
import tensorflow as tf
import sys
from PIL import Image

from depth_from_video_in_the_wild import depth_prediction_net
from depth_from_video_in_the_wild import model

if __name__ == "__main__":
    # Load images
    img = np.asarray(Image.open("depth_from_video_in_the_wild/data_example/erfurt_93/0000000002.png"))
    img1 = img[:,:416]
    img1 = np.expand_dims(img1,axis=0)
    img2 = img[:,416:832]
    img2 = np.expand_dims(img2,axis=0)

    inference_model = model.Model(
        is_training=False,
        batch_size=1,
        img_height=128,
        img_width=416)
    saver = tf.train.Saver()
    sess = tf.Session()
    saver.restore(sess, "example_model/model-413174")

    test = inference_model.inference_egomotion(img1, img2, sess)
    print(test)