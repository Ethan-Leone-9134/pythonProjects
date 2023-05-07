import turtle
import math

# Function List for turtle to draw basic shapes
# triangle - Creates a scalene triangle with 3 side lengths
# iso_triangle - Creates an isoceles triangle with a base and height
# rect - Creates a rectangle with length and width
# parallel - Creates a parallelogram with length, with and the acute angle in degrees
# polygon - Creates an equilateral polygon with sides and length

# Notes for function list
# Color - Applies to pen and will fill the shape in with that color
# Rotation - Rotates the shape counterclockwise
# Squares and rhombuses can be made using rect and parallel with length and width set equal


def triangle(left, base, right, color, rotation):
    if left + right <= base:
        print('Sum of the sides of triangle cannot be larger than base.')
        return
    semi = (left+base+right)/2
    area = math.sqrt(semi*(semi-left)*(semi-base)*(semi-right))
    height = (2*area)/base
    left_angle = math.degrees(math.acos(height/left))
    right_angle = math.degrees(math.asin(height/right))
    turtle.pendown()# Format turtle
    if ',' in color:
        turtle.colormode(255)
        color = color.split(', ')
        for x in range(3):
            color[x] = int(color[x])
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.setheading(rotation-90-left_angle)  # Left line
    turtle.forward(left)
    turtle.setheading(rotation)  # Bottom line
    turtle.forward(base)
    turtle.setheading(rotation+180-right_angle)  # Right line
    turtle.forward(right)
    turtle.end_fill()
    turtle.penup()


def iso_triangle(base, height, color, rotation):
    top_angle = math.degrees(math.atan(base/(2*height)))
    side_len = math.sqrt((height ** 2) + (base / 2) ** 2)
    turtle.pendown()
    turtle.setheading(0+rotation)  # Format turtle
    if ',' in color:
        turtle.colormode(255)
        color = color.split(', ')
        for x in range(3):
            color[x] = int(color[x])
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.right(90+top_angle)  # Left line
    turtle.forward(side_len)
    turtle.setheading(0+rotation)  # Bottom line
    turtle.forward(base)
    turtle.left(90+top_angle)  # Right line
    turtle.forward(side_len)
    turtle.end_fill()
    turtle.penup()


def rect(length, height, color, rotation):
    turtle.pendown()
    turtle.setheading(180+rotation)  # Format turtle
    if ',' in color:
        turtle.colormode(255)
        color = color.split(', ')
        for x in range(3):
            color[x] = int(color[x])
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.end_fill()
    turtle.penup()


def parallel(height, length, angle, color, rotation):
    acute = angle
    obtuse = 180 - angle
    turtle.pendown()
    turtle.setheading(0+rotation)  # Format turtle
    if ',' in color:
        turtle.colormode(255)
        color = color.split(', ')
        for x in range(3):
            color[x] = int(color[x])
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.forward(length)
    turtle.left(acute)
    turtle.forward(height)
    turtle.left(obtuse)
    turtle.forward(length)
    turtle.left(acute)
    turtle.forward(height)
    turtle.left(obtuse)
    turtle.end_fill()
    turtle.penup()


def polygon(length, sides, color, rotation):
    inner_angle = 360/sides
    turtle.pendown()  # Format turtle
    turtle.setheading(180+rotation)
    if ',' in color:
        turtle.colormode(255)
        color = color.split(', ')
        for x in range(3):
            color[x] = int(color[x])
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.begin_fill()
    for x in range(sides):
        turtle.left(inner_angle)
        turtle.forward(length)
    turtle.end_fill()
    turtle.penup()


def pyramid(base, height, xy_rot, z_rot):
    iso_triangle(base, height, 'lightblue', 0)
    b1 = base * z_rot/90
    left = math.sqrt((base/2)**2 + height**2)+1
    top_angle = math.asin(base/(2*left))/(math.pi/180)
    turtle.setheading(180)
    turtle.forward(1)
    print(top_angle)
    turtle.fillcolor('blue')
    turtle.begin_fill()
    turtle.setheading(270)
    turtle.right(top_angle)
    turtle.forward(left)
    turtle.setheading(0)
    turtle.forward(b1)
    turtle.end_fill()


def customTriangle(left, base, right, color, rotation, starting):
    if left + right <= base:
        print('Sum of the sides of triangle cannot be larger than base.')
        return
    semi = (left+base+right)/2
    area = math.sqrt(semi*(semi-left)*(semi-base)*(semi-right))
    height = (2*area)/base
    left_angle = math.degrees(math.acos(height/left))
    right_angle = math.degrees(math.asin(height/right))
    turtle.pendown()# Format turtle
    if ',' in color:
        turtle.colormode(255)
        color = color.split(', ')
        for x in range(3):
            color[x] = int(color[x])
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.begin_fill()
    if starting == -1:
        turtle.setheading(rotation)  # Bottom line
        turtle.forward(base)
        turtle.setheading(rotation+180-right_angle)  # Right line
        turtle.forward(right)
        turtle.setheading(rotation-90-left_angle)  # Left line
        turtle.forward(left)
    elif starting == 1:
        turtle.setheading(rotation+180-right_angle)  # Right line
        turtle.forward(right)
        turtle.setheading(rotation-90-left_angle)  # Left line
        turtle.forward(left)
        turtle.setheading(rotation)  # Bottom line
        turtle.forward(base)
    else:
        turtle.setheading(rotation-90-left_angle)  # Left line
        turtle.forward(left)
        turtle.setheading(rotation)  # Bottom line
        turtle.forward(base)
        turtle.setheading(rotation+180-right_angle)  # Right line
        turtle.forward(right)
    turtle.end_fill()
    turtle.penup()




# base =75 placeholder
# 63*sb1/80, sb1, 23*sb1/80
# triangle(63, 80, 23, 'black', 0)
# turtle.mainloop()
"""
turtle.speed(100)
triangle(80, 100, 'red', 40)
turtle.setheading(180)
turtle.forward(200)
rect(80, 80, 'blue', -40)
turtle.setheading(45)
turtle.forward(250)
polygon(50, 6, 'green', 0)
turtle.setheading(-45)
turtle.forward(250)
parallel(50, 60, 70, 'purple', 0)
turtle.setheading(45)
turtle.forward(250)
# quadril(50, 6, 'purple', 0)


turtle.hideturtle()
turtle.mainloop()
"""
