"""
Author: Carter Spenner
Date: 3/30/2026
Purpose: To practice using turtle graphics and for loops
"""

#80% code
import random
import turtle

t = turtle.Pen()
t.speed(1)

t.left(90)
t.forward(100)
t.right(45)
t.forward(50)
t.left(135)
t.backward(125)

t.circle(25)
t.color("red")
t.pensize(5)

loops1 = random.randint(3, 6)
for i in range(loops1):
    t.penup()
    t.goto(-50, -50)
    t.pendown()
    t.forward(50)
    t.right(360 / loops1)

#90% code

t.penup()
t.goto(-200, -200)
t.pendown()
t.fillcolor("green")
t.begin_fill()
t.circle(50)
t.end_fill()
t.speed(6)

loops2 = int(float(input("How many lines do you want?: ")) // 1)
for i in range(loops2):
    t.penup()
    t.goto(-300, 0)
    t.pendown()
    t.forward(100)
    t.right(360 / loops2)

turtle.bgcolor("lightblue")

turtle.done()