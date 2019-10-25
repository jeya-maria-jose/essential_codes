import glob
import numpy as np
from skimage import *
from skimage.transform import resize
import imageio
import os
import cv2

#file1 = open('brain_us_img_ids.txt','w+')

location = '/media/jeyamariajose/7888230b-5c10-4229-90f2-c78bdae9c5de/Data/Brain_Ultrasound/unet_small_syn/train/label/*.png'
save_loc = '/media/jeyamariajose/7888230b-5c10-4229-90f2-c78bdae9c5de/Data/Brain_Ultrasound/unet_small_syn/train/img/'

count = 0
for filename in glob.iglob(location):
	img = io.imread(filename,as_gray =True)

	#ret,thresh = cv2.threshold(img,127,255,0)
	image, contours, hierarchy = cv2.findContours(img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	img = cv2.drawContours(img, contours, -1, (0,255,0), 3)

	 
	numcont = len(contours)

	if numcont==0:
		count = count+1
		print(filename[-8 :])
		#break
		
		os.remove(filename)
		os.remove((save_loc+filename[-8 :]))

	#file1.write(filename[64 :])
	
#print(count)
