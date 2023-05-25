import pygame
import random
import colors as clr


#%% Define Classes #%%
class Button:
    def __init__(self, x, y, width, height, color, index, text_color):
        """
        Button class represents a clickable button in Pygame.

        Inputs:
            x (int)             : The x-coordinate of the top-left corner of the button.
            y (int)             : The y-coordinate of the top-left corner of the button.
            width (int)         : The width of the button.
            height (int)        : The height of the button.
            color (tuple)       : The color of the button in RGB format.
            index (int)         : The index of the button in the list
            text_color (tuple)  : The color of the text in RGB format.
        """
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.underText = " "
        self.text = "C"
        self.textColor = text_color
        self.opened = False
        self.index = index

    def draw(self):
        """
        Draw the button on the Pygame window.
        """

        pygame.draw.rect(window, self.color, self.rect)         # Draw the button rectangle
        font = pygame.font.Font(None, 32)                       # Set the font for the button text
        text = font.render(self.text, True, self.textColor)    # Render the button text
        text_rect = text.get_rect(center=self.rect.center)      # Position the text at the center of the button
        window.blit(text, text_rect)                            # Draw the text on the window


    def is_clicked(self, mouse_pos):
        """
        Check if the button is clicked based on the mouse position.

        Args:
            mouse_pos (tuple): The current position of the mouse.

        Returns:
            bool: True if the button is clicked, False otherwise.
        """
        
        return self.rect.collidepoint(mouse_pos)
    

    def update(self):
        self.opened = True
        self.color = (195, 195, 195)
        self.text = self.underText
        pass


    def mine(self):
        self.underText = "M"


    def addNeighbor(self):
        if self.underText == " ":
            self.underText = "0"
        if self.underText != "M":
            self.underText = str(int(self.underText) + 1)


    def layer(self, layerNum: int):
        self.layerNumber = layerNum



#%% Define Flow Functions %%#

def createWindow(size: int):
    """
    Generate a pygame figure window

    Inputs:
        size (int) : number of columns and rows in the game

    Outputs: 
        window (pygame display) : main window for the program
    
    """
    
    pygame.init()           # Initialize Pygame

    width = size*60+10             # Set the screen width
    height = size*60+10            # Set the screen height

    window = pygame.display.set_mode((width, height))       # Create the window
    pygame.display.set_caption("My Pygame Window")          # Set the title

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
            # button = Button(xPos, yPos, length, length, clr.GRAY, str(r*size+c), clr.BLACK)
            button = Button(xPos, yPos, length, length, clr.GRAY, (r*size+c), clr.BLACK)
            boxes.append(button)    # Add button to list

    return boxes


def addMines(size: int, buttonsList: list, quantity: int) -> list:
    """
    Add all mines and update surrounding values

    Inputs:
        size (int)          : number of columns and rows in the game
        buttonsList (list)  : list of push buttons
        quantity (int)      : how many mines will be placed
    
    Outputs: 
        buttonsList (list)  : list of push buttons 
    """

    mines = [size, size - 1]          # Initialize list that contains positions of the mines

    while len(mines) < quantity:
        mineNum = random.randint(0, size**2-1)      # Determine the position of the current mine
        if mineNum not in mines:
            mines.append(mineNum)
            print(mineNum)

    for mineNum in mines:                       # For each mine        
        buttonsList[mineNum].mine()                 # Set the position to a mine
        for r in range(-1, 2):                      # For each row
            for c in range(-1, 2):                      # For each col
                currPos = mineNum + c*size + r              # position of the box to be updated
                if checkValid(currPos, size, mineNum):      # If the current position is valid
                    buttonsList[currPos].addNeighbor()          # Add one to the boxes value

    return buttonsList


def addLayers(size: int, buttonsList: list) -> list:

    # Generate blanks list
    blanks = []
    for block in buttonsList:
        if block.underText == " ":
            blanks.append(block.index)
    print(blanks)

    # Match touching rows
    rows = []
    rows.append([blanks[0]])
    while len(blanks) > 1:
        if blanks[0] + 1 == blanks[1] and blanks[0] % size != size-1:
            rows[-1].append(blanks[1])
        else:
            rows.append([blanks[1]])
        blanks.remove(blanks[0])
    rows.append([blanks[0]])
    print(rows)



    return buttonsList



#%% Define iterated Functions%%#

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


#%% Main Program %%#

size = 10
bombs = 10

window = createWindow(size)
buttonsList = generateButtons(size)
buttonsList = addMines(size, buttonsList, bombs)
buttonsList = addLayers(size, buttonsList)

# Game loop
running = True
while running:                                          # Run with loop condition
    for event in pygame.event.get():                        # For each event
        if event.type == pygame.QUIT:                           # If quit
            running = False                                         # Set loop condition to false
        elif event.type == pygame.MOUSEBUTTONDOWN:              # If a mouse button is pressed
            mouse_pos = pygame.mouse.get_pos()                      # Get mouse position
            for block in buttonsList:                                 # For each button
                if block.is_clicked(mouse_pos):                         # If current button was pressed
                    block.update()                                          # Remove cover
                    if block.underText == "M":                              # If mine
                        running = False                                         # Kill loop
                    if block.underText == " ":                              # If blankspace
                        pass
                    break                                                   # End loop

    
    window.fill(clr.WHITE)          # Clear the screen
    for block in buttonsList:       # For each button
        block.draw()                    # Re-add button
    
    pygame.display.update()     # Update the display

# Finish screen
window.fill(clr.WHITE)          # Clear the screen
for block in buttonsList:       # For each button
    block.update()                  # Uncover
    block.draw()                    # Update gui

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
