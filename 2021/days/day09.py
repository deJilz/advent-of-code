'''
28 April 2022
PART 1 - 423
PART 2 - 

Concepts: numpy
'''
import os
import numpy as np

def main():
    input_path = "C:\\Users\\cdejo\\Desktop\\Coding\\PythonPrograms\\AdventOfCode\\2021\\inputs\\"
    arry = [x[:-1] for x in open(input_path+os.path.basename(__file__).split('.')[0]+'.txt', 'r')]
    # Input to array
    array = np.array([[0] * len(arry[0])] * len(arry))
    for n,l in enumerate(arry):
        array[n] = list(l)

    # Add borders to help calculate risk
    array = np.pad(array, pad_width=1,constant_values=10)
    basin = np.zeros_like(array)
    
    # Loop through and check for low points
    risk = 0
    for x in range(1,len(array[:,0])-1): # rows
        for y in range(1,len(array)-1): # cols
            d = int(array[x,y]) # need d later
            if d < min([int(array[x+1,y]),int(array[x-1,y]), int(array[x,y+1]), int(array[x,y-1])]):
                risk += d + 1
                basin[x,y] = 1
    print("The risk level is " + str(risk) + "\n",basin)   
main()