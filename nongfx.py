#!/usr/bin/python3
##CMPT 120 D100; 16-3
##Jack 'Jryzkns' Zhou
##Brian Fu
##Final Assignment - Planets, Aliens, and Explosions

#Non-graphical functions

def DiceRoll(num): #takes an int as the upper bound
    '''rolls a dice, nuff said'''
    return(random.randint(1,num))

def init(planets): #run after the gfx.init (through an if gate), converts the result from gfx into useable non-gfx results (so that gfx.travel runs correctly)
    for i in range (10):
        for k in range(2):
            planets[i].pop()
    print(len(planets))
    for i in range (0,len(planets)):
        planets[i].append(i)
        
    