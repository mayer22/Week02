# -*- coding: utf-8 -*-
"""
Computing pi by simulating darts at a quarter of a unit circle

@author: Brian Mayer
"""

import math
import turtle
import random


def showMontePi(numDarts):
    wn = turtle.Screen()
    drawingT = turtle.Turtle()
   
    wn.setworldcoordinates(-0.5, -0.5, 1.5, 1.5)
   
    drawingT.up()
    drawingT.goto(-1, 0)
    drawingT.down()
    drawingT.goto(1, 0)
   
    drawingT.up()
    drawingT.goto(0, 1)
    drawingT.down()
    drawingT.goto(0, -1)
   
    inCircle = 0
    drawingT.up()

    for i in range(numDarts):
        x = random.random()
        y = random.random()

        distance = math.sqrt(x**2 + y**2)

        drawingT.goto(x, y)
       
        if distance <= 1:
            inCircle = inCircle + 1
            drawingT.color("blue")
        else:
            drawingT.color("red")
           
        drawingT.dot()


        pi = inCircle / (i+1) * 4
        print(pi)
    
    
    turtle.done()
    wn.exitonclick()
   
    return pi

print("\nMonte Carlo outputs")
showMontePi(10000)
