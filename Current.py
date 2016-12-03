##CMPT 120 D100; 16-3
##Jack 'Jryzkns' Zhou
##Brian Fu
##Daniel Lee
##Final Assignment - Planets, Aliens, and Explosions

##functional definitions
def loadfile():
    '''loads the file to be read''' 
    #file = str(input("Please enter the name of the txt file to import.\nPlease remember to type .txt after the file\nDISCLAIMER:In order for the grapics mode to function properly, \nplease import a maximum of ten planets\nelse, graphics will be automatically cancelled\nNow Please enter the filename: "))
    ###needs validation to get the right file
    fileRef = open("planetsData1.txt","r")
    stringlist=[]
    global planetcount
    planetcount = 0
    for line in fileRef:
        print(line)
        string = line[0:len(line)-1] ##temporarily taking away the dashes
        stringlist.append(string)
        planetcount +=1
    fileRef.close()
    datalist=[]
    for line in stringlist:
        datalist.append(line.split("-"))
    for line in datalist:
        for dig in line:
            dig = int(dig)
    for q in range(len(datalist)):  ##q is an arbitraily assigned counter
        presetplanet[q][0].extend(datalist[q])
        datalist.remove(datalist[q])
        planets.append(presetplanet[q])
    for extra in datalist:  
        planets.append(datalist[extra])
def setPythonPlanet():
    '''modifies the isPythonPlanet parameter to true, to be used at the beginning of game loop'''
    i = int(input("Which Planet would you like to make to be the PythonPlanet?\n"))
    ##needs validation wrt the amount of planets present
    planets[i][3]=True  ##default value in data matrix is False so we set it to True
def isGraphic():
    '''asks user to confirm graphics'''
    graphics = input("Pleaes indicate if you would like to see graphics or not(y/n):")
    ##needs validation so it only takes "y","Y","n", or "N"
    if graphics == "y":
        return True
    else:
        return False
def randomstar(t):
    '''draws a star with varied orientation and varied size'''
    ##doesn't run if no graphics are open
    length=random.randint(5,15)
    t.lt(random.randint(0,359))
    for i in range(5):      ##core star drawing script
        t.fd(length)
        t.rt(144)
def randmove(t):
    '''used to move turtle in random places'''
    ##doesn't run if no graphics are open
    t.pu()      
    t.rt(random.randint(0,359))         ##turns some random direction
    t.fd(random.randint(100,200))    ##teleports some distance away
    t.pd()     
def home(t):
    '''returns the turtle back to origin'''
    ##doesn't run if no graphics are open
    t.pu()     
    t.home()
    t.pd()  
def defaulttitle():
    '''returns the screen title to the title of the game'''
    ##doesn't run if no graphics are open
    time.sleep(3)
    turtle.title("Planets, Aliens, Explosions.")
def drawquasirecursive_planet(t,planet):
    '''length, decrement, n, recurse_angle'''
    ##doesn't run if no graphics are open
    t.rt(random.randint(1,359))
    recursing = True
    length = int(planet[0])
    while recursing == True:    ##dont use recursion and while loop together
        if length <= 0:
            recursing = False
        else:
            color="#"+str(random.randint(555555,999999))
            t.color("black",color)            
            t.begin_fill()
            for i in range(planet[2]):
                t.fd(length)
                t.rt(360/planet[2])#360/n makes sure that the turning number of shape is 0
            t.end_fill()
        t.rt(planet[3])
        length-=planet[1]
    return
def ScreenFlash():
    '''screen flashes, potentially used for amazing explosions'''
    ##doesn't run if no graphics are open
    for i in range(5):
        turtle.bgcolor("#FF0000")   ##red
        time.sleep(0.1)
        turtle.bgcolor("#FFFFAA")   ##yellow
    time.sleep(0.5)
    turtle.bgcolor("#FFFFFF")       ##white
    time.sleep(0.25)
    turtle.bgcolor("#000000")       ##back to black
def wipeplanet(t,planet):
    '''draws a black circle to cover up a planet'''
    ##doesn't run if no graphics are open
    t.color("black","black")
    t.pen(shown = False)
    t.pu()
    t.setpos(planet[1][0],planet[1][1]) ##goes to the centre of the planet
    t.pd()
    t.rt(90)
    t.fd(70)    ##goes below the planet
    t.lt(90)
    t.begin_fill()
    t.circle(100)   ##draws over the planet
    t.end_fill()
def debris(planet):
    '''emulates debris flying around the planet'''
    ##doesn't run if no graphics are open
    stone=turtle.Turtle()
    stone.pen(shown=False)
    stone.pu()
    stone.speed(0)
    stone.setpos(planet[1][0],planet[1][1])     ##goes to the centre of the planet
    for i in range(5):  ##makes debris here
        stone.rt(random.randint(0,180))
        stone.fd(random.randint(50,75))
        stone.pd()
        color="#"+str(random.randint(555555,999999))
        stone.color("black",color)            
        stone.begin_fill()        
        stone.circle(5)
        stone.end_fill()
        stone.pu()
        stone.setpos(planet[1][0],planet[1][1])
