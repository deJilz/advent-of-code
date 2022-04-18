import os
from progress.bar import IncrementalBar


def main():
    # import the txt file into an array - it will use the py file name
    input_path = 'C:/Users/dejohncm/OneDrive - Air Products and Chemicals, Inc/python_venvs/AOC/2021/_inputs/'
    arry = [x for x in open(input_path+os.path.basename(__file__).split('.')[0]+'.txt', 'r')]
    bar = IncrementalBar('Processing',max=n) # n is loop duration


    # some main loop
    for i in range(5):
        # do something
        bar.next()
    bar.finish()
main()