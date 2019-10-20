import glob
import numpy as np
from skimage import *
from skimage.transform import resize
import imageio
import os
import random

pick = random.sample(range(115200), 10920)

#file1 = open('brain_us_img_ids.txt','w+')

location = '/media/jeyamariajose/7888230b-5c10-4229-90f2-c78bdae9c5de/Data/Brain_Ultrasound/unet_syn/train/label/'
location2 = '/media/jeyamariajose/7888230b-5c10-4229-90f2-c78bdae9c5de/Data/Brain_Ultrasound/unet_syn/train/img/'

save_loc = '/media/jeyamariajose/7888230b-5c10-4229-90f2-c78bdae9c5de/Data/Brain_Ultrasound/unet_syn_10/train/'

count = 0
for i in (pick):
	print(i)
	if os.path.exists(location2+"%d.jpg"%i):
		img = io.imread(location2+"%d.jpg"%i,as_gray=True)
		lab = io.imread(location+"%d.png"%i,as_gray=True)

		io.imsave(save_loc+"img/%d.png"%i,img)
		io.imsave(save_loc+"label/%d.png"%i,lab)
		
	#file1.write(filename[64 :])
	

