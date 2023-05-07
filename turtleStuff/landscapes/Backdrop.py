import turtle
import random
import math
import Shapes as shapes


def backdrop(width, height, color):
    turtle.penup()
    turtle.setposition(width/2, height/2)
    shapes.rect(width, height, color, 0)
    turtle.setposition(0, 0)



def hills(width, height, frame_height, color):
    side_points = height-(frame_height/2)
    turtle.penup()
    turtle.setposition(width/2, side_points)
    if ',' in color:
        turtle.colormode(255)
        color = color.split(', ')
        for x in range(3):
            color[x] = int(color[x])
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.pendown()
    turtle.setheading(270)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    # Begin zig-zag
    runner = 0
    jumper = 0
    t_angle = 0
    pos_left = str(turtle.pos()).split(",")
    while runner < width+40:  # Repeat outside FOV
        angle = random.randint(-10, 10)  # Finds a random angle within a range
        magnitude = random.randint(50, 140)  # Gets a random magnitude within a range
        t_angle = angle + t_angle  # Keeps track of total angle related to 0
        if abs(t_angle) > 20:  # Keeps t_angle below 20 degrees from 0
            t_angle = t_angle - (2*angle)
            angle = -1 * angle
        turtle.left(angle)
        turtle.forward(magnitude)
        runner = abs(math.cos(angle * math.pi/180)*magnitude) + runner  # Tracks x-distance from leftmost point
        if runner >= width+40:  # To stop after outside FOV
            turtle.end_fill()



def back_mount(width, height, frame_height, color):
    side_points = height-(frame_height/2)
    turtle.penup()
    turtle.setposition(width/2, side_points)
    if ',' in color:
        turtle.colormode(255)
        color = color.split(', ')
        for x in range(3):
            color[x] = int(color[x])
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.pendown()
    turtle.setheading(270)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    # Begin zig-zag
    runner = 0
    jumper = 0
    t_angle = 0
    pos_left = str(turtle.pos()).split(",")
    while runner < width+40:  # Repeat outside FOV
        angle = random.randint(-10, 10)  # Finds a random angle within a range
        magnitude = random.randint(50, 100)  # Gets a random magnitude within a range
        jumper = math.sin(angle * math.pi/180)*magnitude + jumper  # Tracks y components to magnitude
        if abs(jumper) > 30:  #
            jumper = jumper - (2*math.sin(angle * math.pi/180)*magnitude)
            angle = -1 * angle
        turtle.setheading(angle)
        turtle.forward(magnitude)
        runner = abs(math.cos(angle * math.pi/180)*magnitude) + runner  # Tracks x-distance from leftmost point

        if runner >= width+40:  # To stop after outside FOV
            turtle.end_fill()

"""
frame_width = int(800)
frame_height = int(500)
ground_width = 100
turtle.setup(frame_width, frame_height, 250, 50)


turtle.speed(0)
backdrop(frame_width, frame_height, 'lightblue')
back_mount(frame_width, frame_height/1.5, '123, 30, 248')
back_mount(frame_width, frame_height/2, '137, 60, 242')
back_mount(frame_width, frame_height/3, '151, 90, 236')
back_mount(frame_width, frame_height/4, '165, 120, 230')
back_mount(frame_width, frame_height/5, '165, 120, 230')

turtle.mainloop()
"""