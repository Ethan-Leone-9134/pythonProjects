"""
File Name   :  Updated openBackground.py
Author      :  Ethan Leone
Date        :  09/26/2023
Description :  This script opens a new chrome window that will have a music 
               video and a background video playing. The background video will be 
               fullscreened, and volume set to a chosen value.

Usage:
- Ensure that the required libraries are installed by running 'pip install webbrowser pynupt'.
- Update any custom modules.
- Run the script to perform the desired tasks.
"""

#%%%# Import Statements #%%%#

import webbrowser
from pynput.keyboard import Controller as kController
from pynput.keyboard import Listener as kListener
from pynput.keyboard import Key
from pynput.mouse import Controller as mController
from pynput.mouse import Button
from pynput.mouse import Listener as mListener
import time
import threading


class EscapeKeyPressed(Exception):
    pass

event = threading.Event()

#%%%# Keyboard Functions #%%%#

def ctrlTap(hitKey):
    """
    Function does a "CTRL + key"
    Inputs:
        hitkey (key)   : key that is being pressed after the CTRL
    Outputs:
        none (Keyboard is Affected)
    """

    keyboard.press(Key.ctrl)        # Press     CTRL
    keyboard.press(hitKey)          # Press     Key
    keyboard.release(hitKey)        # Release   Key
    keyboard.release(Key.ctrl)      # Release   CTRL


def shftTap(hitKey):
    """
    Function does a "SHFT + key"
    Inputs:
        hitkey (key)   : key that is being pressed after the SHFT
    Outputs:
        none (Keyboard is Affected)
    """

    keyboard.press(Key.shift)       # Press     SHFT
    keyboard.press(hitKey)          # Press     Key
    keyboard.release(hitKey)        # Release   Key
    keyboard.release(Key.shift)     # Release   SHFT


def ctrlShftTap(hitKey):
    """
    Function does a "CTRL + key"
    Inputs:
        hitkey (key)   : key that is being pressed after the CTRL
    Outputs:
        none (Keyboard is Affected)
    """

    keyboard.press(Key.ctrl)        # Press     CTRL
    keyboard.press(Key.shift)       # Press     Shift
    keyboard.press(hitKey)          # Press     Key
    keyboard.release(hitKey)        # Release   Key
    keyboard.release(Key.shift)     # Release   Shift
    keyboard.release(Key.ctrl)      # Release   CTRL


def windTap(hitKey):
    """
    Function does a "Windows + key"
    Inputs:
        hitkey (key)   : key that is being pressed after the Windows Key
    Outputs:
        none (Keyboard is Affected)
    """

    keyboard.press(Key.cmd)         # Press     Windows
    keyboard.press(hitKey)          # Press     Key
    keyboard.release(hitKey)        # Release   Key
    keyboard.release(Key.cmd)       # Release   Windows


def toggleKey(key, iterations=1, delay=0):
    """
    Function press and release some key with possible variations
    Inputs:
        key (Key)        : Key being hit
        iterations (int) : How many times to press the key
        delay (float)    : Allows for a pause between presses
    Outputs:
        none (Keyboard is Affected)
    """

    for i in range(iterations):     # Repeat once for each "iteration"
        keyboard.press(key)             # Press the key
        keyboard.release(key)           # Release the key
        time.sleep(delay)               # Delay if requested


def keyFun(function:None, waitTime, string=""):
    # function
    if string != "":
        print(" ".join(["---",string,"---"]))
    time.sleep(waitTime)


def typeOut(typeStr):
    for let in list(typeStr):
        toggleKey(let,1,0.04)
    pass
    time.sleep(0.5)


#%%%# Delay Functions  #%%%#

def on_m_click(x, y, button, pressed):
    if pressed and button == Button.left:
        # print('Left mouse button pressed at position (x={}, y={})'.format(x, y))
        # You can add your desired actions here after the left mouse button is pressed
        event.set()
        print("--- Mouse Pressed ---")
        return False  # Stop the listener

