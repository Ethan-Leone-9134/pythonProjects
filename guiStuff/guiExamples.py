from PyQt5.QtGui import (QPainter, QColor, QBrush, QFont, QPalette, QIcon)
from PyQt5.QtCore import (Qt, QSize, QCoreApplication)
from PyQt5.QtWidgets import (
    QApplication, QDesktopWidget, QMainWindow, QPushButton, QLabel,
    QTextEdit, QCheckBox, QVBoxLayout, QLineEdit, QHBoxLayout, QFrame,
    QScrollArea, QWidget
)
import sys



class widgetEx(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Create a vertical layout for the frame and its widgets
        frame_layout = QVBoxLayout()

        # Create a QFrame with a box shape
        frame = QFrame(self)
        frame.setFrameShape(QFrame.Box)
        frame.setLineWidth(2)
        frame.setStyleSheet("background-color: %s;" % QColor("cyan").name())

        # Create a QLabel and a QLineEdit
        label = QLabel("Name:", frame)
        line_edit = QLineEdit(frame)

        # Add the widgets to the frame layout
        frame_layout.addWidget(label)
        frame_layout.addWidget(line_edit)

        # Set the frame layout
        frame.setLayout(frame_layout)

        # Set the geometry of the frame
        frame.setGeometry(100, 50, 200, 100)

        # Set the main window layout
        main_layout = QHBoxLayout()
        main_layout.addWidget(frame)
        self.setLayout(main_layout)

        self.setWindowTitle('Frame Example')
        self.show()


class CircularButtonEx(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Set the button's default size
        self.setFixedSize(50, 50)

        # Set the button's background color and border style
        self.setStyleSheet('''
            QPushButton {
                background-color: #F44336;
                border-style: none;
                border-radius: 25px;
                }
            QPushButton:hover {
                background-color: #E57373;
                }
            ''')

    def paintEvent(self, event):
        # Draw a circle on the button's background
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QBrush(QColor('#F44336')))
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(0, 0, self.width(), self.height())

        # Call the parent class's paintEvent method to draw the button's text and icon
        super().paintEvent(event)


class ScrollBoxEx(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        vbox = QVBoxLayout(self)

        for i in range(30):
            hBox = QHBoxLayout()
            label1 = QTextEdit('Label {}'.format(i), self)
            label1.setMaximumHeight(30)
            label2 = QTextEdit('Hola: {}'.format(i), self)
            label2.setMaximumHeight(30)

            hBox.addWidget(label1)
            hBox.addWidget(label2)

            vbox.addLayout(hBox)


        scroll = QScrollArea(self)
        scroll.setWidgetResizable(True)

        widget = QWidget()
        widget.setLayout(vbox)

        scroll.setWidget(widget)

        vbox_scroll = QVBoxLayout(self)
        vbox_scroll.addWidget(scroll)

        button = QPushButton('Button')
        vbox_scroll.addWidget(button)

        self.setLayout(vbox_scroll)

        self.setWindowTitle('Scroll Box Example')
        self.show()


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
        self.winSize = [self.screen.width(), self.screen.height()]  # Window dimensions
        self.setGeometry(
            0, 0, self.winSize[0], self.winSize[1]
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





if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex1 = widgetEx()

    button = CircularButtonEx()
    button.show()

    ex2 = ScrollBoxEx()

    ex3 = PushButtonEx()
    ex3.show()

    sys.exit(app.exec_())
