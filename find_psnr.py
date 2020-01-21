from skimage.metrics import structural_similarity as ssim

import glob
import numpy as np
from skimage import *
from skimage.transform import resize
import imageio
import os
import cv2
import tensorflow as tf
#import io
import numpy
from skimage import io
import tensorflow as tf


def log10(x):
    numerator = tf.log(x)
    denominator = tf.log(tf.constant(10, dtype=numerator.dtype))
    return numerator / denominator


def psnr(im1, im2):
    img_arr1 = numpy.array(im1).astype('float32')
    img_arr2 = numpy.array(im2).astype('float32')
    mse = tf.reduce_mean(tf.squared_difference(img_arr1, img_arr2))
    psnr = tf.constant(255**2, dtype=tf.float32)/mse
    result = tf.constant(10, dtype=tf.float32)*log10(psnr)
    with tf.Session():
        result = result.eval()
    return result

#file1 = open('brain_us_img_ids.txt','w+')

location = '/media/jeyamariajose/7888230b-5c10-4229-90f2-c78bdae9c5de/Data/Brain_Ultrasound/Final/noisy/test/label/*.png'
save_loc = '/home/jeyamariajose/Projects/Overcomplete-Autoencoder/Segmentation/resized/deno_us_oc_ae/15/'

# location2 = '/media/jeyamariajose/7888230b-5c10-4229-90f2-c78bdae9c5de/Data/Brain_Ultrasound/Final/unet/test/img2/'
# location = '/home/jeyamariajose/Baselines/pix2pixHD/results/final/real/*.png'
# save_loc = '/home/jeyamariajose/Baselines/pix2pixHD/results/final/syn/'
# location = '/home/jeyamariajose/Baselines/pytorch-CycleGAN-and-pix2pix/results/real/*.png'
# save_loc = '/home/jeyamariajose/Baselines/pytorch-CycleGAN-and-pix2pix/results/syn/'

tot=0
count = 0
psnr1 = 0

for filename in glob.iglob(location):

	img = cv2.imread(filename)
	img2 = cv2.imread(save_loc+filename[-8:])

	# tot = tot + ssim(img,img2)

	count+=1

	# Read images from file.
	#im1 = tf.decode_png(filename)
	#im2 = tf.decode_png(save_loc+filename[-8:])
	# Compute PSNR over tf.uint8 Tensors.
	psnr1 = psnr1 + psnr(img,img2)
	#print(tf.image.psnr(img, img2, max_val=255))
	print(count)
	#tmp = tf.image.psnr(img, img2, max_val=255)
	#print(tf.print(tmp,[tmp]))
	#print(filename[61:65])

print(psnr1/count)

