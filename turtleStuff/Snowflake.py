import turtle
import math

turtle.speed(1000)

def snowflake(length, layers):
    tips = 6
    tipdis = length / 5  # Length of each sideways pertrution
    tipextra = math.cos(math.pi/4) * tipdis * 1.5
    print(tipextra)
    #  Distance between far tip intersection and tip
    layerdis = length / layers  # Distance between pertrutions
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


snowflake(100, 3)
turtle.hideturtle()
turtle.mainloop()