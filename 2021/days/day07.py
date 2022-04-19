# 2021 - Day 7

import os

def main():
    # import the txt file into an array - it will use the py file name
    input_path = 'C://Users//cdejo//Desktop//Coding//PythonPrograms//AdventOfCode//2021//inputs//'
    array = [x for x in open(input_path+os.path.basename(__file__).split('.')[0]+'.txt', 'r').readlines()]
    array = list(map(int, array[0].strip().split(",")))
    
    y = []
    for i in range(min(array),max(array)):
        f = sum([((abs(k-i)*(abs(k-i)+1))/2) for k in array])
        y.append(f)
    print ("Cheapest option costs " + str(min(y)))

main()

