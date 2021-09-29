from PIL import Image
import pytesseract
import numpy as np

def process_image(iamge_name, lang_code):
	return pytesseract.image_to_string(Image.open(iamge_name), lang=lang_code)

def print_data(data):
	print(data)

def output_file(filename, data):
	print('hello world!')
	file = open(filename, "w+")
	file.write(data)
	file.close()

def main():
	#data_eng = process_image("test_eng.png", "eng")
	#data_ben = process_image("test_ben.png", "ben")
	#data_fas = process_image("/home/milad/Documents/all_programming_projects/ocr/tesseract_ocr/images/oranization_letter.jpg", "fas")
	data_fas = process_image("/home/milad/Documents/all_programming_projects/ocr/tesseract_ocr/images/keyhan_newspaper_test1.jpeg", "fas")
    #print_data(data_eng)
	#print_data(data_ben)
	#output_file("eng.txt", data_eng)
	#output_file("ben.txt", data_ben)
	output_file("./outputs/fas3.txt", data_fas)


if  __name__ == '__main__':
	main()