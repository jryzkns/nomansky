#!/usr/bin/python3
##CMPT 120 D100; 16-3
##Jack 'Jryzkns' Zhou
##Brian Fu
##Final Assignment - Planets, Aliens, and Explosions

#Main loop

#Level 0 (imports and base/global definitions)

#local imports
import graphics as gfx #important ones are AmazingExplosion, MildExplosion, and travel (these work regardless of gfx!)
#AE destroys planet as well and does gfx, ME is only gfx, and travel assigns a coord. as well as does gfx
import nongfx as ngfx #important is DiceRoll(num)
#DE rolls a num sided die

#import
import time
import random
import turtle

#Main matrix
planets=[] #need mutable global list to manipulate in init 
#this is where the opened file data will be stored, in syntax of the singular planets in a matrix

#Level 0.5 (define gfx data)

#Define gfx planet data
##Planet data if gfx: calculations, isPythonPlanet, coordinate position, visual data, range position
##Planet Data if not gfx: calcs, isPythonPlanet, range position
##calculations are done as [civ lvl, fuel on planet, rocks on planet]
##if civ lvl = 0 then no aliens
##this would be so much easier with objects
planet0 = [[],False,[-220,200],[50,10,5,30],0]
planet1 = [[],False,[210,110],[55,10,3,60],1]
planet2 = [[],False,[0,-200],[60,15,4,90],2]
planet3 = [[],False,[-220,-200],[35,5,6,45],3]
planet4 = [[],False,[150,-100],[40,10,8,0],4]
planet5 = [[],False,[0,-50],[25,4,10,180],5]
planet6 = [[],False,[10,100],[30,5,3,80],6]
planet7 = [[],False,[-200,-75],[30,10,4,120],7]
planet8 = [[],False,[150,200],[45,10,4,50],8]
planet9 = [[],False,[230,-200],[25,3,5,270],9]

#Define preset gfx matrix
presetplanet = [planet0,planet1,planet2,planet3,planet4,planet5,planet6,planet7,planet8,planet9]

#Level 1 (inputs and validation)

#begin validation
while True:
    try:        
        print("Welcome to Planets, Aliens, and Explosions")
        print()
        
        file = str(input("DISCLAIMER: Graphics will only be enabled for [0,10] planets\nPlease enter the full name of the UTF-8 file to import: "))
        ###needs validation to get the right file
        #try raise except this
        print()
            
        max_turns = int(input("What's the maximum number of turns?: "))
        if max_turns < 0:
            raise ValueError
        print()
        
        explosions = input("Would you like explosions? (Y/N): ")
        if explosions.lower() == 'y':
            explosions = True
        elif explosions.lower() == 'n':
            explosions = False
        else:
            raise ValueError
        print()
        
        #Player Data:
        Name=str(input("What's your name?: "))
        print()
        
        Position= 0  ##player starts at position 0
        
        Fuel=int(input("How much fuel will you start with?: "))
        if Fuel < 0:
            raise ValueError
        print()
        
        Civ=int(input("Please indicate your civilization level (0 to 3 including): "))
        if Civ not in range (0,4): #interval [0,3]
            raise ValueError
        ##needs validation to be in the interval [0,3]
        print()
        
        Rocks=[]
        
        #Init player data, in validation loop due to init
        player = [Name, Position, Fuel, Civ, Rocks]        
        
        pythonplanet = int(input("Which Planet would you like to make to be the PythonPlanet?\nPlease enter a planet that exists in your import file: "))
        #will raise IndexError if invalid
        print()
        
        graphics = input("Please indicate if you would like to see graphics or not (Y/N): ")
        #IndexError is raised in the resulting function
        print()
        
        try:
            #initialize
            gfx.init(file, pythonplanet, presetplanet, planets, player, graphics) #gfx.init loads the file regardless of gfx
            #try raise except this
        except IndexError and FileNotFoundError:
            raise ValueError        
        break
    except ValueError:
        print("Hey! Some of those value(s) were incorrect, please enter them again!")
        print()

#end validation

#run to convert matrix if not gfx
if not gfx.isGraphic:
    ngfx.init(planets)

##print(planets) #debugging
#Turn the planet calcs into ints!
ngfx.calc_str_to_int(planets)


#Level 2 (Main game loop)

dead = False
win = False

