#!/usr/bin/python3
import sys
import os
import itertools
import collections
import numpy as np

'''
20 May 2022
AOC Day 11
Part 1: 1640
'''

array = np.array([list(x.strip()) for x in open(os.path.basename(__file__).split('_')[0]+'.txt', 'r')])
array = array.astype(int)

STEPS = 100
cnt = 0
R = len(array)
C = len(array[0])

def flash(r,c):
    global cnt
    cnt += 1 # we flashed
    array[r][c] = -1 # mark as visited
    # look around flashing cell
    for dr in [-1,0,1]:
        for dc in [-1,0,1]:
            rr = r + dr
            cc = c + dc
            # make sure within bounds and is not visited
            if 0<=rr<R and 0<=cc<C and array[rr][cc] != -1:
                array[rr][cc] += 1
                if array[rr][cc] >= 10: # does this new cell need to flash
                    flash(rr,cc)
            

print('before any steps\n',array)

for s in range(0,STEPS):
    # inital flash at the beginning of each step
    array = array + 1
    
    # check for 9s in array now to recursivley flash
    for y in range(R):
        for x in range(C):
            if array[y][x] == 10:
                flash(y,x)
    
    # set visisted cells to zero
    for y in range(R):
        for x in range(C):
            if array[y][x] == -1:
                array[y][x] = 0
    
    print('after step',s+1)
    print('',array)

print("Total flashes: ",cnt)