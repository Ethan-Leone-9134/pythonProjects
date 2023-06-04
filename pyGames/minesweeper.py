"""
File Name   :  minesweeper.py
Author      :  Ethan Leone
Date        :  05/26/2023
Description :  This script contains a basic minesweeper game

Usage:
- Ensure that the required libraries are installed by running 'pip install pygame'.
- Update custom module: pygameClasses, colors.
- Run the script to play the game.
"""

#%% Import Statements %%#
import os                          # Used for operating system related functionalities
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'  # Disable pygame welcome message
import pygame                      # Pygame library for game development
import random                      # Used for generating random numbers or choices
import colors as clr               # Custom module for defining color constants
import pygameClasses as pgc        # Custom module containing pygame classes

#%% Define Classes #%%


class Button(pgc.pygamePushButton):
    """
    Class represents the primary "boxes" for the game

    Attributes:
        rect (pygame.Rect)      : Object defining the position and size.
        backColor (tuple)       : The background color of the object in RGB format.
        underText (str)         : The important game text that is hidden at the start
        text (str)              : The text currently displayed on the box.
        textColor (tuple)       : The color of the text in RGB format.
        index (int)             : The index value of the object.
        opened (bool)           : Was the object is opened.
        cascadeChecked (bool)   : Was the object checked for cascading
        flagged (bool)          : Is the box flagged

    Methods:
        draw()                  : Draw the button on the Pygame window.
        is_clicked(mouse_pos)   : Check if the button is clicked based on the mouse position.
        update()                : Update the button based on its current state.
        mine()                  : Set the button text to mine value.
        addNeighbor()           : Add 1 to the surrounding indicator.
        flag()                  : Handle adding flags.
        checked()               : Set cascaded to true
        finish()                : Sequence to run when the game has terminated (tells if flags were right).
    """

    def __init__(self, x:int , y: int, width: int, height: int, index: int, backColor: tuple, textColor: tuple):
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
        super().__init__(window, x, y, width, height, backColor, " ", textColor)
        # self.backColor = backColor
        # self.text = " "
        # self.textColor = textColor
        self.underText = " "
        self.index = index
        self.opened = False
        self.cascadeChecked = False
        self.flagged = False


    def update(self, normal=1):
        """
        Update the boxes and unhide text

        Inputs: 
            normal (int) : Optional argument - 0 for opened as a cascade
        """
        if not(self.flagged or self.opened):    # If box can be updated
            self.opened = True                      # Set box to open
            self.text = self.underText              # Set unhide true value
            if self.underText == " ":               # If underText is a blank
                self.backColor = clr.LIGHTGRAY
            elif self.underText == "1":             # If underText is "1"
                self.backColor = clr.GREEN
            elif self.underText == "2":             # If underText is "2"
                self.backColor = clr.TEAL
            elif self.underText == "3":             # If underText is "3"
                self.backColor = clr.CYAN
            elif self.underText == "4":             # If underText is "4"
                self.backColor = clr.BLUE
                self.textColor = clr.WHITE
            elif self.underText == "5":             # If underText is "5"
                self.backColor = clr.NAVY
                self.textColor = clr.WHITE
            elif self.underText == "6":             # If underText is "6"
                self.backColor = clr.PURPLE
                self.textColor = clr.WHITE
            elif self.underText == "M":             # If underText is a mine
                self.backColor = clr.RED

            if normal or self.underText != " ":     # If the box is not part of a cascade
                self.cascadeChecked = True              # Set the box's cascade value to true


    def mine(self):
        """
        Set to text to mine value
        """
        self.underText = "M"            # Set under mine


    def addNeighbor(self):
        """
        Add 1 to the surrounding indicator
        """

        if self.underText == " ":                       # Check blankness
            self.underText = "0"                            # Set blank to zero for the next step
        if self.underText != "M":                       # Check if not mine
            self.underText = str(int(self.underText) + 1)   # Increment value


    def flag(self):
        """
        Handle adding flags        
        """

        self.flagged = not(self.flagged)    # Flip flagged variable
        if self.flagged:                    # Is the box being flagged
            self.text = "F"                     # Update display
            self.backColor = clr.GOLD
        else:                               # Is the box being unflagged
            self.text = " "                     # Update display
            self.backColor = clr.GRAY


    def checked(self):
        """
        Sets the value of the boolean for cascading to true
        """
        self.cascadeChecked = True      # Set checked to true


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

        self.draw()                             # Print box to screen


