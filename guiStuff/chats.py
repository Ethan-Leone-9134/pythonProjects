"""
File Name   :  chats.py
Author      :  [Me]
Date        :  MM/DD/YYYY
Description :  This script is meant to generate a read-only text message ui. 

Usage:
- Ensure that the required libraries are installed by running 'pip install _______'.
- Update any custom modules.
- Run the script to perform the desired tasks.
"""

import math
import time
from PyQt5.QtGui import (QPainter, QColor, QBrush, QFont, QPalette, QIcon, QFontMetrics)
from PyQt5.QtCore import (Qt, QSize, QCoreApplication)
from PyQt5.QtWidgets import (
    QApplication, QDesktopWidget, QMainWindow, QPushButton, QLabel,
    QTextEdit, QCheckBox, QVBoxLayout, QLineEdit, QHBoxLayout, QFrame,
    QScrollArea, QWidget
)
import sys


def examine(txt, fontNum):
    
    widget = QWidget()
    widget.setStyleSheet('''QTextEdit{
                border-style: none;
                border-radius: 10px;
                font-family: Verdana;
                font-size: 16px;
                padding: 10px;
                }
            ''')
    font = QFont('Verdana', int(fontNum))                   # Create a QFont object with the desired font properties
    widget.setFont(font)                                    # Set the font for the widget
    text = txt.strip()                                      # Text whose length you want to measure
    font_metrics = QFontMetrics(font)                       # Create a QFontMetrics object to measure text
    text_width = font_metrics.boundingRect(text).width()    # Measure the text width in pixels
    text_width = int((text_width+100)/2)
    textHeight = 30

    if text_width > 300:
        textHeight = math.ceil(text_width/300)*33
        text_width = 250
        

    return text, text_width, textHeight+20


class ScrollBoxEx(QWidget):

    def __init__(self, texts):
        super().__init__()
        self.screen = QDesktopWidget().screenGeometry()             # Find screen dimensions
        self.winSize = [self.screen.width()/3, self.screen.height()/1.5]  # Window dimensions
        self.setGeometry(
            100, 100, int(self.winSize[0]), int(self.winSize[1])
        )                                                           # Set figure dimensions to screen size
        self.setWindowTitle("Chats Simulator")                         # Create figure window name
        # self.setWindowIcon(QIcon(r"C:\Users\zaper\Downloads\pokerIcon.jpg"))

        if isinstance(texts, chatLog):
            self.texts = list(texts)[0]
        else:
            self.texts = texts



        # self.button = QPushButton('Button', self)          # Generate button
        # self.button.setGeometry(100,100,200,100)
        # self.button.clicked.connect(self.initUI())

        self.initUI()
    

    def initUI(self):

        vbox = QVBoxLayout(self)            # Initialize scrollbox storing widget

        boxStyle = (                        # Default Box Type
            '''QTextEdit{           
                border-style: none;
                border-radius: 10px;
                font-family: Verdana;
                font-size: 16px;
                padding: 10px;
                }''')

        # print(type(self.texts))
        for current in list(self.texts):               # For every given text dictionary
            hBox = QHBoxLayout()                # Generate a line layout for this text

            [string,width,height] = examine(current["Text"],16)     # Pull data from the dictionary

            if (current["Type"] == "R"):
                label1 = QTextEdit(string, self)            # Initialize the "text" box
                label1.setStyleSheet(boxStyle+'''QTextEdit{background-color: #87CEEB;}''')  # Null
                label1.setFixedWidth(width)
                label2 = QTextEdit('', self)                # Initialize the "blank"
                label2.setAlignment(Qt.AlignRight)
                label2.setFontPointSize(6)
                
            elif (current["Type"] == "S"):
                label1 = QTextEdit('', self)
                label2 = QTextEdit(string, self)
                label2.setStyleSheet(boxStyle+'''QTextEdit{background-color: #EAA11B;}''')  # Null
                # label2.setStyleSheet(boxStyle+'''QTextEdit{background-color: #EE4B2B;}''')  # Safe
                label2.setFixedWidth(width)

            else:
                label1 = QTextEdit('', self)
                label1.setMaximumWidth(1)
                label2 = QTextEdit(string, self)

            label1.setMaximumHeight(height)     # Set label heights
            label2.setMaximumHeight(height)     

            hBox.addWidget(label1)
            hBox.addWidget(label2)

            vbox.addLayout(hBox)


        scroll = QScrollArea(self)              # Generate a scroll area
        scroll.setWidgetResizable(True)         # Allow the scroll area to be resizable

        widget = QWidget()                      # Generate a widget
        widget.setLayout(vbox)                  # Add the text info to a holder widget
        scroll.setWidget(widget)                # Add the widget onto the scroll area

        vbox_scroll = QVBoxLayout(self)         # Generate layout
        vbox_scroll.addWidget(scroll)           # Add the scroll area to the layout
        
        scroll.verticalScrollBar().setValue(    # Start the chats from the bottom
        scroll.verticalScrollBar().maximum())

        self.setLayout(vbox_scroll)             # Place the layout onto the window. 
        self.setStyleSheet('''QWidget{
                background-color: #707070;
                border-style: none;
                border-radius: 25px;
                }
            ''')
        

class PushButtonEx(QMainWindow):    # Creates figure window object
    """
    Class [Description]
    Attributes:
        name (type) : [Description]
    Methods:
        name        : [Description]
    """

    def __init__(self):                                         # Names the figure window as "self"
        super().__init__()                                          # Gives figure window its properties
        self.screen = QDesktopWidget().screenGeometry()             # Find screen dimensions
        self.winSize = [self.screen.width()/5, self.screen.height()/2]  # Window dimensions
        self.setGeometry(
            100, 100, int(self.winSize[0]), int(self.winSize[1])
        )                                                           # Set figure dimensions to screen size
        self.setWindowTitle("Basic Window")                         # Create figure window name
        self.setWindowIcon(QIcon(r"C:\Users\zaper\Downloads\pokerIcon.jpg"))


        # create push button
        self.button = QPushButton("Click me!", self)        # Create push button object
        self.button.setGeometry(100, 100, 200, 50)          # Set dimensions for pushbutton
        self.button.clicked.connect(self.on_button_click)   # Sets callback


    def on_button_click(self):      # Define button callback
        print("Button clicked!")    # Say that the button was clicked
    
    def keyPressEvent(self, event):
        code = event.key()
        modifiers = event.modifiers()
        currPin = (str(self.pinBox.text())).split(' - ')      # Split into array
        if (code > 64) & (code < 91):       # Letter
            letter = chr(code)
            print(f"Letter: {letter}")
        elif (code > 47) & (code < 58):     # Number
            print(f"Number: {code-48}")
        elif code == 16777219:              # Backspace
            print("Backspace")
        elif code == 16777220:              # Enter
            print("Enter")   
        else:                               # Other
            print(code)


def timeCheck(inp=""):
    print(f"{round(time.time() - ALPHA, 8)} -:- {inp}")





from chatDatas import AlphaPred69 as textData
from chatDatas import chatLog

ALPHA = time.time()



if __name__ == '__main__':
    app = QApplication(sys.argv)

    # ex3 = PushButtonEx()
    # ex3.show()

    timeCheck("Pre Class")

    ex2 = ScrollBoxEx(textData)
    
    timeCheck("Post Class")
    ex2.show()

    timeCheck("Final")

    sys.exit(app.exec_())