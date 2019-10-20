import glob
import numpy as np
from skimage import *
from skimage.transform import resize
import imageio
import os

#file1 = open('brain_us_img_ids.txt','w+')

location = '/media/jeyamariajose/7888230b-5c10-4229-90f2-c78bdae9c5de/Data/Brain_Ultrasound/unet_syn/train/label/*.png'
save_loc = '/media/jeyamariajose/7888230b-5c10-4229-90f2-c78bdae9c5de/Data/Brain_Ultrasound/unet_syn/train/img/'

count = 0
for filename in glob.iglob(location):
	img = io.imread(filename)

	if img.shape[0]!=512:
		count = count+1
		#print(filename[101 :])
		#break
		os.remove(filename)
		os.remove((save_loc+filename[101 :])[: -3]+"jpg")

	#file1.write(filename[64 :])
	

