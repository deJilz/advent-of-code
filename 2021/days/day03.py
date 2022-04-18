# Connor DeJohn - 17 April 2022

import os

def main():
    # import txt file with the name of py file
    # array of inputs of form: b'01110110111'
    data = [x[:-2].encode('ascii') for x in open('C://Users//cdejo//Desktop//Coding//PythonPrograms//AdventOfCode//2021//inputs//'+os.path.basename(__file__).split('.')[0]+'.txt','r')]
    
    # Setup
    maxL = len(data[0])
    q = 0
    g = ''
    
    # testing
    print (data[0][2])
    
    # loop through each character space
    for n in range(0,maxL-1):
        #print ("Line " + str(n))
        for i in data:
            # i is a byte object
            # if the first digit in the byte object is 1
            #if n ==1:
            #    print(bin(i[2]))
            if i[n] == 1:
                q = q+1
        if q > maxL:
            g = g + '1'
        else:
            g = g + '0'
        #print (q)
        q = 0
    
    print (g)
    # Calculate results
    #gamma = g.encode('ascii')
    #eps = invertBinary()#.encode('ascii'))
    #pwr = gamma * eps
    
    #Print results
    #print("The Gamma rate is " + str(gamma))
    #print("The epsilon rate is " + str(eps)
    #print("The power consumption is ") + str(pwr))

    
    
def invertBinary(rst):
    ''' Return the inverted binary '''
    #print(rst)
    return (bin(~rst)[3:]) # removes the before stuff

def binaryToInt(bina):
    ''' Passed a bin and converts to int '''
    return int(bina,2)
    
#def intToBinary():

main()