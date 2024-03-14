"""
File Name   :  bingo4.py
Author      :  Ethan Leone
Date        :  03/14/2024
Description :  This script generates a sample bingo board 
               and dabs the positions as given

Usage:
- Ensure that the required libraries are installed by running 'pip install pygame'.
- Update custom module: pygameClasses, colors.
- Run the script to play the game.
"""

#%%%#   Import Statements  #%%%#
import os                           # Used for operating system related functionalities
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'  # Disable pygame welcome message
import pygame                       # Pygame library for game development
import random                       # Used for generating random numbers or choices
import colors as clr                # Custom module for defining color constants
import pygameClasses as pgc         # Custom module containing pygame classes
from itertools import permutations  # Function to find all possible permutations
import numpy as np                  # Array library for arrays
import math                         # Math library for most calculations past +-*/
import time                         # Time Library to regulate the code relative to real-time


#%%%#   Define Classes   #%%%#


class Button(pgc.pygamePushButton):
    """
    Class represents the primary "boxes" for the game

    Attributes:
        rect (pygame.Rect)      : Object defining the position and size.
        pos(list)               : Vector of relevant position values
        backColor (tuple)       : The background color of the object in RGB format.
        text (str)              : The text currently displayed on the box.
        textColor (tuple)       : The color of the text in RGB format.
        index (int)             : The index value of the object.

    Methods:
        draw()                  : Draw the button on the Pygame window.
        target()                : Handle adding targets.
        move()                  : Increment position.
        isFar()                 : Logical to detect distance from target position.
        finish()                : Sequence to run when the game has ended.
    """

    def __init__(self, x:int , y: int, width: int, height: int, index: int, backColor: tuple, textColor: tuple, text=" "):
        """
        Button class represents a clickable button in Pygame.

        Inputs:
            x (int)             : The x-coordinate of the top-left corner of the button.
            y (int)             : The y-coordinate of the top-left corner of the button.
            width (int)         : The width of the button.
            height (int)        : The height of the button.
            index (int)         : The index of the button in the list
            backColor (tuple)   : The text color in RGB format.
            textColor (tuple)   : The background color in RGB format.
        """
        super().__init__(window, x/SCALE, y/SCALE, width/SCALE, height/SCALE, backColor, " ", textColor)
        self.backColor = backColor
        self.text = text
        self.textColor = textColor
        self.pos = [x/SCALE, y/SCALE, width/SCALE, height/SCALE, x/SCALE, y/SCALE]
        self.index = index
        # self.set_font_size(int(20/SCALE))
        self.fnt = pygame.font.SysFont("Ariel", int(100/SCALE)) 
        self.draw()



    def target(self, type=0):
        """
        Handle flagging targets
        Input: 
            type (bool)     : 0 for flag  &  1 for pressed
        """

        self.flagged = type                 # Flip flagged variable
        if self.flagged:                    # Is the box being flagged
            self.backColor = clr.GREEN           # Update display
        else:                               # Is the box being unflagged
            self.backColor = clr.GOLD           # Update display
        self.draw()


    def finish(self):
        """
        Sequence to run when the game has terminated (tells if flags were right)
        """

        self.update()                           # Update the box

        if self.flagged:                        # Is the box flagged
            if self.underText == "M":               # If the box correctly flagged
                self.textColor = clr.GREEN              # Set "F" to green
            else:                                   # If the box falsely flagged
                self.textColor = clr.RED                # Set "F" to red


    def move(self):
        """
        Sets position of the box closer to the desired value
        """

        # Define game speed
        xSpeed = 6  /SCALE
        ySpeed = 6  /SCALE

        # Move x position
        xDif = self.pos[4] - self.pos[0]
        self.pos[0] += valueLim(xDif,xSpeed)/SCALE

        # Move y position
        yDif = self.pos[5] - self.pos[1]
        self.pos[1] += valueLim(yDif,ySpeed)/SCALE

        # Round position vector
        self.pos = [round(val, 5) for val in self.pos]

        # Move position of the box itself
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]

        Button((self.pos[0]-self.pos[2]/2)*SCALE, (self.pos[1]-self.pos[3]/2)*SCALE, self.pos[2]*2*SCALE, self.pos[3]*2*SCALE, 0, clr.GRAY, clr.GRAY)
        

    def isFar(self):
        """
        Logical to detect distance from target position.
        """
        return (abs(self.pos[0]-self.pos[4])+abs(self.pos[1]-self.pos[5]) > 5)


    def draw(self):
        """
        Draw the button on the Pygame window.
        """
        # Draw the button background
        pygame.draw.rect(window, self.backColor, self.rect)
        
        # Render the text
        text_surface = self.fnt.render(self.text, True, self.textColor)
        
        # Get the text surface rect
        text_rect = text_surface.get_rect()
        
        # Center the text on the button
        text_rect.center = self.rect.center
        
        # Blit the text onto the button
        window.blit(text_surface, text_rect)



