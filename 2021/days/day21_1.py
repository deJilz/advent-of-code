#!/usr/bin/python3
import os

'''
17 May 2022
AOC Day 21
Part 1: 798147
'''
array = [int(x.strip()[-1]) for x in open(os.path.basename(__file__).split('_')[0]+'.txt', 'r')]
ROLLS = range(1,1000)
turn = False # False is player 1 turn, true is player 2 turn
BOARD_SIZE = 10
MAX_SCORE = 1000
n = 0

# Load PLAYERs into object
PLAYER = {'location':0,'score':0}
PLAYERS = {}
for i in range(0,len(array)):
    PLAYER = {'location':array[i],'score':0}
    PLAYERS[i] = PLAYER

# loop until the max score is over 1000
while max([PLAYERS[p]['score'] for p in range(0,len(array))])<MAX_SCORE:    
    # set who's turn it is
    if turn:
        k = 1
    else:
        k = 0

    # number of spaces to move
    move = sum(ROLLS[n:n+3])
    # what will the new space be
    space = ((PLAYERS[k]['location'] + move) % BOARD_SIZE)
    
    if space == 0:
        space = 10
    # add to this persons score
    PLAYERS[k]['score'] += space
    # add position and mod 10
    PLAYERS[k]['location'] = space

    # set up for next persons turn
    n += 3
    turn = not turn
    
# output
print('The dice has been rolled %i times.'%n)
print('The min score is %i'%(min([PLAYERS[p]['score'] for p in range(0,len(array))])))
print('The max score is %i'%(max([PLAYERS[p]['score'] for p in range(0,len(array))])))
print('Part 1 answer:',n*min([PLAYERS[p]['score'] for p in range(0,len(array))]))