class FlagBox:
    """
    Class represents the main informational box for the game flags.

    Attributes:
        backColor (tuple): The backColor of the button in RGB format.
        flags (int): The number of remaining flags
        bombs (int): The number of bombs
        text (str): Text displayed on the screen
        textColor (tuple): The backColor of the text in RGB format.
        flagList (set): Contains positions of all flagged boxes

    Methods:
        draw(): Show the box on the screen
        place(index): Places a flag on the board at the specified index and updates the flag count.
        lift(index): Lifts a flag from the board at the specified index and updates the flag count.
        winner(): Updates the flag box when the game is won.
    """
    
    def __init__(self, x, y, width, height, backColor, bombCount, textColor):
        """
        Class represents the main informational box for the game flags.

        Inputs:
            x (int): The x-coordinate of the top-left corner of the button.
            y (int): The y-coordinate of the top-left corner of the button.
            width (int): The width of the button.
            height (int): The height of the button.
            backColor (tuple): The backColor of the button in RGB format.
            bombs (int): The number of bombs
            textColor (tuple): The backColor of the text in RGB format.
        """

        self.rect = pygame.Rect(x, y, width, height)
        self.backColor = backColor
        self.flags = bombCount
        self.bombs = bombCount
        self.text = f"Flags : {self.flags} / {self.bombs}"
        self.textColor = textColor
        self.flagList = set()


    def draw(self):
        """
        Draw the box on the Pygame window.
        """

        pygame.draw.rect(window, self.backColor, self.rect)     # Draw the button rectangle
        font = pygame.font.Font(None, 32)                       # Set the font for the button text
        text = font.render(self.text, True, self.textColor)     # Render the button text
        text_rect = text.get_rect(center=self.rect.center)      # Position the text at the center of the button
        window.blit(text, text_rect)                            # Draw the text on the window


    def place(self, index: int):
        """
        Places a flag on the board at the specified index and updates the flag count.

        Inputs:
            index (int): The index where the flag is placed.
        """

        if self.flags > 0:                                 # If there are flags left to place
            self.flags -= 1                                # Decrease the flag count
            self.text = f"Flags : {self.flags} / {self.bombs}"  # Update the text with the new flag count
            self.flagList.add(index)                       # Add the index to the flagList


    def lift(self, index: int):
        """
        Lifts a flag from the board at the specified index and updates the flag count.

        Inputs:
            index (int): The index where the flag is lifted.
        """
        
        if self.flags >= 0:                                # If there are flags (or no flags) on the board
            self.flags += 1                                # Increase the flag count
            self.text = f"Flags : {self.flags} / {self.bombs}"  # Update the text with the new flag count
            self.flagList.remove(index)                    # Remove the index from the flagList


    def winner(self):
        """
        Updates the flag box when the player won.
        """

        self.rect.width = int(self.rect.width*1.5)         # Increase the width of the flag box
        self.text = f"Flags : {self.flags} / {self.bombs} - Victory"  # Update the text with victory message
        self.backColor = clr.GREEN                         # Set the background color to green


class resetButton(pgc.pygamePushButton):
    """
    Class represents the primary "boxes" for the game

    Attributes:
        rect (pygame.Rect)  : Object defining the position and size.
        backColor (tuple)   : The background color of the object in RGB format.
        underText (str)     : The important game text that is hidden at the start
        text (str)          : The text currently displayed on the box.
        textColor (tuple)   : The color of the text in RGB format.

    Methods:
        draw()                  : Draw the button on the Pygame window.
        is_clicked(mouse_pos)   : Check if the button is clicked based on the mouse position.
        checkClick(mouse_pos)   : Handle resets
    """
        
    def __init__(self, x:int , y: int, width: int, height: int, backColor: tuple, textColor: tuple):
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
        super().__init__(window, x, y, width, height, backColor, "Restart", textColor)

    def checkClick(self, mousePos):
        """
        Check if the reset button was pressed

        Inputs:
            mousePos - mouse position
        """

        if self.is_clicked(mousePos):          # Check if the box was pressed
            pygame.quit()                           # Terminate pygame
            import subprocess                       # Import subprocess module
            subprocess.Popen(['python', __file__])  # Replay the current script


#%% Define Flow Functions %%#

