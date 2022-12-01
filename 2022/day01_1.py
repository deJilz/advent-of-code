#!/usr/bin/python3
import sys
import os
import itertools
import collections
import numpy as np

'''
December 1 2022
AOC Day 1
Part 1: 66186
'''
array = [x.strip() for x in open(os.path.basename(__file__).split('_')[0]+'.txt', 'r')]

thisElfsDiet = 0
fattestElfsDiet = -1

for a in array:
    if a == "":
        fattestElfsDiet = max(thisElfsDiet, fattestElfsDiet)
        thisElfsDiet = 0
    else:
        thisElfsDiet += int(a)
    
print(f"The fattest elf is carring %i calories." % fattestElfsDiet)
