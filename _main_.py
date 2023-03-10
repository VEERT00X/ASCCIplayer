# Importing the libraries

import os 
import sys
import cv2
from PIL import Image

# Configuration

def get_file_path():
    try:
        file_path = sys.argv[1]
    except IndexError:
        file_path = input("Enter file path: ")
    print("File path loaded: " + file_path)
    return file_path

FILE_PATH = get_file_path() 
ASCII = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", ".","!","^","&","~","-","_"]

# Functions

def resized_gray_image(image ,new_width=70):
	width,height = image.size
	aspect_ratio = height/width
	new_height = int(aspect_ratio * new_width)
	resized_gray_image = image.resize((new_width,new_height)).convert('L')
	return resized_gray_image

def pixEl(image):
	pixels = image.getdata()
	characters = "".join([ASCII[pixel//25] for pixel in pixels])
	return characters

def generate(image,new_width=70):
	new_image_data = pixEl(resized_gray_image(image))

	total_pixels = len(new_image_data)

	ascii_image = "\n".join([new_image_data[index:(index+new_width)] for index in range(0, total_pixels, new_width)])

	sys.stdout.write(ascii_image)
	os.system('cls' if os.name == 'nt' else 'clear')
cap = cv2.VideoCapture(FILE_PATH)

# Main

if __name__ == "__main__":
    while True:

        ret,frame = cap.read()
        cv2.imshow("frame",frame)
        generate(Image.fromarray(frame))
        cv2.waitKey(1)

