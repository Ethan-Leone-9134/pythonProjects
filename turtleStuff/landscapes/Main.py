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

turtle.setposition(-frame_width/2, (-frame_height/2))  # Backdrop
shapes.rect(frame_width, frame_height, '110, 160, 230', 180)
turtle.setposition(0, 0)
turtle.penup()

backing.back_mount(frame_width, frame_height/1.75, frame_height, '165, 120, 230')  # Hills
backing.back_mount(frame_width, frame_height/2.2, frame_height, '151, 90, 236')
backing.back_mount(frame_width, frame_height/2.75, frame_height, '137, 60, 242')
backing.back_mount(frame_width, frame_height/3.2, frame_height, '123, 30, 248')
backing.back_mount(frame_width, frame_height/3.5, frame_height, '110, 0, 255')

turtle.setposition(frame_width/2, -frame_height/2)  # Grass
gradient(ground_width, frame_height*2, '67, 255, 49', '67, 155, 49', 90)
#  shapes.rect(frame_width, ground_width, '67, 255, 49', 180)

turtle.setposition(0, 0)

turtle.setposition(150, -150)
nature.mountain(150, 150, 0, 3)

turtle.setposition(-150, -150)
nature.mountain(200, 200, 0, 2)

turtle.setposition(0, -150)
nature.mountain(350, 300, 0, 1)

turtle.setheading(180)
turtle.forward(300)
turtle.setheading(270)
turtle.forward(220)

house(70, 60, 'brown', 0)

turtle.setheading(0)
turtle.forward(150)

nature.tree(40, 30, 60, 80, 3, 30)

turtle.setheading(270)
turtle.forward(130)
turtle.setheading(0 - 3)
turtle.forward(150)
nature.tree(40, 30, 60, 80, 3, 30)

turtle.setheading(270)
turtle.forward(130)
turtle.setheading(0 + 7)
turtle.forward(150)
nature.tree(40, 30, 60, 80, 3, 30)

turtle.setheading(270)
turtle.forward(130)
turtle.setheading(0 - 2)
turtle.forward(150)
nature.tree(40, 30, 60, 80, 3, 30)


"""
for x in range(10):
    turtle.setposition(random.randint(-frame_width/2, frame_width/2), random.randint(-frame_height/2 + 100, frame_height/2))
    snowflake(3, 2, 'white')
    
    """

turtle.hideturtle()
turtle.mainloop()