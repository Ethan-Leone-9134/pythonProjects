import turtle
import random
import Shapes as shapes
import Formations as nature
import Backdrop as backing
from House import house
from Gradient import gradient

frame_width = int(800)
frame_height = int(500)
ground_width = 100

turtle.setup(frame_width, frame_height, 250, 50)

turtle.speed(0)
# Background
turtle.penup()

backing.backdrop(frame_width, frame_height, 'lightblue')
turtle.setposition(-frame_width/2, -frame_height/2)
shapes.rect(frame_width, 150, 'lightgreen', 180)
turtle.setposition(-200, -100)
nature.mountain(150, 250, 0, 3)
turtle.setposition(-100, -100)
nature.mountain(170, 280, 0, 1)
turtle.setposition(100, -100)
nature.mountain(160, 270, 0, 4)
turtle.setposition(200, -100)
nature.mountain(180, 300, 0, 2)

turtle.setposition(-350, -150)
nature.tree(40, 30, 60, 80, 3, 30)



turtle.hideturtle()
turtle.mainloop()