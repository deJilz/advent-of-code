# 2022 - Day 3

import os

def main():
    input_path = 'C:/Users/cdejo/Desktop/Coding/PythonPrograms/AdventOfCode/2021/inputs/'
    array = [x.strip() for x in open(input_path+os.path.basename(__file__).split('.')[0]+'.txt', 'r')]
    
    gamma,eps = '',''
    for i in range(0,len(array[0])): # goes through each digit place
        gamma += most_common(array,i)
        eps += least_common(array,i)
    print('Power Consumed' + str(int(gamma,2)*int(eps,2)))

def most_common(array,c):
    if sum([int(x[c]) for x in array]) > (len(array)/2):
        return '1'
    return '0'

def least_common(array,c):
    if sum([int(x[c]) for x in array]) > (len(array)/2):
        return '0'
    return '1'

main()