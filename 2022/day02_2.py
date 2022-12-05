#!/usr/bin/python3
import sys, os, itertools, collections
import numpy as np

'''
4 Dec 2022
AOC Day 2
Part 2:  3241 (too low), 10967 (too low) -- 12014!
'''
array = [x.strip() for x in open(os.path.basename(__file__).split('_')[0]+'.txt', 'r')]
gameDiff = 0
score = 0

for el in array:
    
    oppThrow = el[0]
    chosenThrow = ''
    
    if el[-1] == 'X': # need to lose
        if oppThrow == 'A':   # rock
            chosenThrow = 'Z' # scissor
        elif oppThrow == 'B': # paper
            chosenThrow = 'X' # rock
        elif oppThrow == 'C': # scissor
            chosenThrow = 'Y' # paper
            
    elif el[-1] == 'Y': # need to draw
        chosenThrow = chr(ord(oppThrow)+23) # same as oponent
        
    elif el[-1] == 'Z': # need to win
        if oppThrow == 'A':   # rock
            chosenThrow = 'Y' # paper
        elif oppThrow == 'B': # paper
            chosenThrow = 'Z' # scissor
        elif oppThrow == 'C': # scissor
            chosenThrow = 'X' # rock
        
    
    # ----------------- vvv from part 1
    gameDiff = abs(ord(oppThrow) - ord(chosenThrow))
    
    match gameDiff:
        case 23: # draw scenario
            score += 3 + (ord(chosenThrow) - 87)
        case 24 | 21: # win scenario
            score += 6 + (ord(chosenThrow) - 87)
        case 22 | 25: # loose scenario
            score += 0 + (ord(chosenThrow) - 87)
    
print("final score",score)
    