#!/usr/bin/python3
import sys
import os
import itertools
import collections
import numpy as np

'''
4 Dec 2022
AOC Day 2
Part 1: 11873
'''
array = [x.strip() for x in open(os.path.basename(__file__).split('_')[0]+'.txt', 'r')]
gameDiff = 0
score = 0

for el in array:
    # check win/loose/draw
    gameDiff = abs(ord(el[0]) - ord(el[-1]))
    
    match gameDiff:
        case 23: # draw scenario
            score += 3 + (ord(el[-1]) - 87)
        case 24 | 21: # win scenario
            score += 6 + (ord(el[-1]) - 87)
        case 22 | 25: # loose scenario
            score += 0 + (ord(el[-1]) - 87)
    
    
print("final score",score)
    