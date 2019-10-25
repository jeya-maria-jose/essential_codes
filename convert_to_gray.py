import glob
import numpy as np
from skimage import *
from skimage.transform import resize
import imageio

#file1 = open('brain_us_img_ids.txt','w+')

location = '/media/jeyamariajose/7888230b-5c10-4229-90f2-c78bdae9c5de/Data/Brain_Ultrasound/unet_small_syn/train/img/*.png'
save_loc = '/media/jeyamariajose/7888230b-5c10-4229-90f2-c78bdae9c5de/Data/Brain_Ultrasound/randomized/'

for filename in glob.iglob(location):
	img = io.imread(filename, as_gray=True)
	#print(img.shape)
	io.imsave(filename,img)
	

