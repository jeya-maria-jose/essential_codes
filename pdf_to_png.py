import glob 
from pdf2image import convert_from_path

for filename in glob.iglob('/home/jeyamariajose/Projects/jjtech/text_ocr_tam/Data/pdf/**/*.pdf'):
	month = filename[58:65]
	number = filename[66:74]
	print filename
	pages = convert_from_path(filename, 500)

	for page in pages:
		page.save('/home/jeyamariajose/Projects/jjtech/text_ocr_tam/Data/png/'+month+'/'+number+'.png', 'png')