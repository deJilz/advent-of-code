#!/usr/bin/python3
import sys
import os
import itertools
import collections
import numpy as np

'''
17 May 2022
AOC Day 17
Part 1: 5886
'''
array = [x.strip() for x in open(os.path.basename(__file__).split('_')[0]+'.txt', 'r')][0]
x_s = [int(x) for x in array[15:].split(',')[0].split('..')]
y_s = [int(x) for x in array[15:].split(',')[1][3:].split('..')]


def check_inside(pt):
    ''' takes a pt array input check_inside([180,-100]) 
    and returns if it is inside the input bounds 
    1  - inside the target area
    0  - not at the target area yet
    -1 - past the target area
    '''
    if x_s[0] <= pt[0] <= x_s[1] and y_s[0] <= pt[1] <= y_s[1]:
        return 1 # in the target area
    if pt[0] > x_s[1] or pt[1] < y_s[0]:
        return -1 # past the target area
    return 0 # not there yet


MAX_VEL = 1000
heights = [] # list of all the max heights

# Check every possible initial velocity
for y in range(1,MAX_VEL):
    for x in range(1,MAX_VEL):
        # Get initial velocity
        x_vel = x
        y_vel = y
        # start from origin
        cur_x = 0
        cur_y = 0
        # reset shot height list
        height = []
        # loop until a shot lands past the bounded area
        while check_inside([cur_x,cur_y]) != -1:
            # check if the shot is inside the bounded area
            if check_inside([cur_x,cur_y]) == 1:
                #print(" -- inside target - max:",max(height))
                # add the max height to the big list
                heights.append(max(height))
            
            # add the height to the small list
            height.append(cur_y)
            
            # Adjust the position
            cur_x += x_vel
            cur_y += y_vel
            
            # Adjust the velocity
            x_vel += -1 # decreases by 1 until we hit zero
            if x_vel <0:
                x_vel = 0
            y_vel += -1 # always decreases
# print the max of the big list
print('max y',max(heights))