import turtle
import math

def drawFractalLine(t, distance, angle, level):
    if level == 0:
        t.setheading(angle)
        t.forward(distance)
    else:
        drawFractalLine(t, distance / 3, angle, level - 1)
        drawFractalLine(t, distance / 3, angle + 60, level - 1)
        drawFractalLine(t, distance / 3, angle - 60, level - 1)
        drawFractalLine(t, distance / 3, angle, level - 1)

def drawKochSnowflake(t, distance, level):
    angles = [0, -120, 120]
    startPosition = t.position()
    for angle in angles:
        drawFractalLine(t, distance, angle, level)
        t.setheading(angle + 120)
    t.penup()
    t.setpos(startPosition)
    t.pendown()

def main():
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.penup()
    t.goto(-100, 60)
    t.pendown()
    drawKochSnowflake(t, 200, 2)


if __name__ == '__main__':
    main()
