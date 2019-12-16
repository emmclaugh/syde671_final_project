""" Getting optical flow fields for training data.

    The mechanism by which the neural net related to this
    project performs odometry is based on optical flow. 
    As such, optical flow has certain requirements for travel
    limits, i.e. pixels have to move only slightly between
    frames.

"""

# ---------------------------------------------------------
# Imports

import cv2
import plotly
import skimage
import numpy as np

# ---------------------------------------------------------
# Variables

imagePaths = [
    'img/000315.png',
    'img/000316.png',
    'img/000317.png',
    'img/000318.png',
    'img/000319.png',
    'img/000320.png',
]

# ---------------------------------------------------------
# Classes


# ---------------------------------------------------------
# Functions


# ---------------------------------------------------------
# Main

def main():
    images = []

    for path in imagePaths:
        images.append(cv2.imread(path))


    # old_frame = images[0]
    # old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)

    hsv = np.zeros_like(images[0])
    hsv[...,1] = 255

    for i in range(len(images)):

        delta = 1

        try:
            prvs    = cv2.cvtColor(images[i], cv2.COLOR_BGR2GRAY)
            nxt     = cv2.cvtColor(images[i+delta],cv2.COLOR_BGR2GRAY)
        except:
            break

        flow    = cv2.calcOpticalFlowFarneback(prvs,nxt, None, 0.5, 3, 15, 3, 5, 1.2, 0)


        mag, ang = cv2.cartToPolar(flow[...,0], flow[...,1])
        hsv[...,0] = ang*180/np.pi/2
        hsv[...,2] = cv2.normalize(mag,None,0,255,cv2.NORM_MINMAX)
        rgb = cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)

        cv2.imshow('frame2',rgb)
        # k = cv2.waitKey(30) & 0xff
        # if k == 27:
        #     break
        # elif k == ord('s'):
        # cv2.imwrite(f'opticalfb_{i}.png',frame2)
        cv2.imwrite(f'opticalhsv_d{delta}_{i}.png',rgb)
        prvs = next

    cv2.destroyAllWindows()
    

if __name__ == "__main__":
    main()