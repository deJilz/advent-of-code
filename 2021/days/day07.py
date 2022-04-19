
#from progress.bar import IncrementalBar
#bar = IncrementalBar('Processing',max=n) # n is loop duration
#bar.next()
#bar.finish()

import os

def main():
    # import the txt file into an array - it will use the py file name
    input_path = 'C://Users//cdejo//Desktop//Coding//PythonPrograms//AdventOfCode//2021//inputs//'
    array = [x for x in open(input_path+os.path.basename(__file__).split('.')[0]+'.txt', 'r').readlines()]
    array = list(map(int, array[0].strip().split(",")))
    

        
main()