#%%%#   Define   Visual  Initial   Functions   #%%%#

def createWindow(size: int) -> pygame.Surface:
    """
    Generate a pygame figure window

    Inputs:
        size (int) : number of columns and rows in the game

    Outputs: 
        window (pygame display) : main window for the program
    
    """
    
    pygame.init()           # Initialize Pygame

    width = 520             # Set the screen width
    height = 600            # Set the screen height

    window = pygame.display.set_mode((width, height))   # Create the window
    pygame.display.set_caption("Bingo Player")          # Set the title

    window.fill(clr.GRAY)       # Clear screen

    # pygame.font.SysFont("Ariel", int(20/SCALE))

    return window


def genBoxes(board: list) -> list:
    """
    Create the boxes

    Inputs:
        board (array)   : Array of board positions
    
    Outputs: 
        boxes (list)    : list of push buttons
    """

    boxes = []              # Initialize position list
    length = 93             # Square side length
    letDict = {0:"B", 1:"I", 2:"N", 3:"G", 4:"O"}
    for cn, column in enumerate(board):       # For each row
        # Letter Header
        Letter = Button(100*cn + 50*math.floor(cn/5), 80, length, length, 0 , clr.WHITE, clr.INDIGO)
        Letter.text = letDict[cn % 5]
        Letter.draw()
        boxes.append(Letter)
        # Number boxes
        for rn, point in enumerate(column):   # For each column
            button = Button(point[0], point[1], length, length, (0), clr.LIGHTGRAY, clr.BLACK)
            button.text = str(point[2])
            button.draw()
            boxes.append(button)    # Add button to list

    return boxes


#%%%#   Define      Temporary      Functions   #%%%#


def randVec(min:int,max:int,len:int,count:int=1) -> list:
    """
    Function randVec creates a vector of random points without repeating unless count is specified
    Inputs:
        min (int)      : Minimum of vector range
        max (int)      : Maximum of vector range
        len (int)      : Number of points in simple vector
        count (int)    : Number of repeatitions of vector
    Outputs:
        vect (list)    : Random integer vector
    """

    vect = []                               # Initialize list variable
    for bNum in range(count):               # For each repeatition
        currLine = list(range(min, max+1))      # Generate linear list
        random.shuffle(currLine)                # Shuffle data points in new addition
        vect += currLine[0:len]                 # Add to list
    return vect                             # Output list


#%%%#   Define   Machine   Input   Functions   #%%%#


def readBoard():
    """
    Function reads the board data

    Inputs:
        none
    Outputs:
        board (list)     : List of board data
    """

    # Generate boards
    board = []
    for n in range(WIDTH*5):        # For each column
        array = []
        vect = [randVec(1 + HEIGHT*5*(n % 5), HEIGHT*5 + HEIGHT*5*(n % 5), 5, HEIGHT)]      # Values of the column
        for cn, column in enumerate(vect):                  # For each column
            newCol = []                                         # New column
            for rn, ball in enumerate(column):                  # For each row in the column
                newCol += [[n*100 + 50*math.floor(n/5), 200 + rn*100 + 100*math.floor(rn/5), ball]]     # Data for the point
            array += [newCol]                                   # Add point to the column
        board += array                                      # Add column to the board
    return board                                            # Output the column


def readCalls(timeOriginal:float, called:list):
    """
    Function reads the called ball values

    Inputs:
        timeOriginal (float)    : Time at the start of the game loop
        called (list)           : List of called balls
    Outputs:
        called (list)           : List of called balls
        ranNum (int)            : Selected ball value
    """


    # Find calls
    ranNum = 0
    if len(called) == 73:
        called += "end"
    else:
        if (time.time() - timeOriginal) > 15*((len(called)-1)):
            ranNum = random.randint(1,75)
            while ranNum in called:
                ranNum = random.randint(1,75)
            called += [(ranNum)]
            print(f"Ball call: {ranNum}")

    return called, ranNum


