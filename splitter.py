import tifffile as tf
import numpy as np
import os
import sys
import cv2
import glob


def save_image(image, name):
    #this function is responsible to save the image
    #image is the image to be saved
    #name is the name of the image
    #size is the size of the image
    print("saving image")
    tf.imsave(name, image)


def split_image(image, size):
    #this function is responsible to split the image into smaller images
    #image is the image to be split
    image = tf.imread(image)
    print(image.shape)
    path = "./OutputFold"
    if not os.path.exists(path):
        os.makedirs(path)

        for i in range(0, image.shape[0], size):
            for j in range(0, image.shape[1], size):
                if(i+size <= image.shape[0] and j+size <= image.shape[1]):
                    save_image(image[i:i+size, j:j+size], path + "/" + str(i) + "_" + str(j) + ".tif")
                    print("image saved")

