'''
12 May 2022
Part 1: 4147524
Part 2: 3570354

'''

import os

def main():
    input_path = 'REDACTED'
    array = [x.strip() for x in open(input_path+os.path.basename(__file__).split('.')[0]+'.txt', 'r')]
    
    # Declare
    oxy_rating = [True] * len(array)
    co2_rating = [True] * len(array)#oxy_rating
    o2_string = ''
    co2_string = ''
    gamma,eps = '',''
    
    # Go through each column
    for i in range(0,len(array[0])):
        
        # ------ Part 1
        gamma += get_common_part1(array,i,True)
        eps += get_common_part1(array,i,False)
        
        
        # ------ Part 2
        # Get the most and least common of lines
        # that haven not been eliminated for part 2
        most_com = get_common_part2(array,i,oxy_rating,True)
        least_com = get_common_part2(array,i,co2_rating,False)
        
        # go through each line
        for n,l in enumerate(array):
            if l[i] != most_com:
                oxy_rating[n] = False
            if l[i] != least_com:
                co2_rating[n] = False
        if sum(oxy_rating) == 1:
            for n in range(0,len(oxy_rating)):
                if oxy_rating[n]:
                    o2_string = array[n]
        if sum(co2_rating) == 1:
            for n in range(0,len(co2_rating)):
                if co2_rating[n]:
                    co2_string = array[n]
    print('Power Consumed: ',int(gamma,2)*int(eps,2))
    print('Life Support Rating: ',int(o2_string,2)*int(co2_string,2))

def get_common_part1(array,c,most_or_least):
    ''' Get a True for most common'''
    if sum([int(x[c]) for x in array]) > (len(array)/2):
        if most_or_least: return '1'
        return '0'
    if most_or_least: return '0'
    return '1'

def get_common_part2(array,c,rating,most_or_least):
    ''' passed a True for most, False for least '''
    s = 0
    for j in range(0,len(array)):
        if rating[j]:
            s += int(array[j][c])
    if s >= (sum(rating)/2):
        if most_or_least: return '1'
        return '0'
    if most_or_least: return '0'
    return '1'
main()