def travel(coordinate):
    '''receives call from the coordinate list, which is planets[...][0]'''
    player[1] = coordinate   ##the player's position is now the planet's position    
    if isGraphic:
        astronaut.goto(coordinate[0],coordinate[1])
def DiceRoll():
    '''rolls a dice, nuff said'''
    return(random.randint(1,6))
##Event Functions
def playermove():
    destination=int(input("Which Planet would you like to go to? "))    ##Validate wrt # of planets
    travel(planets[destination][1])
def backdropinit():
    ##doesn't run if no graphics are open
    stars=[]
    for i in range(5):                  ##initiate stars
        stars.append(turtle.Turtle())  
    for star in stars:
        star.color("#FFFFEE")
        star.speed(0)
        star.pen(shown = False)
    for i in range(4):
        for star in stars:
            randmove(star)
            randomstar(star)
def planetinit(planets):
    ##doesn't run if no graphics are open
    drawer = turtle.Turtle()
    drawer.speed(0)
    drawer.pen(shown = False)
    drawer.pensize(3)
    for i in range(len(planets)):
        drawer.pu()
        drawer.setpos(planets[i][1][0],planets[i][1][1])
        drawer.pd()
        drawquasirecursive_planet(drawer,planets[i][2])
        home(drawer)
def MildExplosion(boomplanet):
    '''takes in planets[...]'''
    print("An Explosion has happened!")
    ##rocks spread out to nearby planets
    ##check if player is on planet    
    if isGraphic:
        turtle.title("An Explosion has happened!")
        ScreenFlash()       ##Aesthetic :^)
        debris(boomplanet)  ##Aesthetic :^)
        defaulttitle()
def AmazingExplosion(boomplanet):
    '''takes in planets[...]'''
    print("Amazing Explosion!!")
    planets.remove(boomplanet)       ##destroys the planet data
    ##rocks spread out to nearby planets
    ##check if player is on planet    
    if isGraphic:
        turtle.title("Amazing Explosion!!")
        ScreenFlash()       ##Aesthetic :^)
        eraser=turtle.Turtle()
        eraser.speed(0)
        wipeplanet(eraser,boomplanet)   ##planet MIA
        turtle.title("A planet has been destroyed!")
        home(eraser)        ##placeholder for something to happen before changing titles
        defaulttitle()
def astronautinit():
    '''initializes the astronaut variable, and puts the astronaut onto home planet'''
    global astronaut
    astronaut=turtle.Turtle()    
    astronaut.pu()
    travel(planets[0][1])
    astronaut.pd()
    astronaut.speed(1)
    astronaut.color("#DCDCDC")
    astronaut.pensize(10)
def init():
    '''initiatizes everything'''
    loadfile()
    setPythonPlanet()
    global isGraphic
    if planetcount > 10:
        isGraphic = False
    else:
        isGraphic=isGraphic()
    if isGraphic:
        turtle.bgcolor("#010001")
        turtle.title("Loading...")
        backdropinit()
        planetinit(planets)
        defaulttitle()
        astronautinit()
        
import turtle   ##reference link https://docs.python.org/3.5/library/turtle.html
import random
import time     ##only used for delays in flashing screen

##TOP LEVEL##

print("Welcome to Planets, Aliens, and Explosions")

##Planet data: calculations,position,visual,isPythonPlanet 
planet0 = [[],[-220,200],[50,10,5,30],False]
planet1 = [[],[210,110],[55,10,3,60],False]
planet2 = [[],[0,-200],[60,15,4,90],False]
planet3 = [[],[-220,-200],[35,5,6,45],False]
planet4 = [[],[150,-100],[40,10,8,0],False]
planet5 = [[],[0,-50],[25,4,10,180],False]
planet6 = [[],[10,100],[30,5,3,80],False]
planet7 = [[],[-200,-75],[30,10,4,120],False]
planet8 = [[],[150,200],[45,10,4,50],False]
planet9 = [[],[230,-200],[25,3,5,270],False]
presetplanet = [planet0,planet1,planet2,planet3,planet4,planet5,planet6,planet7,planet8,planet9]

planets=[]

##Astronaut Data:
Name=input("What's your name? ")
Position=[0] ##initiation placeholder for player
Fuel=input("how much fuel will you start with? ")   ##needs validation?
Civ=input("Please indicate your civilization level(integer from 0 to 3): ") ##needs validation to be in the interval [0,3]
Rocks=[]
player = [Name, Position, Fuel, Civ, Rocks]

init()
print(planets)

while True: ##main game loop
    ##Update Game board
    playermove()
    
if isGraphic:
    turtle.mainloop()
    
    ##commit
    ##kek
