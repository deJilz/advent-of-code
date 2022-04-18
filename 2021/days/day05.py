# Connor DeJohn - 4 April 2022

import os
import numpy

class clsBoard:
    """simple board class"""
    x = 1000
    y = 1000
    
    def __init__(self):
        x = 1000
        y = 1000
        board = numpy.zeros((x, y))
        #return self
    
    # def __init__(self, xrng, yrng):
        # x = xrng
        # y = yrng
        # board = numpy.zeros((x, y))
    
    def __str__(self):
        return 'Too big to show....'
    
    # [['941', '230'], '->', ['322', '849']]
    def add_vert(self, line):
        #print(str(line[0][0]))
        for n in range(line[0][1],line[2][1]):
            print(str(n))
        
    def add_hor(self, line):
        print(str(line[0][0]))



def main():
    # import txt file with the name of py file
    data = [x for x in open('C:/Users/cdejo/Desktop/Coding/PythonPrograms/AdventOfCode/2021/inputs/'+os.path.basename(__file__).split('.')[0]+'.txt','r')]
    # do a dictionary of them  138,842 -> 138,133
    data = [list(x.split(' ')) for x in data]
    for n in range(0,len(data)):
        data[n][0] = data[n][0].split(',')
        data[n][2] = data[n][2].split(',')
        data[n][2][1] = data[n][2][1][:-1]
        
    # create board class
    brd = clsBoard()
    print(str(data[0][0][0])) # puts out the 1st digit
    
    #loop through inputs
    for k in data:
        if k[0][0] == k[0][1]: # if this is a horizontal
            brd.add_hor(k)
        elif k[2][0] == k[2][1]: # if this is a vertical
            brd.add_vert(k)
        
    #print(str(brd.board[0,0]))
main()