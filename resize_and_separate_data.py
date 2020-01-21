import glob
import numpy as np
from skimage import *
from skimage.transform import resize
import imageio
import os
import cv2
from scipy import ndimage, misc

#file1 = open('brain_us_img_ids.txt','w+')

location = '/home/jeyamariajose/Baselines/pytorch-CycleGAN-and-pix2pix/datasets/night2day/train/*.jpg'
save_loc = '/media/jeyamariajose/7888230b-5c10-4229-90f2-c78bdae9c5de/Data/night2day/train/'
# location2 = '/media/jeyamariajose/7888230b-5c10-4229-90f2-c78bdae9c5de/Data/Brain_Ultrasound/Final/unet/test/img2/'


count = 0

for filename in glob.iglob(location):

	fl = filename.split("/")
	tmp = fl[8]
	image = cv2.imread(filename)
	image = misc.imresize(image, (128, 256))
	img = image[:,0:128]
	label = image[:,128:256]
	
	# tmp = filename[-8 :]
	
	# print(tmp)

	# if tmp=="..jpg":
	# os.remove(filename)

	# a=int(tmp[: 4])
	# a+=1300
	# print(str(a))
	
	# print(tmp)
	
	cv2.imwrite(save_loc + "img/" + tmp,img)
	cv2.imwrite(save_loc + "label/" + tmp,label)




	#color_img = cv2.cvtColor(img,cv2.COLOR_GRAY2RGB)

	#ret,thresh = cv2.threshold(img,127,255,0)
	#image, contours, hierarchy = cv2.findContours(img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	# img = cv2.drawContours(img, contours, -1, (0,255,0), 3)

	#img[img>=0.5] = 255

	#cv2.imwrite(save_loc+filename[-8 :],img)
	#numcont = len(contours)

	# if numcont==0:
	# 	count+=1
	# 	print(filename[-8:])
	# 	os.remove(save_loc+filename[-8:])
	
	# if "fake_B" in filename:
	# 	#os.remove(filename)
	# 	#print(filename[: -15])
	# 	#print(filename[94:98])
	# 	#print("HI")
	# 	count = count+1
	# 	#print(filename[100:104])
	# 	cv2.imwrite(filename[: -15]+filename[94:98]+".png",img)
	# 	os.remove(filename)
	# else:
	# 	os.remove(filename)
	# #r,c =img.shape

	# if r!=512 or c!=512:
	# 	count = count+1
	#print(img.shape)
	# 	#break
		
	# 	os.remove(filename)
	# 	os.remove((save_loc+filename[-8 :]))
	#cv2.imsave(filename,img)
	#file1.write(filename[64 :])
	
print(count)
