# 2021 - Day 8

import os

def main():
    # import the txt file into an array - it will use the py file name
    input_path = 'C://Users//cdejo//Desktop//Coding//PythonPrograms//AdventOfCode//2021//inputs//'
    array = [x for x in open(input_path+os.path.basename(__file__).split('.')[0]+'.txt', 'r').readlines()]
    # data consists of only quote "output" data
    data = [array[i].strip().split("|")[1].split(" ")[1:] for i in range(len(array))]
    
    q = 0
    for j in data:
        q += sum([1 for p in j if trigger(len(p))])
    print(str(q)) # Part 1 - 365
    
def trigger(l):
    if ((l == 2) or (l == 4) or (l == 3) or (l == 7)):
        return 1
    return 0
main()

