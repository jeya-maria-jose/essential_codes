import glob
import numpy as np
from skimage import *
from skimage.transform import resize
import imageio
import os
import cv2

#file1 = open('brain_us_img_ids.txt','w+')

location = '/home/jeyamariajose/Projects/Overcomplete-Autoencoder/Segmentation/oc_ae_t/'
save_loc = '/media/jeyamariajose/7888230b-5c10-4229-90f2-c78bdae9c5de/Data/Brain_Ultrasound/Final/results/oc_ae_t/'

count = 0

for k in range(1,20):
	count=count+5
	for i in range(0,330):
		# t = str(i).zfill(4)
		# # t = int(t)
		# print(t)

		img = np.ones((512,512))
		# print(img.shape)
		for j in range(1,17):
			
			t = str(i).zfill(4)
			t = t + "_"+str(j)
			# print(t)
			tmp1 = cv2.imread(location+str(count)+"/"+t+".png",0)

			if j<=4:
				img[0:128,int(512*((j-1)/4)):int(512*((j)/4))] = tmp1
			elif j>4 and j<=8:
				print(i,j)
				img[128:256,int(512*((j-5)/4)):int(512*((j-4)/4))] = tmp1
			elif j>8 and j<=12:
				img[256:384,int(512*((j-9)/4)):int(512*((j-8)/4))] = tmp1
			elif j>12 and j<=16:
				img[384:512,int(512*((j-13)/4)):int(512*((j-12)/4))] = tmp1 

		if not os.path.isdir(save_loc + str(count)+"/"):

			os.makedirs(save_loc + str(count)+"/")
		cv2.imwrite(save_loc + str(count)+"/" + str(i).zfill(4) + ".png",img)



"""	
for filename in glob.iglob(location):
	
	img = cv2.imread(filename,0)	
	img1 = img[0:128,0:128]
	img2 = img[0:128,128:256]
	img3 = img[0:128,256:384]
	img4 = img[0:128,384:512]
	
	img5 = img[128:256,0:128]
	img6 = img[128:256,128:256]
	img7 = img[128:256,256:384]
	img8 = img[128:256,384:512]

	img9 = img[256:384,0:128]
	img10 = img[256:384,128:256]
	img11 = img[256:384,256:384]
	img12 = img[256:384,384:512]

	img13 = img[384:512,0:128]
	img14 = img[384:512,128:256]
	img15 = img[384:512,256:384]
	img16 = img[384:512,384:512]

	tmp = filename[-8 :]
	# for i in range(1,16):
	# 	file = "img"+str(i)
	cv2.imwrite(save_loc + tmp[: -4]+"_1.png",img1)
	cv2.imwrite(save_loc + tmp[: -4]+"_2.png",img2)
	cv2.imwrite(save_loc + tmp[: -4]+"_3.png",img3)
	cv2.imwrite(save_loc + tmp[: -4]+"_4.png",img4)
	cv2.imwrite(save_loc + tmp[: -4]+"_5.png",img5)
	cv2.imwrite(save_loc + tmp[: -4]+"_6.png",img6)
	cv2.imwrite(save_loc + tmp[: -4]+"_7.png",img7)
	cv2.imwrite(save_loc + tmp[: -4]+"_8.png",img8)
	cv2.imwrite(save_loc + tmp[: -4]+"_9.png",img9)
	cv2.imwrite(save_loc + tmp[: -4]+"_10.png",img10)
	cv2.imwrite(save_loc + tmp[: -4]+"_11.png",img11)
	cv2.imwrite(save_loc + tmp[: -4]+"_12.png",img12)
	cv2.imwrite(save_loc + tmp[: -4]+"_13.png",img13)
	cv2.imwrite(save_loc + tmp[: -4]+"_14.png",img14)
	cv2.imwrite(save_loc + tmp[: -4]+"_15.png",img15)
	cv2.imwrite(save_loc + tmp[: -4]+"_16.png",img16)
	
	# ret,thresh = cv2.threshold(img,127,255,0)
	# image, contours, hierarchy = cv2.findContours(img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	# img = cv2.drawContours(img, contours, -1, (0,255,0), 3)

	 
	# numcont = len(contours)

	# if numcont==0:
	# 	count = count+1
	# 	print(filename[-8 :])
	# 	#break
		
	# 	os.remove(filename)
	# 	os.remove((save_loc+filename[-8 :]))

	#file1.write(filename[64 :])
	#print(filename[108:112]+'s')
	# io.imsave(save_loc+filename[108:112]+"s.png",img)
	
#print(count)
"""