def on_k_press(key):
    if key == Key.esc:

        event.set()
        print(123)
        print("--*-- Escape Pressed --*--")
        raise EscapeKeyPressed("Escape key pressed")



def wait4mouse():
    print("--- Waiting on Mouse ---")

    try:
        # Start listeners for both mouse and keyboard
        mouse_listener = mListener(on_move=None, on_click=on_m_click, on_scroll=None)
        mouse_listener.start()

        keyboard_listener = kListener(on_press=on_k_press)
        keyboard_listener.start()

        # Wait until the event is set or EscapeKeyPressed is raised
        while not event.is_set():
            pass

        # Join both listeners to the main thread
        mouse_listener.stop()
        keyboard_listener.stop()
        
    except EscapeKeyPressed as e:
        print(23456)
        print("Error:", e)



#%%%#  Other Functions  #%%%#

def frac2num(fraction_str):
    try:
        numerator, denominator = map(int, fraction_str.split('/'))
        result = numerator / denominator
        return result
    except ValueError:
        print("Invalid fraction format. Please provide the fraction in the format 'numerator/denominator'.")
        return 0
    except ZeroDivisionError:
        print("Cannot divide by zero.")
        return 0



def getData():
    appPin = 7               # Which number is the chrome tab in your pins at the bottom

    # Data inputs
    partNum = input("What is the part number: ")
    shape = "1/4-20"
    len = input("Screw Length (fraction): ")
    screwType = "Socket Head Screw"

    # Get Document Name (L=Decimal)
    docName = [shape, "x", "{:.03f}".format(frac2num(len)), " ", screwType]
    docName = "".join(docName)

    # Get Decription (L=Fraction)
    docDesc = [shape, "x", len, " ", screwType]
    docDesc = "".join(docDesc)

    return appPin, partNum, docName, docDesc


def importFromMcMC(pin, partNum, docName, docDesc):

    # Keypresses
    keyFun(windTap(str(pin)), 0.5)
    keyFun(windTap(Key.up), 0.5, "Fusion Opened")
    keyFun(ctrlTap("n"), 0.5, "New Studio Made")
    keyFun(ctrlShftTap("m"), 0.5 ,"McMaster Opened")

    # Fill in search box
    wait4mouse()
    typeOut(partNum)
    keyFun(toggleKey(Key.enter),0.5,"Item Searched")

    # Wait for the download click
    wait4mouse()
    time.sleep(4)
    keyFun(toggleKey(Key.enter), 0.5, "Item Imported")

def formatStudio(pin, partNum, docName, docDesc):
    
    # Save studio
    keyFun(ctrlTap("s"), 0.5)
    typeOut(docName)
    keyFun(toggleKey(Key.enter), 0.5, "Studio Saved")

    # Open studio properties
    wait4mouse()
    toggleKey(Key.down, 13, 0.025)
    keyFun(toggleKey(Key.enter), 0.5, "Properties Opened")

    # Part number
    wait4mouse()
    keyFun(ctrlTap("a"), 0.5)
    typeOut("MCC: ")
    typeOut(partNum)

    # Part description
    wait4mouse()
    keyFun(ctrlTap("a"), 0.5)
    typeOut(docDesc)
    keyFun(toggleKey(Key.enter), 0.5, "Properties Saved")

    # Save studio
    keyFun(ctrlTap("s"), 0.5)
    typeOut("Properties Updated")
    keyFun(toggleKey(Key.enter), 0.5, "Studio w/ Prop. Saved")


#%%%# Main Code #%%%#

# Establish controllers
keyboard = kController()
mouse = mController()

pin, partNum, docName, docDesc = getData()
importFromMcMC(pin, partNum, docName, docDesc)
formatStudio(pin, partNum, docName, docDesc)

time.sleep(0.5)
print("--- Completedad ---")

#%%%# End of File #%%%#