#!/usr/bin/python3
##CMPT 120 D100; 16-3
##Jack 'Jryzkns' Zhou
##Brian Fu
##Daniel Lee
##Final Assignment - Planets, Aliens, and Explosions

import Current #from Current.py

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

print("Welcome to Planets, Aliens, and Explosions")

##Astronaut Data:
Name=input("What's your name? ")
Position=[0] ##initiation placeholder for player
Fuel=input("how much fuel will you start with? ")   ##needs validation?
Civ=input("Please indicate your civilization level(integer from 0 to 3): ") ##needs validation to be in the interval [0,3]
Rocks=[]

#Player Data
player = [Name, Position, Fuel, Civ, Rocks]

init()
print(planets)

while True: ##main game loop
    ##Update Game board
    destination=int(input("Which Planet would you like to go to? "))    ##Validate wrt # of planets
    travel(planets[destination][2])    

if isGraphic:
    turtle.mainloop()

'''
#modifies the isPythonPlanet parameter to true, to be used at the beginning of game loop
i = int(input("Which Planet would you like to make to be the PythonPlanet?\n"))
##needs validation wrt the amount of planets present
planets[i][3]=True  ##default value in data matrix is False so we set it to True
'''