#!/usr/bin/python3
import sys
import os
import itertools
import collections
import numpy as np
from textwrap import wrap

'''
14 May 2022
AOC Day 4 part 2
Part 2: 4880
'''

data = [x.strip() for x in open(os.path.basename(__file__).split('_')[0]+'.txt', 'r')]
calls = [int(x) for x in data[0].split(',')]

# create boards
boards = {}
j=0
for n in range(2,len(data),6):
    board = {'board':np.zeros((5,5)),'calls':np.zeros((5,5)),'won':True,'hits':0}
    board['board'] = np.array([wrap(x,3) for x in data[n:n+5]],dtype=int)
    boards[j] = board
    j += 1

def check_bingo(board):
    # horizontal check
    for r in board['calls']:
        if sum(r) == 5:
            return True
    # vertical check
    for c in board['calls'].T:
        if sum(c) == 5:
            return True
    return False

breakout = False
for call in calls:
    print(' call',call)
    for b in boards:
        if call not in boards[b]['board']:
            continue
        # get number coordinates - !! assumes only one hit
        listOfCoords = list(zip(np.where(boards[b]['board'] == call)))
        # marks the call board
        boards[b]['calls'][listOfCoords[0],listOfCoords[1]] = 1
        # sets num to zero
        boards[b]['board'][listOfCoords[0],listOfCoords[1]] = -1
        boards[b]['hits'] += 1
        if check_bingo(boards[b]):
            boards[b]['won'] = False
            check_sum = sum([boards[k]['won'] for k in boards])
            if check_sum == 0: # the last board was just marked above
                print(' The last board won!',b)
                print('  score: ',(boards[b]['board'].sum()+boards[b]['hits'])*call)
                breakout = True
                break
    if breakout:
        break