while not dead and not win: ##main game loop
    ##Update Game board
    
    #Step 1 (Check explosions)
    if explosions:
        exploding_planet = random.randrange(1,(len(planets)*5)+1)
        if exploding_planet in range (len(planets)): #Don't do the calculations if exploding_planet isn't on board!
            
            #Check for whether amazing or mild explosion
            if bool(random.getrandbits(1)):
                amazing = True
                mild = False
            else:
                amazing = False
                mild = True
            #amazing also has mild calculations, keep mild as default
            gfx.MildExplosion(planets[exploding_planet])
            '''
            for i in range(exploding_planet-1,-1,-1):
                #planets[i][0][2]
                for k in range(exploding_planet):
                    planets[k][0][2] += planets[i][0][2]
            '''
            if amazing:
                gfx.AmazingExplosion(planets[exploding_planet], planets)
                
            
        
    
    #Step 2(Movement)
    choose_dest = input("Would you like to roll dice, or choose your destination? (C/D): ")
    if choose_dest.lower() == 'c':
        choose_dest = True
    elif choose_dest.lower() == 'd':
        choose_dest = False
    else:
        print("Hey! That's not a valid choice!")
    
    if choose_dest:
        try:
            destination=int(input("Which Planet would you like to go to?: "))   # OR can be roll dice instead of input, stop with blank input with newline, put a counter to stop after so many turns ##Validate wrt # of planets #valid this with an if, if true do everything else, if false continue loop
            gfx.travel(planets[destination][2],player) #works, after trying to travel to 10th planet that doesnt exist, dies
        except ValueError and IndexError:
            print("That's not a valid planet to go to!")
    elif not choose_dest:
        roll = ngfx.DiceRoll(6)
        print("You rolled a", roll,"!")
        input() #To allow user to respond
        if gfx.isGraphic:
            destination = ngfx.a_c_l(planets,ngfx.find_pos(planets, player[1]),roll) #advance_circularly_list, workaround for jack's code
        elif not gfx.isGraphic:
            destination = ngfx.a_c_l(planets, player[2], roll)
        gfx.travel(planets[destination][2],player)
    
    #Step 3 (Aliens)
    #Empty range is False!
    if player[3] < planets[destination][0][0]: #if player is less civ than aliens
        player[2] -= random.randrange(1,player[2]+1) #lose fuel, relies on having fuel death check before looping again
        
    elif player[3] > planets[destination][0][0] and planets[destination][0][1] >= 0: #don't subtract or give fuel if no fuel left on planet, if player is more civ than aliens
        try:
            fuel_loss = random.randrange(1,planets[destination][0][1]+1)
        except ValueError:
            fuel_loss = 0 #For case of no fuel left on planet
        planets[destination][0][1] -= fuel_loss
        player[2] += fuel_loss
        
    elif player[3] == planets[destination][0][0]: #if player same civ as aliens
        try:
            player_fuel_loss = random.randrange(1, int(player[2]/2)+1)
        except ValueError:
            player_fuel_loss = random.getrandbits(1) #For 1 fuel base case (int(0.5) => 0)
        player[2] -= player_fuel_loss
    
    if player[2] > 0: #premature death check (fuel only, planet is confirmed alive)
        rock_loss = planets[destination][0][2]//3 #If planet left with 1-2 rocks, will never get (but intentional)
        planets[destination][0][2] -= rock_loss
        player[4].append(rock_loss)
        
    #Step 3.5 (After aliens gamestate check), if he isPythonPlanet he wins regardless of stranded or not
    if planets[destination][1]:
        print("Congratualations! You have reached PythonPlanet! You win!")
        win = True
    elif player[2] <= 0:
        print("Oh no! You're out of fuel! You become stranded. You lose!")
        dead = True
    '''
    #the main 3 to run
    gfx.MildExplosion(planets[destination]) #only draws, need to spread rock specimens in calc
    #gfx.AmazingExplosion(planets[1],planets) #kills the planet graphically and irl or just irl
    '''

if gfx.isGraphic: #keep in, needed to pause to be windoze friendly
    turtle.mainloop()


#at the end of the main, put a gfx.turtle.reset() after a y/n do you want to keep playing and if isGraphic gate, else do turtle.mainloop() and turtle.exitonclick() with a ty msg (only ty msg if not gfx), as well as kill the loop

'''
#modifies the isPythonPlanet parameter to true, to be used at the beginning of game loop
i = int(input("Which Planet would you like to make to be the PythonPlanet?\n"))
##needs validation wrt the amount of planets present
planets[i][3]=True  ##default value in data matrix is False so we set it to True
'''

