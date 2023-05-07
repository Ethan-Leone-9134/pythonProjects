import turtle
import math

turtle.speed(10)
curInt = 1



def draw_recusions (length, levels):
    coords = [0, 1, 2]
    for x in range(levels):
        cordInd = 1
        if x == 1:
            baseA = length
            baseB = 0
        else:
            size = coords.count("")
            strcord = ""
            for z in coords:
                strcord = "" + strcord + str(z)
            strcord = "[" + strcord + "]"
            print(strcord)
            for y in range(4):
                baseA = str(coords[cordInd])
                baseB = str(coords[cordInd+1])
                coordsnew = baseA + ", " + baseB + ", " + baseB + ", " + baseA + ", -" + baseA + ", " + baseB + ", " + baseB + ", -" + baseA
                old = "" + str(baseA) + ", " + str(baseB) + ""
                strcord = strcord.replace(old, coordsnew)
            strcord = strcord.split(", ")
            coords = []
            for c in strcord:
                intc = int(c)
                coords = [coords] + [intc]

            print(coords)

        cordInd = 1 + 1
        coords = [baseA, baseB, baseB, baseA, -baseA, baseB, baseB, -baseA]
        print(coords)


    # for x in range(levels):

    corepind = 1
    turtle.left(45)
    turtle.pd()
    for x in coords:
        if corepind/2 == math.ceil(corepind/2):
            turtle.right(90)
            turtle.forward(x)
        else:
            turtle.left(90)
            turtle.forward(x)
        corepind = corepind + 1
    #


draw_recusions(100, 2)

turtle.hideturtle()
turtle.mainloop()