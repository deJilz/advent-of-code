#!/usr/bin/python3
import os

'''
14 May 2022
AOC Day 8
Part 1: 365
'''
array = [x.strip() for x in open(os.path.basename(__file__).split('_')[0]+'.txt', 'r')]

def trigger(l):
    if ((l == 2) or (l == 4) or (l == 3) or (l == 7)):
        return 1
    return 0
    
# data consists of only "output" data
data = [array[i].strip().split("|")[1].split(" ")[1:] for i in range(len(array))]

q = 0
for j in data:
    q += sum([1 for p in j if trigger(len(p))])
print("Part 1: ",str(q))