def findDimensions() -> tuple[int, int]:
    """
    Calculate the size and bomb count

    Outputs:
        size  (int) : Amount of rows and columns of boxes
        bombs (int) : Amount of bombs in game
    """

    size = random.randint(8, 14)
    bombs = random.randint(10, 25)
    # bombs = 5
    # size = 12

    return size, bombs


def createWindow(size: int) -> pygame.Surface:
    """
    Generate a pygame figure window

    Inputs:
        size (int) : number of columns and rows in the game

    Outputs: 
        window (pygame display) : main window for the program
    
    """
    
    pygame.init()           # Initialize Pygame

    width = size*60+10             # Set the screen width
    height = size*60+10+100            # Set the screen height

    window = pygame.display.set_mode((width, height))       # Create the window
    pygame.display.set_caption("Minesweeper")          # Set the title

    return window


def generateButtons(size: int) -> list:
    """
    Create the push buttons

    Inputs:
        size (int)   : number of columns and rows in the game
    
    Outputs: 
        boxes (list) : list of push buttons
    """

    boxes = []              # Initialize position list
    length = 50                 # Square side length
    for r in range(size):       # For each row
        for c in range(size):       # For each column
            xPos = c*(length+10)+10     # X position
            yPos = r*(length+10)+10     # Y position
            button = Button(xPos, yPos, length, length, (r*size+c), clr.GRAY, clr.BLACK)
            boxes.append(button)    # Add button to list

    return boxes


def addMines(size: int, buttonsList: list, quantity: int) -> tuple[list, set]:
    """
    Add all mines and update surrounding values

    Inputs:
        size (int)          : number of columns and rows in the game
        buttonsList (list)  : list of push buttons
        quantity (int)      : how many mines will be placed
    
    Outputs: 
        buttonsList (list)  : list of push buttons 
    """

    mines = set()          # Initialize list that contains positions of the mines

    # Generate mine locations
    while len(mines) < quantity:
        mineNum = random.randint(0, size**2-1)      # Determine the position of the current mine
        if mineNum not in mines:
            mines.add(mineNum)

    # Add mines and neighbors
    for mineNum in mines:                       # For each mine        
        buttonsList[mineNum].mine()                 # Set the position to a mine
        for currPos in getSurrounding(mineNum, size):
            buttonsList[currPos].addNeighbor()          # Add one to the boxes value

    return buttonsList, mines



#%% Define Iterated Functions %%#

def checkValid(currPos: int, size: int, mineNum: int) -> bool:
    """
    Check if the current position is a valid position within the specified size and mineNum.

    Inputs:
        currPos (int): The current position.
        size (int): The size of the grid.
        mineNum (int): The mine number.

    Outputs:
        (bool): True if the position is valid, False otherwise.
    """

    if -1 < currPos and currPos < size**2:                              # Avoid calling inexistant button
        if not ((currPos % size == 0) and (mineNum % size == size-1)):      # Prevent jumping from right to left
            if not ((currPos % size == size-1) and (mineNum % size == 0)):      # Prevent jumping from left to right
                return True
    return False


def getSurrounding(source: int, size: int) -> set:
    """
    Returns the list of valid surrounding boxes

    Inputs: 
        source (int) : Center box
        size   (int) : Dimensions of the game

    Outputs:
        surrounding (set) : All valid surrounding boxes
    """    

    surrounding = set()                         # Initialize set variable

    for r in range(-1, 2):                      # For each row
        for c in range(-1, 2):                      # For each col
            currPos = source + c*size + r               # Position of the box to be updated
            if checkValid(currPos, size, source):       # If the current position is valid
                surrounding.add(currPos)                    # Add to surrounding variable
    
    surrounding.remove(source)                  # Remove the center

    return surrounding


def clearSurrounding(buttonsList: list, origin: Button, size: int) -> list:
    """
    Clear all surrounding blanks and reveal the adjacent boxes

    Inputs: 
        buttonsList (list)  : Contains the game boxes
        origin (Button)     : Central box that was actually pressed
        size (int)          : Dimensions of game

    Outputs:
        buttonsList (list)  : Contains the game boxes after modifications
    
    """

    for surroundings in getSurrounding(origin.index, size):  # For all surrounding boxes
        buttonsList[surroundings].update(0)                     # Update surrounding boxes
    
    loopVariable = True                                     # Initialize variable
    while loopVariable:                                     # Detect if last loop had any hits
        loopVariable = False                                    # Reset variable
        for button in buttonsList:                              # For each button
            if button.opened and not button.cascadeChecked:         # Does it need to be verified
                loopVariable = True                                     # Increment loop variable
                button.checked()                                        # Set checked to true for box in question
                for outer in getSurrounding(button.index, size):        # Cascade around current box
                    buttonsList[outer].update(0)                            # Cascade update

    return buttonsList


