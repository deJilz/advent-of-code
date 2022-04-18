# (too high) 10523530073843451431989812761889427748315060377514743190088032175115508218519014832781113204068606422665675868825947237075188341925955228892694994612140700728587886621614384956677153290981864156959280032146697722339582487655556965542857840127097369321162246896252908553631339566497802369008374722956315672638518971265626956095834241986376684200442748517268013478804201853089921903381187795691961647211407360363218573440223171993210801325347813437184443425

import os
from progress.bar import IncrementalBar


def main():
    # import the txt file into an array - it will use the py file name
    input_path = 'C://Users//cdejo//Desktop//Coding//PythonPrograms//AdventOfCode//2021//inputs//'
    arry = [x for x in open(input_path+'day06_mini.txt', 'r')]
    
    arry = arry[0].split(",")
    arry = [int(x) for x in arry] # int array of inital ages
    
    # Initialize variables
    DURATION = 80
    population = len(arry)
    bar = IncrementalBar('Processing',max=population) # n is loop duration
    
    n = 0
    # main loop
    for i in arry:
        #population = population + bloodline(i,DURATION,0) #0 or 1?? is this the first child?
        bar.next()
        population = population + family_tree(i,DURATION)
        
    bar.finish()
    print("After " + str(DURATION) + " days, the population is " + str(population))
    
def family_tree(age, DURATION):
    if DURATION < age:
        return 1
    k = 0
    for c in range(age,DURATION,6):
        k = k + family_tree(age+8,DURATION)
    return k

def bloodline(age, DURATION, chil):
    # if there is not enough time to reproduce, return 1
    if DURATION < age:
        return 1
    
    # set reproductive info
    life = DURATION - age
    life_cycle = 6
    if chil == 0:
        life_cycle = 8
    
    return bloodline(life_cycle+(chil*6),DURATION,chil+1)
    # run a while loop until no more children can be produced
    # k = 0
    # while ((chil+1)*6 < life):
        # k = k + bloodline(age+life_cyle,True,chil)
        # chil = chil + 1
    # return k
    
    
# def bloodline(age, DURATION,new_mom):
    # k = 0
    # life = DURATION - age
    # life_cyle = 6
    # if new_mom:
        # life_cyle = 8
    
    # # if the DURATION happens before the life cycle - return 1
    

    # # while the returned sum * 6 is less than life 
        # # run bloodline again
    # while (k*6 < life):
        # k = k + bloodline(age+life_cyle,DURATION,False) + 1
    # return k    
    
    

main()