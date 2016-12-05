#!/usr/bin/python3
##CMPT 120 D100; 16-3
##Jack 'Jryzkns' Zhou
##Brian Fu
##Final Assignment - Planets, Aliens, and Explosions

#Non-graphical functions

#Have to import due to separate file
import random 

def DiceRoll(num): #takes an int as the upper bound
    '''rolls a dice, nuff said'''
    return(random.randint(1,num))

def init(planets): #run after the gfx.init (through an if gate), converts the result from gfx into useable non-gfx results (so that gfx.travel runs correctly)
    for i in range (10):
        for k in range(3):
            planets[i].pop()
    #print(len(planets))
    for i in range (0,len(planets)):
        planets[i].append(i)
        
        
def a_c_l(lst,pos,adv): #advance_circularly_list
    #iterator = 0
    
    if pos >= len(lst):
        return -1
    
    for i in range (adv):
        if pos >= len(lst)-1:
            pos = 0
            #print(pos)
        else:    
            pos += 1
            #print(pos)
    
    return pos


def find_pos(matrix, find_value): #workaround for jack's code
    for i in range(len(matrix)):
        for k in matrix[i]:
            if k == find_value:
                return i

'''
def ar_init(planets, graphics): #aliens and rocks appender to main planets matrix
    #print(graphics)
    a_it = [] 
    for i in range(len(planets)):    
        bool(random.getrandbits(1))
'''
        
    