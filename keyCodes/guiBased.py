"""
File Name   :  guiBased.py
Author      :  Ethan Leone
Date        :  5/19/2023
Description :  Uses files to store personel data for key codes with an application window

Usage:
- Ensure that the required libraries are installed by running 'pip install _______'.
- Ensure that the custom 'fileInteractor' module is installed
- Run the script to perform the desired tasks.
"""

# Import Statements
from PyQt5 import QtGui
from PyQt5.QtGui import (QPainter, QColor, QBrush, QFont, QPalette, QIcon)
from PyQt5.QtCore import (Qt, QSize, QCoreApplication)
from PyQt5.QtWidgets import (
    QApplication, QDesktopWidget, QMainWindow, QPushButton, QLabel,
    QTextEdit, QCheckBox, QVBoxLayout, QLineEdit, QHBoxLayout, QFrame,
    QScrollArea, QWidget
)
import sys
import time
import fileInteractor as FI    # Custom module for storage
from datetime import datetime

#%% Window Classes ###



class primeWindow(QMainWindow):     # Creates primary window object
    """
    Class generates the primary pincode entering window
    Attributes:
        winSize (list)      : 1x2 list of w and h of window
        pinBox (QLabel)     : Pin code typing area
        letterInfo (QLabel) : Explains key press values
        validCode (QLabel)  : Informational window about entered code
    Methods:
        keyPressEvent   : Handles keyboard presses
        punchEntered    : Adds a punch to the pin file
        infoReq         : Opens the information window
        newPin          : Generate an empty pin
        resetScreen     : Clear the old pin from screen
    """
    
    def __init__(self):         # Names the figure window as "self"
        super().__init__()      # Gives figure window its properties
        self.screen = QDesktopWidget().screenGeometry()                 # Find screen dimensions
        self.winSize = [self.screen.width(), self.screen.height()]      # Window dimensions
        self.setGeometry(0, 0, self.winSize[0], self.winSize[1])        # Set figure dimensions to screen size
        self.setWindowTitle("Passcodes")          # Create figure window name
        
        self.pinBox = centeredLabel("_ - _ - _ - _", 50, self)      # Main pincode typing area
        self.pinBox.setGeometry(700, 400, 600, 100)

        self.letterInfo = centeredLabel("Enter - Punch \n  I - Info\n N - New", 20, self)    # Explain key press values   
        self.letterInfo.setGeometry(1500, 50, 300, 350)

        self.validCode = centeredLabel("  ", 25, self)              # Informational window about entered code
        self.validCode.setGeometry(500, 500, 1000, 100)


    def keyPressEvent(self, event):
        """
        Handles key presses
        Inputs:
            event : key press event item
        Outputs:
            none : change a file or window
        """
        
        code = event.key()
        modifiers = event.modifiers()
        currPin = (str(self.pinBox.text())).split(' - ')      # Split into array

        if code == 16777219:              # Backspace
            for i in range(1,5):
                if currPin[-i] != "_":
                    currPin[-i] = "_"
                    break
            self.pinBox.setText(' - '.join(currPin))          # Set label
            self.validCode.setText("   ")
        elif '_' in currPin:            # If there is room for another number
            if (code > 47) & (code < 58):     # Number
                currPin[currPin.index('_')] = str(code - 48)    # Set earlist _ to input
                self.pinBox.setText(' - '.join(currPin))          # Set label
                if '_' not in currPin:
                    if FI.testPin(''.join(currPin)):    # If pin in folder
                        self.validCode.setText("Pin Code Recognized")
                    else:                               # If pin not in folder
                        self.validCode.setText("Pin Code Not Recognized")
        else:                           # If the code is full and usable
            if FI.testPin(''.join(currPin)):
                if code == 16777220:              # Enter
                    self.punchEntered(''.join(currPin))
                elif code == 73:                   # Letter I
                    self.infoReq(''.join(currPin))
            else:
                if code == 78:                   # Letter N
                    self.newPin(''.join(currPin))


    def punchEntered(self, pin:str):
        """
        Handle pressing of enter when all values are filled
        Inputs: 
            pin (str) : pincode to have a punch added
        Outputs:
            none : change a file or window
        """

        if pin == "9999":                   # If admin
            self.admin = adminWindow()          # Open admin window
            self.admin.show()                   # Show admin window
            while self.admin.isVisible():       # Wait for the info window to be closed
                QApplication.processEvents()        # Process events while waiting
        else:
            userData = FI.readPin(pin)                 # Get user's information
            currTime = datetime.fromtimestamp(round(time.time())).strftime("%A, %B %d, %Y %I:%M:%S")    # Format time
            command = f'{userData["Name"]} : {currTime}'        # Generate displayed text
            self.validCode.setText(command)                     # Display text
            userData["punches"].append(round(time.time()))      # Add punch to record
            FI.writePin(pin, userData)                          # Save user data
        self.resetScreen()                   # Clear pin


    def infoReq(self, pin:str):
        """
        Generate the information request window
        Inputs: 
            pin (str) : pincode to have a info changed
        Outputs:
            none : change a file or window
        """

        self.infoWindow = infoWindow(pin)       # Open the information window
        self.infoWindow.show()                  # Display the window
        while self.infoWindow.isVisible():      # Wait for the info window to be closed
            QApplication.processEvents()            # Process events while info is open
        

    def newPin(self, pin: str):
        """
        Generate a new file
        Inputs: 
            pin (str) : pincode to be created
        Outputs:
            none : change a file or window
        """

        attributeList = ["Name", "Birthday", "Phone Number", "E-Mail", "Address"]
        userData = {attribute: "" for attribute in attributeList}       # Set all user values to " "

        newValues = {
            "Pincode": pin,                         # Get pincode
            "creationDate": round(time.time()),     # Set create date
            "punches": [round(time.time())]         # Add a punch
        }
        userData.update(newValues)                  # Add fixed values to userdata
        FI.writePin(pin, userData)                  # Save user data
        self.infoReq(pin)                           # Open info request window
        self.resetScreen()                          # Reset the screen


    def resetScreen(self):
        """
        Reset the screen to default
        Inputs : none
        Outputs : none
        """

        QApplication.processEvents()            # Process anything in buffers
        time.sleep(2)                           # 2-second delay
        self.pinBox.setText("_ - _ - _ - _")    # Overwrite pincode typing area
        self.validCode.setText(" ")             # Clear pin info



