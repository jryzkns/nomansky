##CMPT 120 D100; 16-3
##Jack 'Jryzkns' Zhou
##Brian Fu
##Daniel Lee
##Final Assignment- Turtle test

##functional definitions
def randomstar(t):
    '''draws a star with varied orientation and varied size'''
    length=random.randint(5,15)
    t.lt(random.randint(0,359))
    for i in range(5):      ##core star drawing script
        t.fd(length)
        t.rt(144)
def randmove(t):
    '''used to move turtle in random places'''
    t.pu()      ##just so turtle doesn't leave a mark on its way home
    t.rt(random.randint(0,359))         ##turns some random direction
    t.fd(random.randint(100,200))    ##teleports some distance away
    t.pd()      ##just so turtle doesn't leave a mark on its way home
def home(t):
    '''returns the turtle back to origin'''
    t.pu()      ##just so turtle doesn't leave a mark on its way home
    t.home()
    t.pd()      ##just so turtle doesn't leave a mark on its way home
def defaulttitle():
    '''returns the screen title to the title of the game'''
    time.sleep(3)
    turtle.title("Planets, Aliens, Explosions.")
def quasirecursive_planet(t, length, decrement, n, recurse_angle):
    
    t.rt(random.randint(1,359))
    recursing = True
    while recursing == True:
        if length <= 0:
            recursing = False
        else:
            color="#"+str(random.randint(555555,999999))
            t.color("black",color)            
            t.begin_fill()
            for i in range(n):
                t.fd(length)
                t.rt(360/n)         #360/n makes sure that the turning number of shape is 0
            t.end_fill()
        t.rt(recurse_angle)
        length=length-decrement
    return
def ScreenFlash():
    '''screen flashes, potentially used for amazing explosions'''
    for i in range(5):
        turtle.bgcolor("#FF0000")
        time.sleep(0.1)
        turtle.bgcolor("#FFFFAA")
    time.sleep(0.5)
    turtle.bgcolor("#FFFFFF")
    time.sleep(0.25)
    turtle.bgcolor("#000000")
def wipeplanet(t,planetdata):
    t.color("black","black")
    t.pen(shown = False)
    t.pu()
    t.setpos(int(planetdata[0]),int(planetdata[1]))
    t.pd()
    t.rt(90)
    t.fd(100)
    t.lt(90)
    t.begin_fill()
    t.circle(150)
    t.end_fill()
def astronauttravel(astronaut, planet):
    astronaut.goto(planet[0],planet[1])

##Event Functions
def backdropinit():
    stars=[]
    for i in range(5):                  ##initiate stars
        stars.append(turtle.Turtle())  
    for star in stars:
        star.color("#FFFFEE")
        star.pen(shown = False)
    for i in range(5):
        for star in stars:
            randmove(star)
            randomstar(star)
def planetinit(planetdatalist):               ##don't draw any planets with size > 100!
    planet = turtle.Turtle()
    planet.pen(shown = False)
    planet.pensize(5)
    for i in range(len(planetdatalist)):
        planet.pu()
        planet.setpos(planetdatalist[i][0],planetdatalist[i][1])
        planet.pd()
        quasirecursive_planet(planet, planetdatalist[i][2],planetdatalist[i][3], planetdatalist[i][4], planetdatalist[i][5])
        home(planet)
def AmazingExplosion(boomplanet):
    turtle.title("Amazing Explosion!!")
    ScreenFlash()                           ##to emulate an explosion
    eraser=turtle.Turtle()
    wipeplanet(eraser,boomplanet)           ##covers the physical drawing of the planet
    planetdatalist.remove(boomplanet)       ##destroys the planet data
    turtle.title("A planet has been destroyed!")    ##why dont this work???
    home(eraser)
    defaulttitle()
def astronautinit(astronaut):
    '''initiaalizes the astronaut variable, and puts the astronaut onto home planet'''
    astronaut.pu()
    astronauttravel(astronaut, planetdata1)
    astronaut.pd()
    astronaut.speed(1)
    astronaut.color("#DCDCDC")
    astronaut.pensize(10)
def init(planetdatalist,astronaut):
    turtle.bgcolor("#010001")
    turtle.title("Loading...")
    backdropinit()
    planetinit(planetdatalist)
    astronautinit(astronaut)
    defaulttitle()
    
import turtle   ##reference link https://docs.python.org/3.5/library/turtle.html
import random
import time

##TOP LEVEL##

##planetdatax = [x-position,y-position,lengthsize,decrementsize,number of sides, recurse-angle]##
##other items in the list: civilization level, isPythonPlanet, fuel, rock
planetdata1 = [-220,200,50,10,5,30]             #######sort out data structure
planetdata2 = [210,110,55,10,3,60]
planetdata3 = [0,-200,60,20,4,90]
planetdata4 = [-220,-200,35,5,6,45]
planetdata5 = [150,-100,40,10,8,0]
planetdata6 = [0,-50,25,4,10,180]
planetdata7 = [10, 100, 30, 5, 3, 80]
planetdatalist = [planetdata1,planetdata2,planetdata3,planetdata4,planetdata5,planetdata6, planetdata7]


astronaut=turtle.Turtle()



init(planetdatalist,astronaut)

#astronauttravel(astronaut, planetdata7)
#astronauttravel(astronaut, planetdata5)
#astronauttravel(astronaut, planetdata1)

turtle.mainloop()