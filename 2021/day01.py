'''
28 April 2022
did awhile ago in VBA lol
PART 1 - 1162
PART 2 - 1190

Concepts: 
'''
import os

def main():
    input_path = "C:\\Users\\cdejo\\Desktop\\Coding\\PythonPrograms\\AdventOfCode\\2021\\inputs\\"
    array = [int(x.strip()) for x in open(input_path+os.path.basename(__file__).split('.')[0]+'.txt', 'r')]
    
    av,last_av,k = 0,0,0
    for n in range(1,len(array)):
        av = sum(array[n:n+3])/3
        if av>last_av: k+=1
        last_av = av
    print("Elevation Changes: " + str(k-1))

main()