class infoWindow(QMainWindow):      # Creates information window object
    """
    Class generates the information entering window
    Attributes:
        winSize (list)              : 1x2 list of w and h of window
        userInfo (dict)             : Dictionary containing the user info
        valueBoxes (list)           : List of input boxes
        mainLayout (QLayout)        : Information box area
        saveButton (QPushButton)    : Button to save and close the window
    Methods:
        createBoxes     : Generate all informational boxes
        basicDataLabel  : Generate a label next to a text box
        savePin         : Save the user info to the json file
    """
    
    def __init__(self, pin:str):                             # Names the figure window as "self"
        super().__init__()                                  # Gives figure window its properties
        self.screen = QDesktopWidget().screenGeometry()                 # Find screen dimensions
        self.winSize = [self.screen.width(), self.screen.height()]      # Window dimensions
        self.setGeometry(0, 0, self.winSize[0], self.winSize[1])        # Set figure dimensions to screen size
        self.setWindowTitle("User Information")                              # Create figure window name

        self.userInfo = FI.readPin(pin)         # Get the user's info from their file
        self.createBoxes()                      # Generate the informational boxes

        self.saveButton = QPushButton("Save and Return!", self)     # Create save button object
        self.saveButton.setGeometry(1500, 525, 200, 50)             # Set dimensions for pushbutton
        self.saveButton.clicked.connect(self.savePin)               # Sets callback


    def createBoxes(self):
        """
        
        """
        self.valueBoxes = []
        infoWidget = QWidget(self)                   # Create a widget for the layout to exist in
        self.mainLayout = QVBoxLayout(infoWidget)    # Create a vertical layout for the parent widget

        self.basicDataLabel("Key code", self.userInfo["Pincode"])   # Key code

        for key in ["Name", "Birthday", "Phone Number", "E-Mail", "Address"]:   # Most "input" data
            self.basicDataLabel(key, self.userInfo[key], 1)         # Generate box

        createDate = datetime.fromtimestamp(self.userInfo["creationDate"]).strftime("%A, %B %d, %Y %I:%M:%S")   # Format create date
        self.basicDataLabel("Creation Date", createDate)            # Generate create date box

        infoWidget.setGeometry(50, 50, int(self.winSize[0]*0.6), self.winSize[1]-200)        # Set the size and position of the central widget relative to the screen


    def basicDataLabel(self, key, value, edit=0):
        """
        
        """
        lineUp = QHBoxLayout()                          # Create a horizontal layout to hold the label and text box

        label = QLabel(key)                             # Create a QLabel for displaying the key
        label.setFont(QFont("Arial", 25))
        label.setFixedHeight(int(self.winSize[1]/12))   # Set positions
        label.setFixedWidth(int(self.winSize[0]/5))
        label.setStyleSheet("border: 2px dashed red")

        if edit:
            textBox = QTextEdit(value)                  # Create a QTextEdit widget if in edit mode
        else:
            textBox = QLabel(value)                     # Create a QLabel widget if not in edit mode
        textBox.setFont(QFont("Arial", 25))
        textBox.setFixedHeight(int(self.winSize[1]/12))

        lineUp.addWidget(label)                         # Add the label widget to the layout
        lineUp.addWidget(textBox)                       # Add the text box widget to the layout
        self.valueBoxes.append(textBox)                 # Append the text box widget to the list for later reference
        self.mainLayout.addLayout(lineUp)               # Add the lineUp layout to the main layout

        
    def savePin(self):
        """
        
        """

        keys = ["Name", "Birthday", "Phone Number", "E-Mail", "Address"]    # List of keys to save values from
        for index, key in enumerate(keys, 1):               # For each value in keys
            value = self.valueBoxes[index].toPlainText()        # Get new value to value of edit box
            self.userInfo[key] = value                          # Set new value

        FI.writePin(self.userInfo["Pincode"], self.userInfo)    # Save the file
        self.close()                                            # Close the window



