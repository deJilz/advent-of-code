#!/usr/bin/python3
import sys
import os
import itertools
from collections import Counter
import numpy as np

'''
17 May 2022
AOC Day 17
Part 2: 1806
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
heights = [] # list of starting velocities that land in 

# Check every possible initial velocity
for y in range(-MAX_VEL,MAX_VEL):
    for x in range(0,MAX_VEL):
        # Get initial velocity
        x_vel = x
        y_vel = y
        # start from origin
        cur_x = 0
        cur_y = 0
        # loop until a shot lands past the bounded area
        while check_inside([cur_x,cur_y]) != -1:
            # check if the shot is inside the bounded area
            if check_inside([cur_x,cur_y]) == 1:
                # add the initial velocity to the big list
                heights.append([y,x])
                
            # Adjust the position
            cur_x += x_vel
            cur_y += y_vel
            
            # Adjust the velocity
            if x_vel != 0: # decreases by 1 until we hit zero
                # else just continue
                if x_vel > 0:
                    x_vel += -1
                else:
                    x_vel += 1
            y_vel += -1 # always decreases

# Create a hashable list
heights = [tuple(x) for x in heights]
# Create counter object to check the unique keys
cnt = Counter(heights).keys()
print('unique starting velocities: ',len(cnt))