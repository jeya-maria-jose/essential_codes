import glob
import numpy as np
from skimage import *
from skimage.transform import resize
import imageio
import os
import cv2
#file1 = open('brain_us_img_ids.txt','w+')

#location = '/home/jeyamariajose/Projects/Self_Attention_Aux_Synthesis/results/trainastest/brainus-SA-rerun/test_latest/images/*.png'
location = '/media/jeyamariajose/7888230b-5c10-4229-90f2-c78bdae9c5de/Data/Brain_Ultrasound/wavelets/bior8/test/labelcol/*.png'
save_loc = '/media/jeyamariajose/7888230b-5c10-4229-90f2-c78bdae9c5de/Data/Brain_Ultrasound/wavelets/bior8/test/label/'

count = 0
for filename in glob.iglob(location):

	img = cv2.imread(filename, 0)
	#print(img.shape)
	
	img[img!=255] = 0

	img[img==255] = 1
	#print(np.unique(img))
	
	#label = img[:,0:256]
	#r,c = label.shape
	#print(r,c)
	tmp = filename[-8 :]
	# 
	#print(tmp)
	cv2.imwrite(save_loc+tmp,img)

	# if tmp[-1 :]!='1':
	# 	#os.remove(filename)
	# 	tmp = filename[-7 :]
	# 	#print(tmp[: -4])
	# 	i = str(tmp[: -4])
	# 	i = i.zfill(4)
	# 	#count = count+1
	# 	count = count+1
	


	# 	#print(filename[: -7])
	# 	print(i)
	# 	io.imsave(save_loc + i + ".png",img)




