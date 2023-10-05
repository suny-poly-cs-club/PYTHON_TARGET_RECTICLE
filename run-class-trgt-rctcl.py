import cv2 as cv
import numpy as np


x0 = 0 
y0 = 0
x1 = 100
y1 = 100

B0 = 0
G0 = 0
R0 = 255

PATH = r'C:\Users\Administrator\OneDrive - SUNY Polytechnic Institute\DSP\DEV\PROJECTS\PYTHON\COMPUTER_VISION\img\Warno-feature-2000x1270-1.jpg'    

cap = cv.VideoCapture(r"C:\Users\Administrator\OneDrive - SUNY Polytechnic Institute\DSP\DEV\PROJECTS\PYTHON\COMPUTER_VISION\dartVid.webm")
frame = cap.read()
cv.imshow("Frame", frame[1])
cv.waitKey(0)