import turtle
import random

def quasirecursive_planet(t, length, decrement, n, recurse_angle):
    t.rt(random.randint(1,359))
    recursing = True
    color="#"+str(random.randint(555555,999999))
    t.color("black",color)
    while recursing == True:
        if length <= 0:
            recursing = False
        else:            
            t.begin_fill()
            for i in range(n):
                t.fd(length)
                t.rt(360/n)         #360/n makes sure that the turning number of shape is 0
            t.end_fill()
        t.rt(recurse_angle)
        length=length-decrement
    return