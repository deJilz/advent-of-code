'''
10 May 2022
PART 1 ANSWER - 5585
PART 2 ANSWER - 

Concepts: 
'''

import os
import numpy as np

def main():
    array = [x.strip() for x in open('C:/Users/dejohncm/OneDrive - Air Products and Chemicals, Inc/python_venvs/AOC/2021/_inputs/'+os.path.basename(__file__).split('.')[0]+'.txt', 'r')]
    
    # Declare some
    WID = 10
    map = np.zeros((WID,WID))
    
    # Create np array
    points = np.array([[0]*4]*len(array))
    for n,a in enumerate(array):
        points[n][0], points[n][1] = a.split('->')[0].split(',')
        points[n][2], points[n][3] = a.split('->')[1].split(',')

    # Count trenches
    for n, point in enumerate(points):
        x1,x2,y1,y2 = point[0],point[2],point[1],point[3]
        print("",point)
        if (x1 != x2) and (y1 != y2): # diag
            #continue
            # get the x coord of the leftmost
            if x1 < x2:
                dx = x1
                dy = y1
            else:
                dx = x2
                dy = y2
            if y1 > y2:
                # first point is lower than second point
                for z in range(0,abs(y2-y1)+1):
                    map[dy+z,dx+z] += 1#dx+z,dy+z] += 1
            else:
                # 1st point in higer than 2nd
                for z in range(0,abs(y2-y1)+1):
                    print(" as",z,dx+z,dy-z)
                    map[dy-z,dx+z] += 1 #dx+z,dy-z] += 1

        if x1 == x2: # horizontal
            for y in range(min(y1,y2),max(y1,y2)+1):
                map[y,x1] += 1 # R C - 
        elif y1 == y2: # vertical
            for x in range(min(x1,x2),max(x1,x2)+1):
                map[y1,x] += 1
        print("Map\n",n)
        print("",to_string(map))
    print("Final Map\n",map)
    print("test tostring\n",to_string(map))
    #print("Final Map trans\n",map.transpose())
    print("Map Score: ",np.count_nonzero(map>1))

def to_string(map):
    for l in map:
        for e in l:
            if e == 0:
                print(" . ",end="")
            else:
                print(" ",int(e),end="")
        print("\n")

main()
    