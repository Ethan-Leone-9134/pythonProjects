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
        self.text = " "
        self.textColor = text_color
        self.opened = False
        self.index = index
        self.layerNumber = 0
        self.flagged = False


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
        if not(self.flagged):
            self.opened = True
            if self.underText == " ":
                self.color = clr.LIGHTGRAY
            elif self.underText == "1":
                self.color = clr.GREEN
            elif self.underText == "2":
                self.color = clr.TEAL
            elif self.underText == "3":
                self.color = clr.CYAN
            elif self.underText == "4":
                self.color = clr.BLUE
                self.textColor = clr.WHITE
            elif self.underText == "5":
                self.color = clr.NAVY
            elif self.underText == "6":
                self.color = clr.PURPLE
            elif self.underText == "M":
                self.color = clr.RED

            self.text = self.underText


    def layer(self, layerNum: int):
        """
        Add a layer number 
        """
        self.layerNumber = layerNum         # Set layer number


    def mine(self):
        """
        Set to text to mine value
        """
        self.underText = "M"            # Set under mine


    def addNeighbor(self):
        """
        Add 1 to the surrounding indicator
        """

        if self.underText == " ":
            self.underText = "0"
        if self.underText != "M":
            self.underText = str(int(self.underText) + 1)


    def flag(self):
        """
        Handle adding flags        
        """

        self.flagged = not(self.flagged)    # Flip flagged variable
        if self.flagged:                    # Is the box being flagged
            self.text = "F"                     # Update display
            self.color = clr.GOLD
        else:                               # Is the box being unflagged
            self.text = " "                     # Update display
            self.color = clr.GRAY


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



class TextBox:
    def __init__(self, x, y, width, height, color, bombs, text_color):
        """
        Button class represents a clickable button in Pygame.

        Args:
            x (int): The x-coordinate of the top-left corner of the button.
            y (int): The y-coordinate of the top-left corner of the button.
            width (int): The width of the button.
            height (int): The height of the button.
            color (tuple): The color of the button in RGB format.
            bombs (int): The number of bombs
            text_color (tuple): The color of the text in RGB format.
        """
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.flags = bombs
        self.bombs = bombs
        self.text = f"Flags : {self.flags} / {self.bombs}"
        self.text_color = text_color

    def draw(self):
        """
        Draw the button on the Pygame window.
        """
        pygame.draw.rect(window, self.color, self.rect)         # Draw the button rectangle
        font = pygame.font.Font(None, 32)                       # Set the font for the button text
        text = font.render(self.text, True, self.text_color)    # Render the button text
        text_rect = text.get_rect(center=self.rect.center)      # Position the text at the center of the button
        window.blit(text, text_rect)                            # Draw the text on the window

    def place(self):
        if self.flags > 0:
            self.flags -= 1
            self.text = f"Flags : {self.flags} / {self.bombs}"

    def lift(self):
        if self.flags >= 0:
            self.flags += 1
            self.text = f"Flags : {self.flags} / {self.bombs}"

    def winner(self):
        self.rect.width = int(self.rect.width*1.5)
        self.text = f"Flags : {self.flags} / {self.bombs} - Victory"
        self.color = clr.GREEN



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
    height = size*60+10+100            # Set the screen height

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


def addMines(size: int, buttonsList: list, quantity: int) -> tuple[list, list]:
    """
    Add all mines and update surrounding values

    Inputs:
        size (int)          : number of columns and rows in the game
        buttonsList (list)  : list of push buttons
        quantity (int)      : how many mines will be placed
    
    Outputs: 
        buttonsList (list)  : list of push buttons 
    """

    mines = []          # Initialize list that contains positions of the mines

    # Generate mine locations
    while len(mines) < quantity:
        mineNum = random.randint(0, size**2-1)      # Determine the position of the current mine
        if mineNum not in mines:
            mines.append(mineNum)

    # Add mines and neighbors
    for mineNum in mines:                       # For each mine        
        buttonsList[mineNum].mine()                 # Set the position to a mine
        for currPos in getSurrounding(mineNum, size):
            buttonsList[currPos].addNeighbor()          # Add one to the boxes value

    mines.sort() 
    return buttonsList, mines


