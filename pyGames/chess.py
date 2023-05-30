

#%% Import Statements %%#
import os                          # Used for operating system related functionalities
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'  # Disable pygame welcome message
import pygame                      # Pygame library for game development
import random                      # Used for generating random numbers or choices
import colors as clr               # Custom module for defining color constants
import pygameClasses as pgc        # Custom module containing pygame classes

#%% Define Classes %%#

class BoardTile(pgc.pygamePushButton):
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
        
    """
        
    def __init__(self, x:int , y: int, width: int, height: int, backColor: tuple):
        """
        Button class represents a clickable button in Pygame.

        Inputs:
            x (int)             : The x-coordinate of the top-left corner of the button.
            y (int)             : The y-coordinate of the top-left corner of the button.
            width (int)         : The width of the button.
            height (int)        : The height of the button.
            index (int)         : The index of the button in the list
            backColor (tuple)   : The text color in RGB format.
        """
        super().__init__(window, x, y, width, height, backColor, "", backColor)



#%% Define Functions %%#

def createWindow() -> pygame.Surface:
    """
    Generate a pygame figure window

    Inputs:
        none

    Outputs: 
        window (pygame display) : main window for the program
    
    """
    
    pygame.init()           # Initialize Pygame

    width = 8*60+10             # Set the screen width
    height = 8*60+10+100            # Set the screen height

    window = pygame.display.set_mode((width, height))       # Create the window
    pygame.display.set_caption("Minesweeper")          # Set the title

    return window


def generateTiles() -> list:
    """
    Create the push buttons

    Inputs:
        none
    
    Outputs: 
        boxes (list) : list of push buttons
    """

    boxes = []              # Initialize position list
    length = 50                 # Square side length
    for r in range(8):       # For each row
        for c in range(8):       # For each column
            xPos = c*(length+10)+10     # X position
            yPos = r*(length+10)+10     # Y position
            button = BoardTile(xPos, yPos, length, length, clr.GRAY)
            boxes.append(button)    # Add button to list

    return boxes


def updateScreen(tiles, pieces, sideBoards):
    """
    Update the screen during loops

    Inputs:
        buttonsList (list)          : List of game boxes
        flagBox (TextBox)           : Flag info box
        restartButton (PushButton)  : Button for restarts
    """

    window.fill(clr.WHITE)          # Clear the screen
    for tile in tiles:       # For each button
        tile.draw()                    # Re-add button
    for piece in pieces:
        piece.draw()                  # Draw flag box
    # sideBoards.draw()            # Draw restart button
    pygame.display.update()         # Update the display





window = createWindow()
tiles = generateTiles()



while True:                                             # Run until exitted
    for event in pygame.event.get():                        # Check event type
        if event.type == pygame.QUIT:                           # If quit event
            pygame.quit()                                           # Terminate pygame module
        if event.type == pygame.MOUSEBUTTONDOWN:                # If mouse was pressed
            pass

    updateScreen(tiles, tiles, 0)

