import turtle
import random
import Shapes as shapes

def house(width, height, color, rotation):
    shapes.rect(width, height, color, rotation)  # Draw house
    rw = 4*width/3  # Roof Dimension
    rh = 2*height/3
    turtle.setheading(180+rotation)  # Move Turtle
    turtle.forward(width/2)
    turtle.right(90)
    turtle.forward(rh)
    shapes.iso_triangle(rw, rh, 'grey', rotation)  # Draw Roof
    dw = width/5  # Door Dimensions
    dh = dw*2
    turtle.setheading(270+rotation)  # Move Turtle
    turtle.forward(rh+height)
    turtle.right(90)
    turtle.forward(dw/2)
    shapes.rect(dw, dh, 'black', 180)  # Door
    turtle.right(0)
    turtle.forward(dw/2)
    turtle.left(90)
    turtle.forward(height)








"""
house(140, 120, 'brown', 0)
turtle.mainloop()
"""