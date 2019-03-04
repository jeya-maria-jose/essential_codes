import csv
import glob 
from shutil import copyfile

index = list()
with open('ml_cleaned.csv', 'r') as csvfile:
	csv_reader = csv.reader(csvfile, delimiter = ',')
	print csv_reader
	for column in csv_reader:
		
		index.append(float(column[0]))

#print(index)
j = 0
for i in index:

	j=j+1
	filename = "/home/jeyamariajose/Projects/dl/data/all/check%d.csv"%i
	filename2 = "/home/jeyamariajose/Projects/dl/data/cleaned/check%d.csv"%j
	
	print(filename)
	copyfile(filename, filename2)
