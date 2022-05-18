'''
28 April 2022
PART 1 - 362271
PART 2 - 

Concepts: 
'''
import os

def main():
    # import the txt file into an array - it will use the py file name
    input_path = "C:\\Users\\cdejo\\Desktop\\Coding\\PythonPrograms\\AdventOfCode\\2021\\inputs\\"
    array = [x for x in open(input_path+os.path.basename(__file__).split('.')[0]+'.txt', 'r')]
    
    err_hits = {')':0,
                ']':0,
                '}':0,
                '>':0}
    t = 0
    # part 1
    for l in array:
        try:
            err_hits[stack_1(l)] += 1
        except:
            t = 0
        #print("------------")
    print('Part 1 score: ' + str(score_errors(err_hits)))
    # part 2
    s = 0
    err_hits = {')':0,
                ']':0,
                '}':0,
                '>':0}
    for l in array:
        try:
            s += sum(stack_2(l))
        except:
            t=0
    print('Part 2 score: ' + str(s))

def score_errors(err_hits):
    ''' err_hits is a dict wtih the amount of errors each bracket had '''
    score_card = {')':3,
                  ']':57,
                  '}':1197,
                  '>':25137}
    return sum([score_card[k]*err_hits[k] for k in [')',']','}','>']])

def autocomplete_score(err_hits):
    score_card = {')':1,
                  ']':2,
                  '}':3,
                  '>':4}
    return sum([score_card[k]*err_hits[k] for k in [')',']','}','>']])
    
def stack_1(line):
    stk = []
    key = {'(':1,
           '[':2,
           '{':3,
           '<':4,
           ')':-1,
           ']':-2,
           '}':-3,
           '>':-4}

    prev = key[line[0]]
    for c in line:
        stk.append(key[c])
        #print(stk) # to see progress - cool to see waves
        if key[c]<0: # check previous - if match then remove the last two
            if abs(key[c]) == prev:
                stk = stk[:-2]
            else:
                return c
        prev = stk[-1] # last stk element

def stack_2(line):
    stk = []
    key = {'(':1,
           '[':2,
           '{':3,
           '<':4,
           ')':-1,
           ']':-2,
           '}':-3,
           '>':-4}

    prev = key[line[0]]
    for c in line:
        stk.append(key[c])
        #print(stk) # to see progress - cool to see waves
        if key[c]<0: # check previous - if match then remove the last two
            if abs(key[c]) == prev:
                stk = stk[:-2]
            else:
                return [0,0] # return true of the line is corrupted
        prev = stk[-1] # last stk element
    print(str(stk))
    return stk


main()