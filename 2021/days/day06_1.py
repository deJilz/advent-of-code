#!/usr/bin/python3
import os
import numpy as np

'''
14 May 2022
AOC Day 6
Part 1: 375482
'''
array = np.array([list(map(int,x.strip().split(','))) for x in open(os.path.basename(__file__).split('_')[0]+'.txt', 'r')][0],dtype=int)

ages = np.zeros(10)
DAYS = 80

for i in array:
    ages[i] += 1

def decrease_ages(fish):
    new_fish = np.zeros(10)
    for i in range(0,len(fish)-1):
        new_fish[i] = fish[i+1]
    return new_fish

for day in range(1,DAYS):
    ages = decrease_ages(ages)
    # The get +1 more days so everything can get aged next loop
    ages[9] += ages[0]
    ages[7] += ages[0]
    ages[0] = 0
    
print("After %s days there are %i fish!" %(DAYS,ages.sum()))