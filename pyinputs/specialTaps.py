

from pynput.keyboard import Controller as kController
from pynput.keyboard import Listener as kListener
from pynput.keyboard import Key
import time


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


def toggleKey(key, iterations=1, delay=0.0):
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



def typeOut(typeStr, delay=0.0):
    for let in list(typeStr):
        toggleKey(let,1,delay)
    pass
    time.sleep(delay)


# Establish controllers
keyboard = kController()