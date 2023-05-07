import turtle
import math

turtle.width(10)
turtle.speed(10)

def draw_United(points, length, circle):
    if (points/2) == round(points/2):
        print("Error")
    turtle.pendown()
    turtle.left((90/points)*(points-1))
    midright = math.ceil(points/2)
    angle = ((midright-1) * (360/points))
    for x in range(points):
        turtle.right(angle)
        turtle.forward(length)

    if circle == 1:
        angle = math.pi/180 * 2 * (180-angle)
        circrad = 2 * (math.sin(angle/2)*length)/math.sin(angle)
        circrad = (length+circrad+length)/3
        turtle.setheading(180)
        turtle.circle(circrad/2)


def move(direction, factor):
    if direction == "U":
        turtle.penup()
        turtle.setheading(90)
        turtle.forward(factor)
        turtle.right(90)
    if direction == "D":
        turtle.penup()
        turtle.setheading(270)
        turtle.forward(factor)
        turtle.right(270)
    if direction == "L":
        turtle.penup()
        turtle.setheading(180)
        turtle.forward(200)
        turtle.right(180)
    if direction == "R":
        turtle.penup()
        turtle.setheading(0)
        turtle.forward(200)
        turtle.right(0)


move("R", 300)
draw_United(5, 200, 1)
move("L", 300)
draw_United(7, 200, 1)
move("L", 300)
draw_United(9, 200, 1)
move("U", 200)
draw_United(11, 200, 1)
move("R", 300)
draw_United(15, 200, 1)

turtle.hideturtle()
turtle.mainloop()