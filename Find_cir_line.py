#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 14:31:08 2019

@author: apple
"""

import cv2
import numpy as np

img = cv2.imread("TrafficLight.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 90, 110)

lines = cv2.HoughLinesP(edges, 1, np.pi/180, 200, 20, 10)
circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 1, 120, param2=20, maxRadius=100, minRadius=30)

for line in lines:
    x1 = int(round(line[0][0]))
    y1 = int(round(line[0][1]))
    x2 = int(round(line[0][2]))
    y2 = int(round(line[0][3]))
    cv2.line(img, (x1, y1), (x2, y2), (255, 255, 0), 10)
    
for i in circles[0, :]:
    cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
    cv2.circle(img,(i[0], i[1]), 2, (0, 0, 255), 3)
    
cv2.imwrite("Linescircles.jpg", img)
#cv2.waitKey(0)

#cv2.destroyAllWindows()