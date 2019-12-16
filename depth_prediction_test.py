from matplotlib import pyplot as plt
import cv2 # used for resize. if you dont have it, use anything else
import numpy as np
import tensorflow as tf
import sys
from PIL import Image

from depth_from_video_in_the_wild import depth_prediction_net
from depth_from_video_in_the_wild import model

if __name__ == '__main__':
    # Load images
    img = np.array(Image.open("data_example/erfurt_93/0000000002.png"))
    img1 = img[:,:416]
    img1 = np.expand_dims(img1,axis=0)

    # img1 = cv2.resize(img1, (416,128))
    # img1 = np.expand_dims(img1,axis=0)
    ### DEPTH

    inference_model = model.Model(
        is_training=False,
        batch_size=1,
        img_height=128,
        img_width=416)
    saver = tf.train.Saver()
    sess = tf.Session()

    saver.restore(sess, "example_model/model-413174")
    d1 = inference_model.inference_depth(img1, sess)
    d1 = np.squeeze(d1)

    # saver.restore(sess, "my_CP_archive/delta_2/model-415998")
    # d2 = inference_model.inference_depth(img1, sess)
    # d2 = np.squeeze(d2)

    # saver.restore(sess, "my_CP_archive/delta_3/model-416856")
    # d3 = inference_model.inference_depth(img1, sess)
    # d3 = np.squeeze(d3)

    # saver.restore(sess, "my_CP_archive/delta_4/model-413756")
    # d4 = inference_model.inference_depth(img1, sess)
    # d4 = np.squeeze(d4)

    # saver.restore(sess, "my_CP_archive/delta_5/model-413249")
    # d5 = inference_model.inference_depth(img1, sess)
    # d5 = np.squeeze(d5)

    plt.subplot(2,1,1)
    font = {'family' : 'normal',
            'size'   : 22}

    plt.rc('font', **font)
    plt.imshow(np.squeeze(img1))
    plt.axis('off')
    plt.title('Original Image')
    plt.subplot(2,1,2)
    plt.imshow(d1, cmap='gray',vmin=np.min(d1), vmax=np.max(d1))
    plt.axis('off')
    plt.title('Depth Estimation')
    # plt.subplot(6,1,3)
    # plt.imshow(d2, cmap='gray',vmin=np.min(d2), vmax=np.max(d2))
    # plt.axis('off')
    # plt.title('d=2')
    # plt.subplot(6,1,4)
    # plt.imshow(d3, cmap='gray',vmin=np.min(d3), vmax=np.max(d3))
    # plt.axis('off')
    # plt.title('d=3')
    # plt.subplot(6,1,5)
    # plt.imshow(d4, cmap='gray',vmin=np.min(d4), vmax=np.max(d4))
    # plt.axis('off')
    # plt.title('d=4')
    # plt.subplot(6,1,6)
    # plt.imshow(d5, cmap='gray',vmin=np.min(d5), vmax=np.max(d5))
    # plt.axis('off')
    # plt.title('d=5')
    plt.show()