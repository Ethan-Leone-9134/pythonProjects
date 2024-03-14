"""
File Name   :  bingo.py
Author      :  Ethan Leone
Date        :  03/09/2024
Description :  This script generates a sample bingo board and dabs the positions as given

Usage:
- Ensure that the required libraries are installed by running 'pip install matplotlib numpy'.
- Update any custom modules.
- Run the script to perform the desired tasks.
"""

#%%%#   Import  Libraries   #%%%#
import matplotlib.pyplot as plt
from matplotlib.text import Text
import numpy as np
import random
import time 
import math


#%%%#   Define  Classes   #%%%#

class crossText(Text):
    def __init__(self, currX, currY, text, fontsize=12, color='black', **kwargs):
            super().__init__(currX, currY, text, fontsize=fontsize, color=color, **kwargs)
            self.posVec = [currX,currY,currX,currY]
            self.set_position((currX, currY))  # Set initial position
            self.set_fontsize(fontsize)  # Set initial fontsize
            self.set_color(color)  # Set initial color
            

    def set_position(self, position):
        self.set_x(position[0])
        self.set_y(position[1])
        self.posVec[0:2] = position
        plt.show()
        plt.pause(0.000001)

    def set_desired(self, position):
        self.posVec[2:4] = position

    def set_fontsize(self, fontsize):
        super().set_fontsize(fontsize)

    def set_color(self, color):
        super().set_color(color)

    def move(self):
        xSpeed = 0.2
        ySpeed = 0.2
        # Move x
        if self.posVec[0] > self.posVec[2]:
            self.posVec[0] -= xSpeed
        elif self.posVec[0] < self.posVec[2]:
            self.posVec[0] += xSpeed
        else:
            self.posVec[0] = self.posVec[2]

        # Move y
        if self.posVec[1] > self.posVec[3]:
            self.posVec[1] -= ySpeed
        elif self.posVec[1] < self.posVec[3]:
            self.posVec[1] += ySpeed
        else:
            self.posVec[1] = self.posVec[3]

        self.posVec = [round(val, 1) for val in self.posVec]
        # Move cross hair
        self.set_position((self.posVec[0],self.posVec[1]))

    def isFar(self):
        return (abs(cHair.posVec[0]-cHair.posVec[2])+abs(cHair.posVec[1]-cHair.posVec[3]) > 0.005)


#%%%#   Define  Functions   #%%%#

def box(wid, axis=1, star=0):
    if axis:
        return [star, wid, wid, star, star]
    else:
        return [star, star, wid, wid, star]

def grid(wid, scale, axis=1, star=0):
    outer = []
    for n in range(scale):
        if (axis):
            wid2 = wid
        else: 
            wid2 = wid*(n+1)

        outer += box(wid2, axis, star)

    return outer

def genFig():
    #%# Plotting
    fig, ax = plt.subplots(figsize=(4,6))        # Initialize
    ax.set_title("Bingo Board")     # Set title
    ax.axis('equal')                # Set equal axis width

    ax.set_xticks(range(0,10+1))    # Set x ticks
    ax.set_yticks(range(0,15+1))    # Set y ticks

    ax.set_xlim(-0.01,10.01)        # Set x limit
    ax.set_ylim(-0.02,15.02)        # Set y limit

    ax.set_xticklabels([])          # Hide x labels
    ax.set_yticklabels([])          # Hide y labels

    plt.ion()
    plt.grid(which='major', axis='both', linestyle='-',linewidth=1)

    return ax

def randVec(min,max,len,count=1):

    vect = []
    for bNum in range(count):
        currLine = list(range(min, max+1))
        # print(currLine)
        random.shuffle(currLine)
        vect += currLine[0:len]

    return vect

def getIndex(aray, value):
    indexes = [index for index, element in enumerate(aray) if element == value]
    return indexes

def readCalls(timeOriginal):
    


#%%%#   Start  Main  Code   #%%%#

# Set size
width = 2
height = 3

# Generate boards
board = []
for n in range(width*5):
    board += [randVec(1 + height*5*(n % 5), height*5 + height*5*(n % 5), 5, height)]
print(board)

# Graph lines
xpoints = np.array(grid(5,3,1,0) + grid(10,3,1,5))
ypoints = np.array(grid(5,3,0,0) + grid(5,3,0,0))
ax = genFig()
ax.plot(xpoints, ypoints)       # Make plot
plt.pause(0.5)

# Place numbers
for c in range(width*5):
    for r in range(height*5):
        ax.text(c+0.2, height*5-1-r+0.2, board[c][r], fontsize=13, color='blue' )
        plt.show()
        plt.pause(.01)

# Generate crosshair 
cHair = ax.add_artist(crossText(2,height*5-1,"+", fontsize=28, color='blue'))
tOrigin = time.time()

# Call numbers
called = set()
for ballNum in range(0,74):
    # Find calls
    ranNum = random.randint(1,75)
    while ranNum in called:
        ranNum = random.randint(1,75)
    called.add(ranNum)

    # Place rings
    for n in range(width):
        col = math.floor((ranNum-1)/15)+(5*n)   # column Number
        if ranNum in board[col]:                # If there is a match
            spotz = getIndex(board[col],ranNum)     # Find all indexes
            if (n+1) % 2 == 0:
                spotz.reverse()
            for spot in (spotz):                    # Repeat for each found position
                cHair.set_desired([col,height*5-1-spot] )# Set the desired position
                while cHair.isFar():                    # While the marker is not over a target
                    cHair.move()                            # Move the marker

                plt.pause(0.5)                          # Pause for the dabbing
                ax.text(cHair.posVec[0],cHair.posVec[1]+0.25, "⬤", fontsize=20, color='green',alpha=0.25)
                plt.show()                              # Show the plot
        
    cHair.set_desired([(width*5-1)/2,height*5-1])

    print(f"Ball call {ranNum} ended at time: {round(time.time() - tOrigin,2)} / {15*(ballNum+1)} [s]")

    while (time.time() - tOrigin) < 15*(ballNum+1): 
        cHair.move()
    

plt.show(block=True)
#%%%#   End  of  Script  File   #%%%#
