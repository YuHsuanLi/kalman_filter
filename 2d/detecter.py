import cv2
import numpy as np
from PIL import Image, ImageSequence


gif_name = 'ball.gif'
gif = Image.open(gif_name)
index = 1
list = []
lower_red = np.array([0,0,100])
upper_red = np.array([0,0,255])
center_list = []

for frame in ImageSequence.Iterator(gif):
	frame = frame.convert('RGBA')  
	opencv_img = np.array(frame, dtype=np.uint8)  
	opencv_img = cv2.cvtColor(opencv_img, cv2.COLOR_RGBA2BGRA)
	gray = cv2.cvtColor(opencv_img, cv2.COLOR_RGB2GRAY)
	circle = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1,20,param1=50,param2=50)
	x, y, r = np.round(circle[0][0]).astype("int")
	cv2.circle(opencv_img, (x, y), r, (0, 255, 0), 4)
	center_list.append([x, y])
center_list = np.array(center_list)
np.save('center.npy', center_list)




	