# Import necessary packages
import sys
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QMainWindow, QPushButton, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QCoreApplication, Qt
import time
import math

### Start Figure Window Code ###
class MyWindow(QMainWindow):    # Creates figure window object
    def __init__(self):         # Names the figure window as "self"
        super().__init__()      # Gives figure window its properties
        self.screen = QDesktopWidget().screenGeometry()                 # Find screen dimensions
        self.winSize = [self.screen.width(), self.screen.height()]      # Window dimensions
        self.setGeometry(0, 0, self.winSize[0], self.winSize[1])        # Set figure dimensions to screen size
        self.setWindowTitle("Clock")          # Create figure window name

        ##### Start Main Code #####

        self.valid = 1               # Loop condition for clock
        self.remTime = 20*60         # Time remaining in current round
        self.roundMinutes = 20       # Minutes per round

        self.createPushButtons()    # Create the push buttons

        # create timeClock
        self.timeClock = QLabel("", self)
        self.showTime(self.remTime)
        self.timeClock.setGeometry(200, 100, self.winSize[0]-400, 600)
        self.timeClock.setFont(QFont("Arial", 250))
        self.timeClock.setAlignment(Qt.AlignCenter)

    #####  End main code  #####
    ##### Start functions #####


    def showTime(self, seconds):
        minsLeft = math.floor(seconds/60)       # Calculate remaining whole minutes
        secLeft = seconds - minsLeft*60         # Calculate remaining seconds
        if seconds <= 0:                        # If time is up
            self.nextRound()                        # End current round
        if secLeft < 10:                        # If seconds has only 1 digit
            secLeft = "0" + str(secLeft)            # Give leading zero
        else:
            secLeft = str(secLeft)
        self.timeClock.setText(str(minsLeft)+":"+secLeft)
        QCoreApplication.processEvents()

    def mainLoop(self):
        while self.valid:    # While the loop condition is true
            start = time.time()     # Find time at start of iteration
            while time.time() < start + 1:       # Run nested-loop for one second
                QCoreApplication.processEvents()         # As a delay, update all boxes
            if self.valid:          # Ensure loop condition still true
                self.nextSec()           # Update time
            print(self.remTime)
            print(self.valid)

    def createPushButtons(self):    # Function to create all push button objects


        ### Second Change ###
        # create backSecondButton
        self.backSecButton = QPushButton("+", self)             # Create push button object
        self.backSecButton.setGeometry(self.winSize[0]-200, 300, 100, 100)        # Set dimensions for pushbutton
        self.backSecButton.clicked.connect(self.backSec)        # Sets callback
        self.backSecButton.setFont(QFont("Arial", 30))          # Set font

        # create nextSecondButton
        self.nextSecButton = QPushButton("-", self)             # Create push button object
        self.nextSecButton.setGeometry(self.winSize[0]-200, 500, 100, 100)        # Set dimensions for pushbutton
        self.nextSecButton.clicked.connect(self.nextSec)        # Sets callback
        self.nextSecButton.setFont(QFont("Arial", 30))          # Set font

        ### Minute Change ###
        # create backMinuteButton
        self.backMinButton = QPushButton("+", self)             # Create push button object
        self.backMinButton.setGeometry(100, 300, 100, 100)        # Set dimensions for pushbutton
        self.backMinButton.clicked.connect(self.backMin)        # Sets callback
        self.backMinButton.setFont(QFont("Arial", 30))          # Set font

        # create nextMinuteButton
        self.nextMinButton = QPushButton("-", self)             # Create push button object
        self.nextMinButton.setGeometry(100, 500, 100, 100)        # Set dimensions for pushbutton
        self.nextMinButton.clicked.connect(self.nextMin)        # Sets callback
        self.nextMinButton.setFont(QFont("Arial", 30))          # Set font

        # create playPauseButton
        self.playPauseButton = QPushButton("⏵", self)           # Create push button
        self.playPauseButton.setGeometry(int((self.winSize[0])/2)-50, 700, 100, 100)      # Set dimensions for pushbutton
        self.playPauseButton.clicked.connect(self.playPause)    # Sets callback
        self.playPauseButton.setFont(QFont("Arial", 30))          # Set font

    #####   End Normal Functions   #####
    ##### Start Callback Functions #####

    def nextSec(self):                      # Define button callback
        self.remTime = self.remTime - 1     # Increment time
        self.showTime(self.remTime)         # Display new time

    def backSec(self):                      # Define button callback
        self.remTime = self.remTime + 1     # Increment time
        self.showTime(self.remTime)         # Display new time

    def nextMin(self):                      # Define button callback
        self.remTime = self.remTime - 60    # Increment time
        self.showTime(self.remTime)         # Display new time

    def backMin(self):                      # Define button callback
        self.remTime = self.remTime + 60    # Increment time
        self.showTime(self.remTime)         # Display new time

    def playPause(self):
        if self.playPauseButton.text() == "⏵":
            self.playPauseButton.setText("▐▐")
            self.mainLoop()
        elif self.playPauseButton.text() == "▐▐":
            self.valid = 0
            self.playPauseButton.setText("⏵")

    ##### End callback functions #####
### End Figure window code ###


if __name__ == '__main__':          # If statement locks the foloowing code to this script file, rather than being called somewhere else
    app = QApplication(sys.argv)    #
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
