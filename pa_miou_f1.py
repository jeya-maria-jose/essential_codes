import numpy as np
import cv2

yval = cv2.imread("/home/jeyamariajose/Projects/CBAS/results_CBAS_pics/real25.png")

yHaT = cv2.imread("/home/jeyamariajose/Projects/CBAS/results_CBAS_pics/real_target.png")

ttp = np.sum((yval == 1))

tp = np.sum((yHaT == 1) & (yval == 1))
fp = np.sum((yHaT == 1) & (yval == 0))
fn = np.sum((yHaT == 0) & (yval == 1))
tn = np.sum((yHaT == 0) & (yval == 0))
# print(tp,fp,fn)

tot = tp+fp
tot2 = tp+fn
if tot==0 or tot2 ==0 or tp==0:
    f1_s = 1
    miou = 1
    pa = 1
else:
  precision = tp / (tp + fp);
  recall = tp / (tp + fn);
  f1_s = (2 * precision * recall) / (precision + recall);
  miou = tp / (tp+fn+fp)
  pa = (tp+tn)/(tp+tn+fp+fn)


print(f1_s,miou,pa)



  
