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
from pynput.keyboard import Controller, Key
import time

#%%%# Custom Functions #%%%#

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

#%%%# Define Input Variables #%%%#

chromeApp = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'  # If window opens but tabs dont, fix this
urlVideo = 'https://www.youtube.com/watch?v=jgm58cbu0kw'
urlMusic = 'https://www.youtube.com/watch?v=_2MOGj5vb-M'
volumeTarget = 40           # Please type with in bounds:  0<x<100
chromePin = 2               # Which number is the chrome tab in your pins at the bottom

#%%%# Main Code #%%%#

keyboard = Controller()                     # Create a keyboard controller
windTap(str(chromePin))                     # Open chrome with windows shortcut
time.sleep(0.5)
ctrlTap("n")                                # Generate new chrome window
print("--- Windows Made ---")
time.sleep(0.5)
webbrowser.get(chromeApp).open(urlMusic)    # Open music Link
print("--- Music Made ---")
time.sleep(3) 
webbrowser.get(chromeApp).open(urlVideo)    # Open Video Link
print("--- Video Made ---")
time.sleep(3)
toggleKey('f')                              # Press and release for full screen
print("--- Fullscreen Now ---")
toggleKey(Key.media_volume_down, 100)                   # Set volume to zero
toggleKey(Key.media_volume_up, int(volumeTarget/2))     # Set volume to target
print("--- Completedad ---")
# keyboard.stop()            # Close the keyboard controller    # DOES NOT WORK

#%%%# End of File #%%%#