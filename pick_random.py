import glob
import numpy as np
from skimage import *
from skimage.transform import resize
import imageio
import os
import random

pick = random.sample(range(1300), 1300)

#file1 = open('brain_us_img_ids.txt','w+')

# location = '/media/jeyamariajose/7888230b-5c10-4229-90f2-c78bdae9c5de/Data/Brain_Ultrasound/unet_syn/train/label/'
# location2 = '/media/jeyamariajose/7888230b-5c10-4229-90f2-c78bdae9c5de/Data/Brain_Ultrasound/unet_syn/train/img/'

# save_loc = '/media/jeyamariajose/7888230b-5c10-4229-90f2-c78bdae9c5de/Data/Brain_Ultrasound/unet_syn_1/train/'

location = '/media/jeyamariajose/7888230b-5c10-4229-90f2-c78bdae9c5de/Data/Brain_Ultrasound/unet/train/label/'
location2 = '/media/jeyamariajose/7888230b-5c10-4229-90f2-c78bdae9c5de/Data/Brain_Ultrasound/unet/train/img/'

save_loc = '/media/jeyamariajose/7888230b-5c10-4229-90f2-c78bdae9c5de/Data/Brain_Ultrasound/unet_check/train/'

count = 0
for i in (pick):
	i = str(i)
	i = i.zfill(4)
	# if os.path.exists(location2+"%d.jpg"%i):
	# 	img = io.imread(location2+"%d.jpg"%i,as_gray=True)
	# 	lab = io.imread(location+"%d.png"%i,as_gray=True)

	# 	io.imsave(save_loc+"img/%d.png"%i,img)
	# 	io.imsave(save_loc+"label/%d.png"%i,lab)
	if os.path.exists(location2+"%s.png"%i):
		img = io.imread(location2+"%s.png"%i,as_gray=True)
		lab = io.imread(location+"%s.png"%i,as_gray=True)

		io.imsave(save_loc+"img/%s.png"%i,img)
		io.imsave(save_loc+"label/%s.png"%i,lab)
		
	#file1.write(filename[64 :])
	

