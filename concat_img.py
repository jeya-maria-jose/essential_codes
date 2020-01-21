import os
import glob
import numpy as np
from skimage import *
from skimage.transform import resize
import imageio
import cv2
#file1 = open('brain_us_img_ids.txt','w+')

location = '/media/jeyamariajose/7888230b-5c10-4229-90f2-c78bdae9c5de/Data/Brain_Ultrasound/play/image/*.png'
save_loc = '/media/jeyamariajose/7888230b-5c10-4229-90f2-c78bdae9c5de/Data/Brain_Ultrasound/Final/unet_small_mix_tr3/train/label/'

c= 1
for filename in glob.iglob(location):
	#print(filename)
	# i = str(c)
	# i = i.zfill(4)

	# c=c+1

	img = cv2.imread(filename)
	#print(img.shape)

	#print(np.unique(img))
	#img[img!=255] = 0

	#img[img==255] = 1
	#img = img[50:450, 50:450];
	#print(np.unique(img))
	
	#label = img[:,0:256]
	num = filename[-8 :]
	tmp = filename[: -14]

	label = cv2.imread(tmp+'label/'+num)

	newimg = np.concatenate((img,label),axis = 1)
	sub = (np.unique(label))==255
	suble = len(sub)

	#print(num[: 4])
	#cv2.imwrite(tmp + 'new/'+num,newimg)
	if sub[suble-1]==True:
		c+=1
		cv2.imwrite(tmp + 'new2/'+num,newimg)


	#print(tmp)
	# if 'r' in tmp:
	# 	os.remove(filename)
	# #print(tmp)
	#if tmp[3]!='n':
	#	os.remove(filename)
	#resized = cv2.resize(img, (512,512), interpolation = cv2.INTER_AREA)
	#io.imsave(filename,resized)
	#label = io.imread(filename[: -12]+"label/"+filename[-8 :], as_gray=True)
	#cv2.imwrite(filename[: -8]+tmp[0:4]+'r'+'.png',img)
	#os.remove(filename)

print(c)



