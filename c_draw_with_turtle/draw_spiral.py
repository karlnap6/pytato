import turtle
import random

wn=turtle.Screen()
wn.setup(800,600)
#wn.bgcolor(“white”)
s=turtle.Turtle()

def draw_cir(r=10, size=50, speed=0):
    for i in range(size):
        s.speed(speed)
        s.circle(r+i,45)
        j=random.random()
        k=random.random()
        l=random.random()
        s.pencolor((j,k,l))
    s.penup()
    s.home()
    s.pendown()

def draw_left_cir(r=10, speed=1):
    for i in range(10):
        s.speed(speed)
        s.circle(r*i)
        s.penup()
        s.sety(r*i*-1)
        s.setx(r*i*-1)
        s.pendown()
        j=random.random()
        k=random.random()
        l=random.random()
        s.pencolor((j,k,l))
    s.penup()
    s.home()
    s.pendown()

def draw_right_cir(r=10, speed=1):
    for i in range(10):
        s.speed(speed)
        s.circle(r*i)
        s.penup()
        s.setx(r*i)
        s.sety(r*i*-1)
        s.pendown()
        j=random.random()
        k=random.random()
        l=random.random()
        s.pencolor((j,k,l))

draw_left_cir()
draw_right_cir()
s.hideturtle()
turtle.done()