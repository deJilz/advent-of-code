import os
import numpy as np
'''
28 April 2022
PART 1 - 423
PART 2 - 

Concepts: numpy
'''

array = np.array([list(x.strip()) for x in open(os.path.basename(__file__).split('_')[0]+'.txt', 'r')],dtype=int)

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