class adminWindow(QMainWindow):     # Creates adminastrative window object
    """
    Class generates the primary pincode entering window
    Attributes:
        winSize (list)      : 
        pinBox (QLabel)     : 
        letterInfo (QLabel) : 
        validCode (QLabel)  : 
    Methods:
        onPassPress     : Handles password enter press
        basicDataLabel  : Generate a label next to a text box
        openSearch      : Generate the search bar and info boxes
    """

    def __init__(self):                             # Names the figure window as "self"
        super().__init__()                                  # Gives figure window its properties
        self.screen = QDesktopWidget().screenGeometry()                 # Find screen dimensions
        self.winSize = [self.screen.width(), self.screen.height()]      # Window dimensions
        self.setGeometry(0, 0, self.winSize[0], self.winSize[1])        # Set figure dimensions to screen size
        self.setWindowTitle("Admin Information")                        # Create figure window name

        self.titleBar = QLabel(self)                                    # Generate Instructions
        self.titleBar.setText("Enter Password and Press Enter")         # Set label text
        self.titleBar.setFont(QFont("Arial", 20))                       # Set Font
        self.titleBar.setGeometry(100, 50, 600, 50)                     # Set position
        
        self.passWord = QLineEdit(self)                                 # Passwords box
        self.passWord.setFont(QFont("Arial", 20)) 
        self.passWord.setGeometry(100, 100, int(self.winSize[0]*0.3), 100)
        self.passWord.returnPressed.connect(self.onPassPress)           # Declare enter command
        

    def onPassPress(self):   
        """
        Handles changing screen when correct password is entered
        """     
        if self.passWord.text() == "":                  # If it is the password
            self.searchBar = QLineEdit(self)                        # Place searchbar
            self.searchBar.setFont(QFont("Arial", 20)) 
            self.searchBar.setGeometry(100, 100, int(self.winSize[0]*0.3), 100)
            self.searchBar.show()                                   # Update screen
            # self.searchBar.returnPressed.connect()                  # Set search enter command

            self.passWord.deleteLater()                             # Delete password box
            self.titleBar.setText("Type name here")                      # Overwrite title

            fullList = []
            for pinNumber in FI.getPinList():
                fullList.append(FI.readPin(pinNumber))

            self.masterList = sorted(fullList, key=lambda x: str(x["Name"]))     # Sort by name value

            searchList = QVBoxLayout(self)
            for tag in self.masterList:
                currItem = KeyCodeButton(tag)
                currItem.clicked.connect(self.openSearch)
                searchList.addWidget(currItem)

            scroll = QScrollArea(self)                      # Create scroll area
            scroll.setWidgetResizable(True)
            widget = QWidget()
            widget.setLayout(searchList)
            scroll.setWidget(widget)
            scroll.setGeometry(100, 300, int(self.winSize[0]*0.3), 500)
            scroll.show()

            centralWidget = QWidget(self)                   # Create a central widget for the main window

            self.mainLayout = QVBoxLayout(centralWidget)  # Create a vertical layout for the central widget
            self.valueBoxes = []
            self.basicDataLabel("Key code", " ")
            for key in ["Name", "Birthday", "Phone Number", "E-Mail", "Address"]:
                self.basicDataLabel(key, " ")
            self.basicDataLabel("Creation Date", " ")

            centralWidget.setGeometry(int(self.winSize[0]*0.4), 50, int(self.winSize[0]*0.6), self.winSize[1]-200)        # Set the size and position of the central widget
            centralWidget.show()
    

    def basicDataLabel(self, key, value, edit=0):
        """
        Method adds a label to the display layout
        Inputs:
            key (str) 
        """
        lineUp = QHBoxLayout()

        label = QLabel(key)
        label.setFont(QFont("Arial", 22))
        label.setFixedHeight(int(self.winSize[1]/12))
        label.setFixedWidth( int(self.winSize[0]/5))
        label.setStyleSheet("border: 2px dashed red")
        
        if edit:
            textBox = QTextEdit(value)
        else:
            textBox = QLabel(value)
        textBox.setFont(QFont("Arial", 25))
        textBox.setFixedHeight(int(self.winSize[1]/12))

        lineUp.addWidget(label)
        lineUp.addWidget(textBox)
        self.valueBoxes.append(textBox)
        self.mainLayout.addLayout(lineUp)
        

    def openSearch(self):
        """
        Sets the display boxes to the value off the pressed box
        """
        value = self.sender()                               # Get the pressed box data
        user = value.open()                                  # type: ignore  # Open the json file
        self.valueBoxes[0].setText(str(user["Pincode"]))         # Set display box 1 value 
        self.valueBoxes[1].setText(str(user["Name"]))
        self.valueBoxes[2].setText(str(user["Birthday"]))
        self.valueBoxes[3].setText(str(user["Phone Number"]))
        self.valueBoxes[4].setText(str(user["E-Mail"]))
        self.valueBoxes[5].setText(str(user["Address"]))
        


