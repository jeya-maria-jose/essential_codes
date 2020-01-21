import glob
import numpy as np
from skimage import *
from skimage.transform import resize
import imageio
import os
import cv2

#file1 = open('brain_us_img_ids.txt','w+')

location = '/home/jeyamariajose/Baselines/pytorch-CycleGAN-and-pix2pix/results/BrainUS-rerun/test_latest/images/*.png'
save_loc = '/home/jeyamariajose/Baselines/pytorch-CycleGAN-and-pix2pix/results/syn/'
location2 = '/media/jeyamariajose/7888230b-5c10-4229-90f2-c78bdae9c5de/Data/Brain_Ultrasound/Final/unet/test/img2/'


count = 0

for filename in glob.iglob(location):

	img = cv2.imread(filename)