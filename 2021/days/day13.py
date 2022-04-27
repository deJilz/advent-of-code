'''
26 April 2022
PART 1 - 942
PART 2 - JZGUAPRB

Concepts: Numpy arrays

'''
import os
import numpy as np

def main():
    input_path = 'C:\\Users\\cdejo\\Desktop\\Coding\\PythonPrograms\\AdventOfCode\\2021\\inputs\\'
    array = [x.strip() for x in open(input_path+os.path.basename(__file__).split('.')[0]+'.txt', 'r')]
    
    # Load the point arrays into a numpy array
    points = np.array([[0]*2]*array.index(''))
    
    # Populate the numpy array with the puzzle input
    n = 0
    while (array[n] != ''):
        points[n] = array[n].split(',')
        n+=1
    
    # Init some values/objects
    SIZE_x = max(points[:,0]) + 1
    SIZE_y = max(points[:,1]) + 1
    board = np.array([[0]*SIZE_x]*SIZE_y)
    
    # Store puzzle input folds for future use
    fold_matrix = []
    for f in range(n+1,len(array)):
        e1 = array[f].split('=')[0][-1:]
        e2 = int(array[f].split('=')[1])
        fold_matrix.append([e1,e2])
    
    # Mark the points from the puzzle input
    for x,y in points:
        board[y,x] = 1 # transpose it
    
    # Fold paper
    for axis, num in fold_matrix:
        print(" -> folding %s axis on %d" % (axis, num))
        board = fold(axis,num,board)
        print('There are %i dots visible now'%np.sum(board))
        
    print('Final board: ')
    to_string(board)
    
def fold(axis,c,deck):
    ''' wrapper class for folding takes x/y axis, col number, and board '''
    if axis == 'x':
        return fold_x(axis,c,deck)
    else:
        return fold_y(axis,c,deck)
    
def fold_x(axis,c,paper):
    for cols in range(0,c):
        for rows in range(0,len(paper[:,0])):
            if paper[rows,(2*c)-cols] == 1:
                paper[rows,cols] = 1
    return paper[:,0:c]
    
def fold_y(axis,c,paper):
    for rows in range(0,c):
        for cols in range(0,len(paper[0,:])):
            if paper[(2*c)-rows,cols] == 1:
                paper[rows,cols] = 1
    return paper[0:c,:]
    
def to_string(board):
    ''' np array to_string to match the website format '''
    for l in board:
        for r in l:
            if r:
                print("#",end=" ")
            else:
                print(".",end=" ")
        print("\n")
        
main()