#%% Widget Classes ###



class KeyCodeButton(QPushButton):
    """
    Custom QPushButton used to stores a user info dictionary
    """
    def __init__(self, user: dict):
        """
        Initialize the KeyCodeButton.
        Input:  user (dict): A dictionary containing user information.
        """
        super().__init__()                  # Include pushbutton props
        self.user = user                    # Set input as a property
        self.setText(str(user["Name"]))     # Set the name
        self.setFont(QFont("Arial", 16))    # Set the font

    def open(self) -> dict:
        """
        Get the pin code associated with the button.
        Outputs: user (dict) : A dictionary containing user information.
        """
        return self.user



class centeredLabel(QLabel):
    """
    Custom QLabel that generates centered
    Note: this is done as its own class definition to simplify the disabling of the Qt.AlignCenter error
    """
    def __init__(self, text: str, font: int, parent):
        """
        Initializes the centerLabel class
        Inputs:
            text (str) - Text to be displayed
            font (int) - Font size
            parent (object) - Parent object
        """
        super().__init__(text, parent)              # Give normal QLabel props
        self.setAlignment(Qt.AlignCenter)           # Set horizontally centered       # type: ignore
        self.setFont(QFont("Arial", font))          # Set font size to input



#%% main() ###


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wind = primeWindow()
    wind.show()
    sys.exit(app.exec_())
