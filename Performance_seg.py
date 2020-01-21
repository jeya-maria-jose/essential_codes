import glob
import numpy as np
from skimage import *
from skimage.transform import resize
import imageio
import os
import cv2
from scipy import ndimage, misc


location = '/media/jeyamariajose/7888230b-5c10-4229-90f2-c78bdae9c5de/Data/Brain_Ultrasound/wavelets/org/results/*.png'
save_loc = '/media/jeyamariajose/7888230b-5c10-4229-90f2-c78bdae9c5de/Data/Brain_Ultrasound/wavelets/org/test/label/'
location2 = '/media/jeyamariajose/7888230b-5c10-4229-90f2-c78bdae9c5de/Data/Brain_Ultrasound/Final/unet/test/img2/'


count = 0
f1_s_all=0
miou_all=0
pa_all=0

for filename in glob.iglob(location):
	
	count+=1

	yval = cv2.imread(filename,0)

	tmp = filename[-8 :]

	yHaT = cv2.imread(save_loc+tmp,0)
	
	yval[yval>=50] = 1
	yval[yval!=1]=0
	# yHaT[yHaT>=127] = 1
	# yHaT[yHaT!=1]=0
	# print(np.unique(yHaT))

	ttp = np.sum((yval == 1))
	tp = np.sum((yHaT == 1) & (yval == 1))
	fp = np.sum((yHaT == 1) & (yval == 0))
	fn = np.sum((yHaT == 0) & (yval == 1))
	tn = np.sum((yHaT == 0) & (yval == 0))
	print(tp,fp,fn)

	tot = tp+fp
	tot2 = tp+fn
	# print(tp)
	
	if tot==0 or tot2 ==0 or ttp==0:
		f1_s = 1
		miou = 1
		pa = 1
	else:
		precision = tp / (tp + fp);
		recall = tp / (tp + fn);
		f1_s = (2 * precision * recall) / (precision + recall);
		miou = tp / (tp+fn+fp)
		pa = (tp+tn)/(tp+tn+fp+fn)
	
	f1_s_all+=f1_s
	miou_all+=miou
	pa_all+=pa

print(count)
print(f1_s_all/count,miou_all/count,pa_all/count)
