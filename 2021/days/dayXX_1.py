# Connor DeJohn - 4 April 2022

import os

def main():
    # import txt file with the name of py file
    data = [x for x in open('C:/Users/cdejo/Desktop/Coding/PythonPrograms/AdventOfCode/2021/inputs/'+os.path.basename(__file__).split('.')[0]+'.txt','r')]
    

main()