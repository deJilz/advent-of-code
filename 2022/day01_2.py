#!/usr/bin/python3
import sys
import os
import itertools
import collections
import numpy as np

'''
December 1 2022
AOC Day 1
Part 2: 196804
'''
array = [x.strip() for x in open(os.path.basename(__file__).split('_')[0]+'.txt', 'r')]

thisElfsDiet = 0
elfDiets = []

for a in array:
    if a == "":
        elfDiets.append(thisElfsDiet) 
        thisElfsDiet = 0
    else:
        thisElfsDiet += int(a)

elfDiets.sort()
print("The fattest three elfs have a total of ",sum(elfDiets[-3:]))
