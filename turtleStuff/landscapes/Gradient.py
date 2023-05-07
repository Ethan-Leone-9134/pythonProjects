import turtle
import random
import math
import Shapes as shapes


def gradient(width, height, start, end, rotation):
    turtle.colormode(255)
    start = start.split(', ')
    end = end.split(', ')
    for x in range(3):
        start[x] = int(start[x])
        end[x] = int(end[x])
    tempcolor = [0, 0, 0]
    turtle.setheading(90+rotation)
    for x in range(width):
        if x/2 == math.ceil(x/2):
            turtle.setheading(90+rotation)
        else:
            turtle.setheading(270+rotation)
        for y in range(3):
            tempcolor[y] = int(start[y] - (x+1)*(start[y] - end[y])/width)
        turtle.color(tempcolor)
        turtle.forward(height)
        turtle.setheading(rotation)
        turtle.forward(1)
    turtle.penup()




def find_grads(start, end, count):
    count = count - 1
    start = start.split(', ')
    end = end.split(', ')
    for x in range(3):
        start[x] = int(start[x])
        end[x] = int(end[x])
    for x in range(3):
        start[x] = int(start[x])
        end[x] = int(end[x])
    tempcolor = [0, 0, 0]
    for x in range(count+1):
        for y in range(3):
            tempcolor[y] = int(start[y] - x*(start[y] - end[y])/count)
        print(str(tempcolor).replace("[", "").replace("]", ""))

"""
turtle.speed(0)
find_grads('110, 0, 255', '165, 120, 230', 5)
gradient(200, 100, '210, 40, 250', '25, 90, 150', 0)

turtle.hideturtle()
turtle.mainloop()
"""