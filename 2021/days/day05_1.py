#!/usr/bin/python3
import sys
import os
import itertools
import collections
import numpy as np

'''
14 May 2022
AOC Day 5
Part 1: 5585
'''
array = [x.strip() for x in open(os.path.basename(__file__).split('_')[0]+'.txt', 'r')]

# Declare some
WID = 1000
map = np.zeros((WID,WID))

# Create np array
points = np.array([[0]*4]*len(array))
for n,a in enumerate(array):
    points[n][0], points[n][1] = a.split('->')[0].split(',')
    points[n][2], points[n][3] = a.split('->')[1].split(',')

# Count trenches
for n, point in enumerate(points):
    x1,x2,y1,y2 = point[0],point[2],point[1],point[3]
    if (x1 != x2) and (y1 != y2): # diag
        continue
    if x1 == x2: # horizontal
        for y in range(min(y1,y2),max(y1,y2)+1):
            map[y,x1] += 1 # R C - 
    elif y1 == y2: # vertical
        for x in range(min(x1,x2),max(x1,x2)+1):
            map[y1,x] += 1
print("Map Score: ",np.count_nonzero(map>1))