def updateScreen(buttonsList, flagBox, restartButton, mode: int):
    """
    Update the screen during loops

    Inputs:
        buttonsList (list)          : List of game boxes
        flagBox (TextBox)           : Flag info box
        restartButton (PushButton)  : Button for restarts
        mode (int)                  : 1 for during game  |  2 for end of game    
    """
    
    if not(mode-1):
        window.fill(clr.WHITE)          # Clear the screen
        for block in buttonsList:       # For each button
            block.draw()                    # Re-add button
        flagBox.draw()                  # Draw flag box
        restartButton.draw()            # Draw restart button
        pygame.display.update()         # Update the display
    else:
        # Finish screen
        window.fill(clr.WHITE)          # Clear the screen
        for block in buttonsList:       # For each game box
            block.finish()                  # Uncover
        flagBox.draw()                  # Draw flag box
        restartButton.draw()            # Draw restart button
        pygame.display.update()         # Update screen



#%% Main Program %%#

# Window generation
size, bombs = findDimensions()
window = createWindow(size)
buttonsList = generateButtons(size)
buttonsList, mineList = addMines(size, buttonsList, bombs)
flagBox = FlagBox(60, size*60+20, 60*3, 50, clr.LAVENDER, bombs, clr.BLACK)
restartButton = resetButton(60*6, size*60 + 20, 100, 50, clr.LAVENDER, clr.BLACK)

# Game loop
running = True
while running:                                          # Run with loop condition
    for event in pygame.event.get():                        # For each event
        if event.type == pygame.QUIT:                           # If quit
            running = False                                         # Set loop condition to false
        elif event.type == pygame.MOUSEBUTTONDOWN:              # If a mouse button is pressed
            mouse_pos = pygame.mouse.get_pos()                      # Get mouse position
            if event.button == 1:                                   # If left click
                for block in buttonsList:                               # For each button
                    if block.is_clicked(mouse_pos):                         # If current button was pressed
                        if not(block.flagged or block.opened):                  # If not flagged
                            block.update()                                          # Remove cover
                            if block.underText == "M":                              # If mine
                                running = False                                         # Kill loop
                            if block.underText == " ":                              # If blankspace
                                buttonsList = clearSurrounding(buttonsList, block, size)
                            break                                                   # End click-searching loop
                restartButton.checkClick(mouse_pos)                         # Check for resets
            elif event.button == 3:                                 # If right click
                for block in buttonsList:                               # For each button
                    if block.is_clicked(mouse_pos):                         # If current button was the one pressed
                        if not block.opened:                                    # If current button was already open
                            if not block.flagged:                                   # If the current button is not flagged
                                if flagBox.flags > 0:                                   # If there are any flags left to place
                                    block.flag()                                            # Flag the current button
                                    flagBox.place(block.index)                              # Add flag to the info box
                            else:                                                   # If the current button is flagged
                                block.flag()                                            # Unflag the current button
                                flagBox.lift(block.index)                               # Remove flag from info box
                            if flagBox.flags == 0:                                  # If there are any flags left
                                if mineList == flagBox.flagList:                        # If the flags are placed correctly
                                    running = False                                         # Kill loop condition
                                    flagBox.winner()                                        # Update info box

    updateScreen(buttonsList, flagBox, restartButton, 1)    # Update the screen for continued play

# Keep screen open after end of game
updateScreen(buttonsList, flagBox, restartButton, 2)    # Update the screen finally
while True:                                             # Run until exitted
    for event in pygame.event.get():                        # Check event type
        if event.type == pygame.QUIT:                           # If quit event
            pygame.quit()                                           # Terminate pygame module
            exit()                                                  # Exit
        if event.type == pygame.MOUSEBUTTONDOWN:                # If mouse was pressed
            restartButton.checkClick(pygame.mouse.get_pos())        # Check if restarted

#%% End of File %%#