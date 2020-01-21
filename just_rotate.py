import glob
import numpy as np
from skimage import *
from skimage.transform import resize
import imageio
import os
import cv2
from scipy import ndimage, misc

#file1 = open('brain_us_img_ids.txt','w+')

location = '/home/jeyamariajose/Projects/Overcomplete-Autoencoder/Segmentation/resized/shoes_oc_ae/95/*.jpg'
save_loc = '/media/jeyamariajose/7888230b-5c10-4229-90f2-c78bdae9c5de/Data/night2day/train/'
# location2 = '/media/jeyamariajose/7888230b-5c10-4229-90f2-c78bdae9c5de/Data/Brain_Ultrasound/Final/unet/test/img2/'

count = 0

for filename in glob.iglob(location):

	image = cv2.imread(filename)
	print(image.shape)
	# image =  np.rot90(image,3)
	image = np.flip(image,1)

	cv2.imwrite(filename,image)