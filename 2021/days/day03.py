# 2022 - Day 3

import os

def main():
    input_path = 'C:/Users/cdejo/Desktop/Coding/PythonPrograms/AdventOfCode/2021/inputs/'
    array = [x.strip() for x in open(input_path+os.path.basename(__file__).split('.')[0]+'.txt', 'r')]
    
    gamma,eps = '',''
    cnts = [0]*len(array[0])
    for i in range(0,len(array[0])): # goes through each digit place
        cnts[i] = sum([int(x[i]) for x in array])
        if cnts[i] > len(array)/2:
            gamma += '1'
            eps += '0'
        else:
            gamma += '0'
            eps += '1'
    print(str(cnts))
    print('Power Consumed' + str(int(gamma,2)*int(eps,2)))
main()