

#%% Import Statements %%#
import os                          # Used for operating system related functionalities
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'  # Disable pygame welcome message
import pygame                      # Pygame library for game development
import math
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
        
    def __init__(self, x:int , y: int, width: int, height: int, backColor: tuple, index: int):
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

        self.piece = " "
        self.index = index

    def drawPiece(self, source):
        self.piece = source
        self.textColor = source.color
        self.text = source.getImage()

        self.draw()

    def clear(self):
        self.piece = ""
        self.text = " "


class BasePiece():
    def __init__(self, color: tuple, name: str, index: int):

        self.color = color
        self.name = name
        self.index = index
        pass

    def horizontal(self, distance: int):
        self.index += distance
        pass

    
    def vertical(self, distance: int):
        self.index += distance * 8
        pass

    def getImage(self):

        if self.name == "Blank":
            return " "
        elif self.name == "Pawn":
            return "P"
        elif self.name == "Rook":
            return "R"
        elif self.name == "Knight":
            return "H"
        elif self.name == "Bishop":
            return "B"
        elif self.name == "Queen":
            return "Q"
        elif self.name == "King":
            return "K"



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
    height = 8*60+10            # Set the screen height

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
            if (len(boxes) + r) % 2 == 0: 
                button = BoardTile(xPos, yPos, length, length, clr.WHITE, r*8+c)
            else:
                button = BoardTile(xPos, yPos, length, length, clr.GRAY,  r*8+c)
            boxes.append(button)    # Add button to list

    return boxes


def generatePieces() -> list:

    pieces = []

    # length = 50
    r = 5
    c = 2
    # xPos = c*(length+10)+10     # X position
    # yPos = r*(length+10)+10     # Y position
    # button = BasicPiece(xPos, yPos, length, length, clr.RED)

    for r, color in {0.8:clr.CYAN, 6.2:clr.MAGENTA}.items():
        
        pawnRow = round(r)

        for c in range(8):
            pieces.append(BasePiece(color, "Pawn", pawnRow*8+c))

        if pawnRow < r:
            r = math.ceil(r)
        else:
            r = math.floor(r)
            
        pieces.append(BasePiece(color, "Rook", r*8))
        pieces.append(BasePiece(color, "Knight", r*8+1))
        pieces.append(BasePiece(color, "Bishop", r*8+2))
        pieces.append(BasePiece(color, "Queen", r*8+3))
        pieces.append(BasePiece(color, "King", r*8+4))
        pieces.append(BasePiece(color, "Bishop", r*8+5))
        pieces.append(BasePiece(color, "Knight", r*8+6))
        pieces.append(BasePiece(color, "Rook", r*8+7))

    return pieces


def updateScreen(tiles, pieces, sideBoards):
    """
    Update the screen during loops

    Inputs:
        buttonsList (list)          : List of game boxes
        flagBox (TextBox)           : Flag info box
        restartButton (PushButton)  : Button for restarts
    """

    window.fill(clr.LIGHTGRAY)          # Clear the screen
    for tile in tiles:              # For each button
        tile.draw()                     # Re-add button
    for piece in pieces:
        tiles[piece.index].drawPiece(piece)
    # for piece in pieces:
    #     piece.draw()                    # Draw flag box
    # sideBoards.draw()               # Draw side boards
    pygame.display.update()         # Update the display





window = createWindow()
tiles  = generateTiles()
pieces = generatePieces()

for piece in pieces:
    tiles[piece.index].drawPiece(piece)




while True:                                             # Run until exitted
    for event in pygame.event.get():                        # Check event type
        if event.type == pygame.QUIT:                           # If quit event
            pygame.quit()                                           # Terminate pygame module
        if event.type == pygame.MOUSEBUTTONDOWN:                # If mouse was pressed
            mousePos = pygame.mouse.get_pos()                      # Get mouse position
            for tile in tiles:
                if tile.is_clicked(mousePos):
                    
                    for piece in pieces:
                        if piece.index == tile.index:
                            piece.vertical(-1)
                            tiles[piece.index].drawPiece(piece)
                            tile.clear()
                            break
                    break
            pass

    updateScreen(tiles, pieces, 0)