def checkEnd():
    """
    Function terminates the pygame window.

    Inputs:
        none
    Outputs:
        none
    """

    for event in pygame.event.get():            # Check event type
        if event.type == pygame.QUIT:               # If quit event
            pygame.quit()                                # Terminate pygame module
            exit()                                       # Close the window


#%%%#   Define       Scanning      Functions   #%%%#


def getIndex(aray: list, value: int) -> list:
    """
    Function searches a list for a specific value
    Inputs:
        aray  (1-D List)    : List to be searched through
        value (int)         : Value to be detected
    Outputs:
        indexes (list)      : List of indexes where a match was found
    """

    # Found index list
    indexes = [index for index, element in enumerate(aray) if element == value]


    # if indexes == []:
    #     indexes = min(range(len(aray)), key=lambda i: abs(aray[i] - value))
    #     pass
    # Output vector
    return indexes


def getButInd(aray: list, value: int) -> list:
    """
    Function searches a board for a specific target
    Inputs:
        aray  (1-D List)    : Board to be searched through
        value (int)         : Target to be detected
    Outputs:
        ind (int)           : Index where a match was found
    """
    targDex = getIndex(aray[value[3]],value[0:3])   # Find the target
    ind = ( 1 + 16*value[3] + targDex[0] )          # Get the index in the board
    return ind                                      # Output value


def findTargets(board: list, currBall: int):
    """
    Function scans the board for all instances of the searched value

    Inputs:
        board (list)        : List of board data
        currBall (int)      : Selected ball value
    Outputs:
        targets (list)      : List of targeted board values
    """

    targets = []                            # Initialize list    [xPos, yPos, ballNumber, columnNumber]
    for cn in range(WIDTH):                     # For each column
        col = math.floor((currBall-1)/15)+(5*cn)    # column Number
        for rn, place in enumerate(board[col]):     # Board column
            if currBall in place:                       # If there is a match
                targets += [[place[0],place[1], currBall, col]] # Add target to list

        
    return targets                          # Output list


def optRoute(targets: list, currPos: list) -> list:
    """
    Function finds the most efficient route based on the targets given and current position
    Inputs:
        targets (list)      : List of UNoptimized target positions
        currPos (list)      : Current position of
    Outputs:    
        targets (list)      : List of OPtimized target positions
    """

    permz = (list(permutations(targets, len(targets))))     # All possible routes
    distz = []                              # Average distances vector
    for thisPerm in (permz):                # For each permutation
        perm = [[currPos[0]*SCALE] + [currPos[1]*SCALE] + [0]] + list(thisPerm)
        dist = []                               # Distance vector for this route
        for pointNum in range(len(perm)-1):     # For each path
            distSq = ((perm[pointNum][0] - perm[pointNum+1][0])**2 + (perm[pointNum][1] - perm[pointNum+1][1])**2 )
            dist.append(math.sqrt( distSq ) )
            
        try:
            distz.append(sum(dist))
        except ZeroDivisionError:               # Handle case where dist is an empty list
            distz.append(0)      

    minIndex = distz.index(min(distz))      # Find the index of the permz with the shortest distance
    targets = list(permz[minIndex])         # Find the associated route
    return targets                          # Output route


def findSurrounding(board, cross):

    cX = cross.pos[0]*SCALE
    cY = cross.pos[1]*SCALE

    topLineX = []
    for cols in board:
        topLineX += [cols[0][0]]
    
    targCol = findClosestIndex(topLineX, cX)

    mainColY = []
    for rows in board[targCol]:
        mainColY += [rows[1]]

    targRow = findClosestIndex(mainColY, cY) 

    buttonIndexes = []
    for rn in range(targRow-1, valueLim(targRow+2,HEIGHT*5)):
        for cn in range(targCol-1, valueLim(targCol+2,WIDTH*5)):

            buttonIndexes += [1 + 16*cn + rn]

    return buttonIndexes


def findClosestIndex(lst, target):
    return min(range(len(lst)), key=lambda i: abs(lst[i] - target))
    

def pickEnder(board, cross):


    middleL = math.floor(WIDTH*5/2)
    middleR = math.ceil(WIDTH*5/2)
    middle = (board[middleR][0][0] +  board[middleL][0][0])/2
    top = board[0][0][1] + 100
    bot = board[0][HEIGHT*5-1][1]
    place1 = [middle, top, 0, 0]
    place2 = [middle, bot, 0, 0]


    optimal = optRoute([place1, place2], cross.pos)
    if optimal[0][1] == place1[1]:
        closest = [round(middle/SCALE,3), round(top/SCALE,3)]
    else:
        closest = [round(middle/SCALE,3), round(bot/SCALE,3)]

    return closest



