'''
28 April 2022
Did awhile ago, also did this in VBA a bit ago lol
PART 1 - 2036120
PART 2 - 2015547716

Concepts: 
'''
import os

def main():
    input_path = "C:\\Users\\cdejo\\Desktop\\Coding\\PythonPrograms\\AdventOfCode\\2021\\inputs\\"
    commands = [x.strip() for x in open(input_path+os.path.basename(__file__).split('.')[0]+'.txt', 'r')]
    x,y,aim = 0,0,0
    for cm in commands:
        ty, num = cm.split(' ')
        num = int(num)
        if ty == 'forward':
            x+= num
            y+= (aim*num)
        elif ty == 'up':
            #y-=num
            aim-=num
        elif ty == 'down':
            #y+=num
            aim+=num
    print("Output (part 2 config): ",abs(x*y))

main()