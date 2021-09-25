# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 21:04:43 2021

@author: Shashwat Sparsh
"""
import scipy as sc
import numpy as np
import math as math

#Note: originCoord, abCoord, cdCoord, and angleCoord, are annotated on a screenshot in the repository

#   Original Coordinate Matrix
'''Origin Coords'''
x0 = 33.644561
y0 = -117.841662
originCoord = [x0, y0]

a0 = 33.644561
b0 = -117.84133
abCoord = [a0, b0]

c0 = 33.64428
d0 = -117.841662
cdCoord = [c0, d0]

horizStepVal = (b0-y0)/10
vertStepVal = (c0-x0)/10

'''Fill Coordinates'''
#Coords serves as the matrix to house all the geographical coordinates
Coords = []
#rowCoords serves as an array that is populated by a row of coordinates and then is appeneded into the Coords matrix
rowCoords = []
#These arrays store the discretized coordinates
yVals = []
xVals = []

#Discretization of 10 long coordinates in region prior to rotation
for n in range(0,10):
    if (n < 1):
        currentY = y0
    elif (n > 0):
        currentY = currentY + horizStepVal
    yVals.append(currentY)

#Discretization of 10 lat coordinates in region prior to rotation
for m in range(0,10):
    if (m < 1):
        currentX = x0
    elif (m > 0):
        currentX = currentX + vertStepVal
    xVals.append(currentX)

'''Combining the previous descretizations into a 10 by 10 matrix of long lat coordinates'''    
for i in range(0,10):
    for j in range(0,10):
        coord = [xVals[i],yVals[j]]
        rowCoords.append(coord)
    #append current Row Coordinates to Coords matrix
    Coords.append(rowCoords)
    #reset rowCoords array for next row
    rowCoords = []

#   Transform Coordinate Matrix by angle Theta
'''Angle Calculation'''
#xAngle and yAngle are coordinates parallel to the geometry of the plaza
xAngle = 33.64473
yAngle = -117.84141
angleCoord = [xAngle, yAngle]
#calculations of deltaLat and deltaLong for the theta angle of rotation calculation
horizDelta = angleCoord[1] - originCoord[1]
vertDelta = angleCoord[0] - originCoord[0]
#Calculation of theta in all quadrants
theta = np.arctan2(vertDelta, horizDelta)
#degTheta = math.degrees(theta)

'''Angle Rotation Function'''
def rotate(origin, point, angle):
    #the origin tuple is stored as y, x analogous to long, lat    
    oy, ox = origin
    py, px = point
    #the new coordinates are calculated by the angular rotation
    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    
    qx = round(qx, 6)
    qy = round(qy, 6)
    
    return (qy, qx)


#newCoords represents the region parallel to the plaza geometry
#newRowCoords serves the same function as rowCoords from earlier
newCoords = []
newRowCoords = []

'''Rotate Coords matrix by theta'''
for i in range(len(Coords)):
    for j in range(len(Coords[i])):
        newCoord = rotate(originCoord, Coords[i][j], theta)
        #print(newCoord)
        newRowCoords.append(newCoord)
    newCoords.append(newRowCoords)
    newRowCoords = []

'''Generate waypoint solution'''
#aStarSol stores the results from the A* algorithm at: https://gist.github.com/ryancollingwood/32446307e976a11a1185a5394d6657bc
#The map needs to be set to 10 x 10
#The two scripts are currently not linked yet but work separately as of now

#aStarSol serves as an array of tuples storing results from the mapping A* algorithm run separately
#The solution below is arbitrary and used solely for the sake of verifying this script works
aStarSol = [[1, 1], [0, 0], [9, 9]]
#waypoints store the long lat coordinates based on referencing the aStarSol to the newCoords matrix
waypoints = []

#loop through each tuple from the m
for i in range(len(aStarSol)):
    row_index = aStarSol[i][0]
    column_index = aStarSol[i][1]
    coordinate = newCoords[row_index][column_index]
    waypoints.append(coordinate)

#print solution in console
#print(waypoints)