#%%%#   Define     All    Other    Functions   #%%%#

def valueLim(num, limit):
    # Restricts a number's absolute value if needed
    # (Shrinks if goes over positive limit)
    # (Grows if under negative limit)
    # Inputs  : num - original number
    #           limit - largest possible absolute value (smallest if negative)
    # Outputs : answer - restricted number
    answer = num

    if limit > 0:
        if abs(num) > limit: # If |num| exceeds limit
            if num < 0: # If num is negative
                answer = -limit
            elif num > 0: # If num is positive
                answer = limit
    elif limit < 0:
        if abs(num) < abs(limit): # If |num| exceeds limit
            if num < 0: # If num is negative
                answer = limit
            elif num > 0: # If num is positive
                answer = -limit
    return answer


#%%%#   Start  Main  Code #%%%#
###############################


WIDTH = 3                   # Boards width
HEIGHT = 3                  # Boards height
SCALE = 3.5                 # Game Scale
           
width = int(WIDTH*600/SCALE)                    # Set the screen width
height = int((HEIGHT*700+200)/SCALE)            # Set the screen height

board = readBoard()                             # Get input for the game board
window = createWindow([width,height])           # Generate pygame window
buttonsList = genBoxes(board)                   # Generate piece places

cHair = Button(225,225, 50,50,                  # Generate crosshair 
            0,clr.WHITE, clr.BLUE, "+")
timeBox = Button(100,2000,WIDTH*500,100,        # Generate info box on the bottom
            0, clr.WHITE,clr.BLUE, "TIME: 0 [s]")


# Initialize variables
called = [0]                # List of called numbers
tars = []                   # List of game targets
lineBoard = [item for sublist in board for item in sublist]     # 1-D Box vector
tOrigin = time.time()       # Time at start of loop

try:

    while "end" not in called:                  # While game is active
        alpha = time.time()
        # Detect routes
        [called, currBall] = readCalls(tOrigin, called) # Detect ball number inputs
        if currBall != 0:                       # If there is an actual ball to detect
            tars += findTargets(board, currBall)    # Find all targets to hit
            for targ in tars:                       # Set target color
                buttonsList[getButInd(board,targ)].target()   
            tars = optRoute(tars, cHair.pos)        # Optimize the target list

        # Set desired position
        if tars != []:
            cHair.pos[4:6] = ([tars[0][0]/SCALE+5,tars[0][1]/SCALE+5] )# Set the desired position
            cHair.textColor = clr.BLUE
        else:
            cHair.pos[4:6] = pickEnder(board,cHair)
            # print(cHair.pos)
            cHair.textColor = clr.GREEN

        # Change position
        if tars != []:                  # If there are targets to hit
            if cHair.isFar():              # If the marker is not over a target
                cHair.move()                            # Move the marker
            else:
                pygame.time.delay(500)                  # Pause for the dabbing
                buttonsList[getButInd(board,tars[0])].target(1)   
                # print(f"Ball call {tars[0][2]} pressed at time: {round(time.time() - tOrigin,2)} / {15*(len(called)-1)} [s]")
                tars.remove(tars[0])
        cHair.move()
        tPast = time.time()-tOrigin
        timeBox.text = f"Passed: {tPast: 0.1f} [s]  |  To-Ball: {(15*(len(called)-1)-tPast): 0.1f} [s]  |  {called[-1]}"
        timeBox.draw()

        beta = time.time()
        # Display
        # window.fill(clr.GRAY)       # Clear screen
        # for butt in buttonsList:    # For each box
        #     butt.draw()                 # Show box
        for poses in findSurrounding(board, cHair):
            # print(poses)
            buttonsList[poses].draw()
        cHair.draw()                # Crosshair box
        pygame.display.flip()       # Update screen
        # clock = pygame.time.Clock() # 

        
        while (time.time() - alpha) < (1/50):
            checkEnd()                  # Detect end of game
        gamma = time.time()
        # print(f"Time to plot {1000*(gamma-alpha): 7.3f} [ms]   &   Time to calculate {1000*(beta-alpha): 5.2f} [ms]")
        # print(f"Time to plot {1000*(gamma-alpha)-20: 7.3f} [ms]")
        # End of main loop


    while True:                 # Run until exitted
        checkEnd()                  # Detect end of game

except KeyboardInterrupt:
    print("--- Keyboard Interrupt Occured ---")

#%%%#   End  of  Script  File  #%%%#
