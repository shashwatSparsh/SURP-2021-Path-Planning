# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 21:04:43 2021

@author: Shashwat Sparsh
"""
import scipy as sc
import numpy as np
import math as math

#   Original Coordinate Matrix
'''Origin Coords'''
x0 = 33.644561
y0 = -117.841662

a0 = 33.644561
b0 = -117.84133
abCoord = [a0, b0]

c0 = 33.64428
d0 = -117.841662

horizStepVal = (b0-y0)/10
vertStepVal = (c0-x0)/10

'''Fill Coordinates'''
Coords = []
rowCoords = []
yVals = []
xVals = []

for n in range(0,10):
    if (n < 1):
        currentY = y0
    elif (n > 0):
        currentY = currentY + horizStepVal
    yVals.append(currentY)

#print(yVals)
#print(len(yVals))

for m in range(0,10):
    if (m < 1):
        currentX = x0
    elif (m > 0):
        currentX = currentX + vertStepVal
    xVals.append(currentX)

#print(xVals)
#print(len(xVals))
    
for i in range(0,10):
    for j in range(0,10):
        coord = [xVals[i],yVals[j]]
        rowCoords.append(coord)
    Coords.append(rowCoords)

#print(Coords)
#print(rowCoords)    


#   Translate Coordinate Matrix by angle Theta

'''Angle Calculation'''
xAngle = 33.64473
yAngle = -117.84141
angleCoord = [xAngle, yAngle]
originCoord = [x0, y0]

horizDelta = angleCoord[1] - originCoord[1]
vertDelta = angleCoord[0] - originCoord[0]

theta = np.arctan2(vertDelta, horizDelta)
#degTheta = math.degrees(theta)

'''Angle Rotation Function'''
def rotate(origin, point, angle):
    
    oy, ox = origin
    py, px = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return qy, qx




#print(theta)
#theta = np.arctan(aDeltax, aDeltay)