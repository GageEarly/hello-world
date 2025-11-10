from turtle import Turtle
import math

def drawCircle(t, x, y, radius):
    t.up()
    t.setposition(x, y)
    t.forward(radius)
    t.left(90)
    t.down()
    dist = ((2 * math.pi * radius) / 120)
    i = 0
    while i<= 120:
        t.left(3)
        t.forward(dist)
        i += 1

def  main():
    t = Turtle()
    x = 50
    y = 75
    radius = 100
    drawCircle(t, x, y, radius)

if __name__ == "__main__":
    main()
