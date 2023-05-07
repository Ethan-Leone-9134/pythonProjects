import turtle
import random
import math
import Shapes as shapes

# Function List for turtle to draw formations
# tree - Creates a brown tree trunk with green triangular leaves
# mountain - Creates a triangular mountain using a base and height, with gradient level 'layer'
# snowflake - Creates a snowflake of a certain length and 'layer' pertusions from each branch

# Notes for Formations
# Color - Applies to pen and will fill the shape in with that color
# Rotation - Rotates the shape counterclockwise

def tree(trunk_height, trunk_width, tri_height, tri_base, tri_count, tri_distance):
    brown = '59, 30, 0'  # Prefered Trunk Color Code
    shapes.rect(trunk_width, trunk_height, brown, 0)  # Draws Trunk
    turtle.setheading(90)  # Moves turtle to triangle's zenith
    turtle.forward(tri_height-tri_distance)
    turtle.setheading(180)
    turtle.forward(trunk_width/2)
    for x in range(tri_count):  # Draw Triangular Leaves
        turtle.setheading(90)
        turtle.forward(tri_distance)
        shapes.iso_triangle(tri_base, tri_height, 'green', 0)


def mountain(base, height, rotation, layer):
    turtle.pendown()
    turtle.setheading(90+rotation)
    turtle.forward(height)
    if layer == 1:  # Default color gradients
        color = '160, 160, 160'
    elif layer == 2:
        color = '140, 140, 140'
    elif layer == 3:
        color = '120, 120, 120'
    elif layer == 4:
        color = '100, 100, 100'
    else:
        color = '160, 160, 160'
    shapes.iso_triangle(base, height, color, rotation)  # Draw base mountain
    snow_base = base/4  # Snow dimensions
    snow_height = height/4
    shapes.iso_triangle(snow_base, snow_height, 'white', rotation)  # Draw Snow
    turtle.setheading(270+rotation)  # Move turtle for extra mountain triangle
    turtle.forward(snow_height)
    turtle.setheading(180+rotation)
    turtle.forward(snow_base/2)
    turtle.setheading(0+rotation)
    if ',' in color:  # Interpret Colors
        turtle.colormode(255)
        color = color.split(', ')
        for x in range(3):
            color[x] = int(color[x])
    turtle.fillcolor(color)
    turtle.begin_fill()
    pos_left = str(turtle.pos()).split(",")  # Calculate dimensions for the extra grey
    plx = float(pos_left[0].replace("(", "")) + snow_base
    ply = float(pos_left[1].replace(")", "")) - 1
    turtle.left(random.randint(10, 20))  # Draw up extra grey
    turtle.forward(snow_base * random.randint(5, 8)/10)
    turtle.setposition(plx, ply)
    turtle.end_fill()



def snowflake(length, layers, color):
    tips = 6
    tipdis = length / 5  # Length of each sideways pertrution
    tipextra = math.cos(math.pi/4) * tipdis * 1.5
    #  Distance between far tip intersection and tip
    layerdis = length / layers  # Distance between pertrutions
    turtle.color(color)
    turtle.pd()
    turtle.setheading(90)
    for x in range(tips):
        turtle.forward(length)  # Go up
        turtle.forward(tipextra)
        turtle.back(tipextra)
        for x in range(layers):
            turtle.left(45)  # Turn Left
            turtle.forward(tipdis)
            turtle.back(tipdis)
            turtle.right(90)  # Turn Right
            turtle.forward(tipdis)
            turtle.back(tipdis)
            turtle.left(45)  # Pull Back
            turtle.back(layerdis)
            tipdis = tipdis * 1.5
        turtle.right(360/tips)
        tipdis = length/5
    turtle.pu()