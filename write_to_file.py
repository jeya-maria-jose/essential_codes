import glob
import numpy as np
from skimage import *
from skimage.transform import resize
import imageio

#file1 = open('brain_us_img_ids.txt','w+')

location = '/media/jeyamariajose/7888230b-5c10-4229-90f2-c78bdae9c5de/Data/Brain_Ultrasound/randomized/Brain_test/*.png'
save_loc = '/media/jeyamariajose/7888230b-5c10-4229-90f2-c78bdae9c5de/Data/Brain_Ultrasound/randomized/'

for filename in glob.iglob(location):
	img = io.imread(filename)
	imgn = img[: , 0:512]
	lab = img[: , 512:1024]
	lab[lab>=1]=1
	print(filename[102 :])
	imageio.imwrite(save_loc+'test_img/'+filename[102 :],imgn)
	imageio.imwrite(save_loc+'test_label/'+filename[102 :],lab)
	#print(filename[45 :])

	#file1.write(filename[64 :])
	#file1.write("\n")


file1.close()
