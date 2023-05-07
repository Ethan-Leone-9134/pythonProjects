import turtle

points = 7

if (points/2) == round(points/2):
    print("Error")

midRight = round(points/2)
topLeft = points


pointList = [1, midRight, topLeft]

questioned = points - 3

print(pointList)
print(questioned)
for x in range(questioned):
    print(pointList[-1])
    tempP = pointList[-2] - 1
    print(tempP)
    pointList = pointList + [tempP]

print(pointList)

pointList = pointList + [1]
turtle.pendown()


turtle.left(90)

angle = ((midRight-1)* (360/points))

for x in range(points):
    turtle.right(angle)
    turtle.forward(100)

turtle.hideturtle()
turtle.mainloop()

