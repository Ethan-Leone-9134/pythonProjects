import sys
import math
import os


def start():
    # Function enables tracking of the terminal output
    # Inputs  : none
    # Outputs : none
    # Globals : none

    # Note: Code came from ChatGPT


    class Tee:
        """
        Tee object that captures output to both stdout and a file.
        """
        def __init__(self, filename, stream):
            self.file = open(filename, 'a')
            self.stream = stream

        def __del__(self):
            self.file.close()

        def write(self, data):
            self.file.write(data)
            self.file.flush()
            self.stream.write(data)

        def flush(self):
            self.file.flush()
            self.stream.flush()

    # Define the log file path
    log_file_path = "outputLogs.txt"

    # Create a file object for the log file
    log_file = open(log_file_path, 'w')

    # Create a Tee object to capture output to both stdout and the log file
    tee = sys.stdout = Tee(log_file_path, sys.stdout)


def Print(inputText):
    # Provides formatted output for important information
    # Inputs  : none
    # Outputs : none
    # Globals : none

    
    dashLen = 50                                                    # Number of dashes
    breakLine = "-" * dashLen                                       # Create the breakline
    inputText = str(inputText)
    with open("outputLogs.txt", 'r') as f:       # Open the log file
        lines = f.readlines()                                           # Read the last line
        if "-------" not in lines[-1].strip():                          # If there was no breakline above
            print(breakLine)                                                # Add a breakline
        textLength = len(inputText)                                     # Length of input
        sides = math.floor((dashLen - textLength - 2) / 2)              # Finds amount of side dashes
        sides = '-' * sides                                             # Generates side walls
        if textLength % 2 == 0:                                         # If text length is even
            print(sides + " " + inputText + " " + sides)                    # Normal formatted print
        else:                                                           # If text length is odd
            print(sides + " " + inputText + " -" + sides)                   # Formatted print with an extra dash
        print(breakLine)                                                # Print ending breakline


def close():
    os.remove("outputLogs.txt")
