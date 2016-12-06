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
    
def obtain_list_0s_1s(lst):
    res = []
    for i in lst:
        if (i % 2 == 0):
            res.append(0)
        else:
            res.append(1)
    return res

def convert_2_to_10(lst):
    res = 0
    i2 = 0 #second loop iterator
    for i in range(len(lst)-1,-1,-1): #range should be set at start of loop execution
        res += lst[i] * 2 ** i2
        del lst[i]
        i2 += 1
    return res

def rocklst(planets): #Find all the rock values and put them into a list
    rocklst = []
    for i in range(len(planets)):
        rocklst.append(planets[i][0][2])
    return rocklst

#dependencies: obtain_list_0s_1s, convert_2_to_10, rocklst
def endgame_calcs(planets):
    print("Here are the endgame calculations: ")
    rocks = rocklst(planets)
    converted_lst = obtain_list_0s_1s(rocks)
    print("The converted list of rock specimens to a binary list is:\n", converted_lst)
    binary = convert_2_to_10(converted_lst)
    print("The conversion of the binary list to base 10 is:\n", binary)

#dependency: find_pos
def updateboard(planets, player, graphics):
    '''updates the shell with pertinent game information, only contains prints'''
    print("The Galaxy:")
    ##please get the spacing right here, all the info is printed but
    ##the spacing is off
    print("Planet, AlienCiv, Fuel, Rocks, Python Planet?")
    for i in range(len(planets)):
        print("", i,"\t",planets[i][0][0],"\t  ",planets[i][0][1],"\t",planets[i][0][2],"\t",planets[i][1])
    print("The Astronaut:")
    if graphics:
        print("Name:",player[0],"\nPosition:",find_pos(planets,player[1]),"\nCurrent Fuel:",player[2],"\nCurrent Rocks:",player[4])
    else:
        print("Name:",player[0],"\nPosition:",player[1],"\nCurrent Fuel:",player[2],"\nCurrent Rocks:",player[4])
    print("The Astronaut is Alive.")
    print()

#dependency: jack's update print func
def endgame_response(dead, win, max_turns, playing, planets, player, graphics):
    if win:
        print("The game is over. You have won!")
    elif dead:
        print("The game is over. You have lost.")
    elif not max_turns: #elif max_turns count reaches 0
        print("Oh no! You have run out of turns!")
        print("You were too slow in your quest. You have lost.")
    print()    
    print("Death Recap")
    print()
    updateboard(planets, player, graphics)
    while True:
        keep_playing = str(input("Play Again? (Y/N): "))
        if keep_playing.lower() == 'y':
            return True
        elif keep_playing.lower() == 'n':
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