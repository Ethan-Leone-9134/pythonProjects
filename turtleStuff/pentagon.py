import turtle


def pentagons(length, iterations):
    turtle.speed(3)
    print(iterations)
    if iterations == 1:
        for x in range(5):
            turtle.forward(length)
            turtle.left(72)
    if iterations > 1:
        #  if iterations > 2:
        pentagons(length, iterations-1)
        turtle.forward(length)
        turtle.left(72)
        turtle.forward(length)
        turtle.left(72)
        pentagons(length/2, iterations-1)
        turtle.forward(length)
        turtle.left(72)
        turtle.forward(length)
        turtle.left(72)
        pentagons(length/2, iterations-1)
        turtle.forward(length)
        turtle.left(72)
    """pentagons(length/2, iterations - 1)"""


def main():
    turtle.speed(0)
    turtle.setheading(0)
    turtle.setworldcoordinates(-100, -10, 350, 350)
    pentagons(150, 5)
    turtle.hideturtle()
    turtle.mainloop()


turtle.speed(0)
main()
