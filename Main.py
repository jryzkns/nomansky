#!/usr/bin/python3
##CMPT 120 D100; 16-3
##Jack 'Jryzkns' Zhou
##Brian Fu
##Final Assignment - Planets, Aliens, and Explosions

#Main loop

#local imports
import graphics as gfx
import nongfx as ngfx

#import
import time
import random
import turtle

#Define data
##Planet data: calculations,position,visual,isPythonPlanet 
planet0 = [[],False,[-220,200],[50,10,5,30]]
planet1 = [[],False,[210,110],[55,10,3,60]]
planet2 = [[],False,[0,-200],[60,15,4,90]]
planet3 = [[],False,[-220,-200],[35,5,6,45]]
planet4 = [[],False,[150,-100],[40,10,8,0]]
planet5 = [[],False,[0,-50],[25,4,10,180]]
planet6 = [[],False,[10,100],[30,5,3,80]]
planet7 = [[],False,[-200,-75],[30,10,4,120]]
planet8 = [[],False,[150,200],[45,10,4,50]]
planet9 = [[],False,[230,-200],[25,3,5,270]]

#Define main matrix
presetplanet = [planet0,planet1,planet2,planet3,planet4,planet5,planet6,planet7,planet8,planet9]

planets=[] #need mutable global list to manipulate in init 
#this is where the opened file data is stored, in syntax of the singular planets in a matrix

print("Welcome to Planets, Aliens, and Explosions")

#Astronaut Data:
Name=input("What's your name? ")
Position=[0] ##initiation placeholder for player
Fuel=input("how much fuel will you start with? ")   ##needs validation?
Civ=input("Please indicate your civilization level(integer from 0 to 3): ") ##needs validation to be in the interval [0,3]
Rocks=[]

#Player Data
player = [Name, Position, Fuel, Civ, Rocks]

#begin validation

file = str(input("Please enter the name of the txt file to import.\nPlease remember to type .txt after the file\nDISCLAIMER:In order for the grapics mode to function properly, \nplease import a maximum of ten planets\nelse, graphics will be automatically cancelled\nNow Please enter the filename: "))
    ###needs validation to get the right file
    #try raise except this, put all validation in a huge while loop

pythonplanet = int(input("Which Planet would you like to make to be the PythonPlanet?"))
##needs validation wrt the amount of planets present

graphics = input("Pleaes indicate if you would like to see graphics or not(y/n):")
##needs validation so it only takes "y","Y","n", or "N" (need to put .lower() in the validation loop to check)

#end validation

#initialize
gfx.init(file, pythonplanet,presetplanet, planets,player, graphics)

#print(planets) #debugging

while True: ##main game loop
    ##Update Game board
    destination=int(input("Which Planet would you like to go to? "))    ##Validate wrt # of planets
    gfx.MildExplosion(planets[1])
    gfx.AmazingExplosion(planets[1],planets)
    gfx.travel(planets[destination][2],player) #works, after trying to travel to 10th planet that doesnt exist, dies

if isGraphic: #keep in, needed to pause to be windoze friendly
    turtle.mainloop()

'''
#modifies the isPythonPlanet parameter to true, to be used at the beginning of game loop
i = int(input("Which Planet would you like to make to be the PythonPlanet?\n"))
##needs validation wrt the amount of planets present
planets[i][3]=True  ##default value in data matrix is False so we set it to True
'''

