# irisryz

import turtle
import random


s = turtle.Screen()
s.setup(600,640)
t = turtle.Turtle()
s.bgcolor("black")


shape = ["arrow", "turtle", "circle", "square", "triangle","classic"]
colors = ['violet', "deepskyblue","thistle","pink","cyan",
        "aquamarine","springgreen", "lightgreen","palevioletred","tomato","steelblue"]
blueColors = ["deepskyblue","lightskyblue","dodgerblue","midnightblue","navy", "royalblue"]
pinkColors = ["pink","indianred","crimson","magenta","violet",
                "mistyrose","lavenderblush","palevioletred"]


t.pensize(2)
angle = 35
t.speed(0)


def drawGalaxy(color_list):
    #1st stamp
    t.stamp()
    for length in range(5, 160, 1):    
     
        t.forward(length)
        t.right(angle)
        t.shape(random.choice(shape))
        t.color(random.choice(color_list))
        t.stamp()


typeOfGalaxy = input("would you like a blue, pink, or random galaxy?")
 
if(typeOfGalaxy.lower() == "blue") :
    drawGalaxy(blueColors)
elif (typeOfGalaxy.lower() == "pink") :
    drawGalaxy(pinkColors)
else:
    drawGalaxy(colors)    
     


