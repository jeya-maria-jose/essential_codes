from skimage.metrics import structural_similarity as ssim

import glob
import numpy as np
from skimage import *
from skimage.transform import resize
import imageio
import os
import cv2
#import io

#file1 = open('brain_us_img_ids.txt','w+')
# location = '/home/jeyamariajose/Baselines/pytorch-CycleGAN-and-pix2pix/results/real/*.png'
# save_loc = '/home/jeyamariajose/Baselines/pytorch-CycleGAN-and-pix2pix/results/syn/'

location = '/home/jeyamariajose/Projects/Self_Attention_Aux_Synthesis/results/trainastest/final/real/*.png'
save_loc = '/home/jeyamariajose/Projects/Self_Attention_Aux_Synthesis/results/trainastest/final/syn/'
# location2 = '/media/jeyamariajose/7888230b-5c10-4229-90f2-c78bdae9c5de/Data/Brain_Ultrasound/Final/unet/test/img2/'

# location = '/home/jeyamariajose/Baselines/pix2pixHD/results/final/real/*.png'
# save_loc = '/home/jeyamariajose/Baselines/pix2pixHD/results/final/syn/'


tot=0
count = 0

for filename in glob.iglob(location):

	img = cv2.imread(filename,0)
	img2 = cv2.imread(save_loc+filename[-8:],0)

	tot = tot + ssim(img,img2)

	count+=1

	#print(filename[61:65])

print(tot/count)