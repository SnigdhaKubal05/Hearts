"""
import turtle
import math
import random

screen = turtle.Screen()
screen.bgcolor("black")

t=turtle.Turtle()

t.speed(1)
t.hideturtle()
t.pensize(1)
colors=["red","blue","lime","yellow","cyan","magenta","orange","pink"]

for i in range(120):
    t.penup()
    t.goto(0,40)

    angle = i*(math.pi*2)/120
    
    x = 16 * (math.sin(angle) ** 3) * 15

    y = (13 * math.cos(angle) - 5 * math.cos(2 *angle) - 2 * math.cos(3 * angle) - math.cos(4 * angle)) * 15

    c=random.choice(colors)

    t.color(c)
    t.pendown()
    t.goto(x,y)

    for scale in range(8):
        t.forward(6)
        t.backward(6)
        t.right(45)
        turtle.done()   

"""


import turtle
import math

screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(1)
t.hideturtle()
t.penup()
t.color("#ffb6c1")

for scale in range(11, 17):
    for i in range(120):
        angle = i * (math.pi * 2) / 120

        x = 16 * (math.sin(angle) ** 3) * scale

        y = (13 * math.cos(angle)
             - 5 * math.cos(2 * angle)
             - 2 * math.cos(3 * angle)
             - math.cos(4 * angle)) * scale

        t.goto(x, y)
        t.write("I love you",
                align="center",
                font=("Arial", 8, "bold"))

turtle.done()