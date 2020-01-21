import glob
import numpy as np
from skimage import *
from skimage.transform import resize
import imageio
import os
import cv2
import torch

#file1 = open('brain_us_img_ids.txt','w+')

location = '/media/jeyamariajose/7888230b-5c10-4229-90f2-c78bdae9c5de/Data/Brain_Ultrasound/Final/resized/train/img/*.png'
save_loc = '/media/jeyamariajose/7888230b-5c10-4229-90f2-c78bdae9c5de/Data/Brain_Ultrasound/Final/noisy/train/img/'

count = 0

def add_noise(img):

    noise = torch.randn(img.size()) * 50
    noisy_img = img + noise
    return noisy_img


for filename in glob.iglob(location):

	image = cv2.imread(filename,0)
	tmp = filename[-8 :]
	row,col= image.shape
	# mean = 0
	# var = 1
	# sigma = var**2
	# gauss = np.random.normal(mean,sigma,(row,col))
	# gauss = gauss.reshape(row,col)
	# noisy = image + gauss

	noisy = add_noise(torch.tensor(image))
	noisy = noisy.cpu().numpy()

	cv2.imwrite(save_loc+tmp,noisy)