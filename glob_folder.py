import glob 
from PIL import Image
from pytesseract import image_to_string

for filename in glob.iglob('/home/jeyamariajose/Projects/jjtech/text_ocr_tam/Data/png/**/*.png'):
	print(filename)


	file = open('/home/jeyamariajose/Projects/jjtech/text_ocr_tam/Data/txt/'+month+'/'+number+'.txt','w') 
	file.write(ans) 
	file.close() 


