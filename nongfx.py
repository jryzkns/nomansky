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

def calc_str_to_int(planets): #Turn the planet calc data inside the processed matricies from strs to ints
    for i in range(len(planets)):
        for k in range(len(planets[i][0])): #3 pieces by default
            planets[i][0][k] = int(planets[i][0][k])
    #void, relies on global vars
    
#explosion_rock_calc dependency, god bless jack
def listmod(ls):
    resls=[]
    for i in range(len(ls)):
        sum=0
        for num in ls:
            sum += num
        ls.remove(ls[0])
        resls.append(sum)
    return resls

#Dependency: listmod
def explosion_rock_calc(exploding_planet, planets):
    rocklst = []
    for i in range(1,exploding_planet): 
        rocklst.append(planets[i][0][2])
    modded_rocklst = listmod(rocklst)
    for i in range(len(modded_rocklst)):
        planets[i][0][2] = modded_rocklst[i]
    #void    

def endgame_response(dead, win, max_turns, playing):
    if win:
        print("The game is over. You have won!")
    elif dead:
        print("The game is over. You have lost.")
    elif not max_turns: #elif max_turns count reaches 0
        print("Oh no! You have run out of turns!")
        print("You were too slow in your quest. You have lost.")
    while True:
        keep_playing = input("Play Again? (Y/N): ")
        if keep_playing.lower == 'y':
            return True
        elif keep_playing.lower == 'n':
            return False
            
'''
def ar_init(planets, graphics): #aliens and rocks appender to main planets matrix
    #print(graphics)
    a_it = [] 
    for i in range(len(planets)):    
        bool(random.getrandbits(1))
        
def explosion_rock_calc(planets[exploding_planet], planets):
    for i in range(exploding_planet-1,-1,-1):   
        #planets[i][0][2] [0][2] [0][2]
        for k in range(exploding_planet):
            planets[k] += planets[i]
            print(planets)
            
planets = [10,20,30]
#explosion_rock_calc(2
'''