def addLayers(size: int, buttonsList: list) -> list:

    # Generate blanks list
    blanks = []
    for block in buttonsList:
        if block.underText == " ":
            blanks.append(block.index)

    # Match touching rows
    rows = []
    current_row = [blanks[0]]  # Start a new row with the first value from blanks
    rows.append(current_row)  # Add the first row to the rows list
    for i in range(1, len(blanks)):
        if blanks[i] == current_row[-1] + 1 and blanks[i] % size != 0:
            current_row.append(blanks[i])           # Add value if not next to something bad
        else:
            # Otherwise, start a new row with the current value
            current_row = [blanks[i]]
            rows.append(current_row)  # Add the new row to the rows list


    columnsOne = merge_lists_with_difference(rows, size)
    columnsOne = alternate_and_append(columnsOne)
    columnsTwo = merge_lists_with_difference(columnsOne, size)
    columnsThree = merge_lists_with_difference(columnsTwo, size)
    # print(columnsThree)
    # print(" --- ")


    i = 1
    for layer in columnsThree:
        for boxNumber in layer:
            buttonsList[boxNumber].layer(i)

        i += 1

    


    # groups = mergeNestedLists(cols)
    # print(groups)

    return buttonsList



#%% Define iterated Functions %%#

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


def mergeNestedLists(cols: list) -> list:
    """
    Concatenates all third order list items into one second order list
    """
    groups = []
    for grouping in cols:
        currGroup = []
        for row in grouping:
            for value in row:
                currGroup.append(value)
        groups.append(currGroup)

    return groups


def merge_lists_with_difference(your_list, difference):
    merged_lists = []

    for sublist in your_list:
        if not merged_lists:
            merged_lists.append(sublist)
        else:
            last_merged = merged_lists[-1]
            if any(abs(value - element) == difference for value in last_merged for element in sublist):
                merged_lists[-1].extend(sublist)
            else:
                merged_lists.append(sublist)

    return merged_lists


def alternate_and_append(original_list):
    alternate_list = original_list[::2]  # Get every other value
    remaining_list = original_list[1::2]  # Get the remaining values
    alternate_list.extend(remaining_list)  # Append the remaining values to the alternate list
    return alternate_list


def getSurrounding(source, size):

    surrounding = []

    for r in range(-1, 2):                      # For each row
        for c in range(-1, 2):                      # For each col
            currPos = source + c*size + r              # position of the box to be updated
            if checkValid(currPos, size, source):      # If the current position is valid
                surrounding.append(currPos)
    
    surrounding.remove(source)

    return surrounding


#%% Main Program %%#

size = random.randint(7, 12)
# bombs = random.randint(10, 15)
bombs = 4

window = createWindow(size)
buttonsList = generateButtons(size)
buttonsList, mineList = addMines(size, buttonsList, bombs)
buttonsList = addLayers(size, buttonsList)
flagBox = TextBox(60, size*60+20, 60*3, 50, clr.LAVENDER, bombs, clr.BLACK)
flagList = []

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
                    if not(block.flagged):                                   # If not flagged
                        block.update()                                          # Remove cover
                        if block.underText == "M":                              # If mine
                            running = False                                         # Kill loop
                        if block.underText == " ":                              # If blankspace
                            for block2 in buttonsList:
                                if block.layerNumber == block2.layerNumber:
                                    block2.update()
                            pass
                        break                                                   # End loop

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                for block in buttonsList:                                 # For each button
                    mouse_pos = pygame.mouse.get_pos()                      # Get mouse position
                    if block.is_clicked(mouse_pos):                         # If current button was pressed
                        if not(block.opened):
                            
                            if not(block.flagged):
                                if flagBox.flags != 0:
                                    block.flag()
                                    flagBox.place()
                                    flagList.append(int(block.index))
                            else:
                                block.flag()
                                flagBox.lift()
                                flagList.remove(int(block.index))

                            if flagBox.flags == 0:
                                flagList.sort()
                                if mineList == flagList:
                                    running = False
                                    flagBox.winner()

    
    window.fill(clr.WHITE)          # Clear the screen
    for block in buttonsList:       # For each button
        block.draw()                    # Re-add button
    flagBox.draw()
    
    pygame.display.update()     # Update the display

# Finish screen
window.fill(clr.WHITE)          # Clear the screen
for block in buttonsList:       # For each button
    block.finish()                  # Uncover
flagBox.draw()

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
