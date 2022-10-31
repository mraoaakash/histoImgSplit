import tifffile as tf
import numpy as np
import os
import sys
import cv2
import glob


def validate_image(image_path, size):
    #this function is responsible to validate the image
    #image_path is the image to be validated
    #size is the size of the image
    image = tf.imread(image_path)
    image_name = os.path.basename(image_path).split("_")
    image_name = image_name[len(image_name)-1].split(".")
    image_name = image_name[0]
    print(image.shape)
    if(image.shape[0] % size == 0 and image.shape[1] % size == 0):
        return True
    else:
        return False