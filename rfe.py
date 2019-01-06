from sklearn.feature_selection import RFE
from sklearn.svm import LinearSVC
import numpy as np
import pandas as pd
from sklearn import svm

array_lst=pd.read_csv('inputdata_wo_OS.csv')
array_OS=pd.read_csv('OS.csv')
svm = LinearSVC()
rfe = RFE(svm, 50)
rfe.fit(array_lst,array_OS)
ranking_RFE=rfe.ranking_
arr=np.asarray(array_lst)
print(rfe.support_)
print(rfe.ranking_)
indices=np.where(ranking_RFE==1)
print(indices)
data_RFE=arr[:,indices]
data=np.squeeze(data_RFE)
print data