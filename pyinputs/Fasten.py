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
from specialTaps import *
from mouseTest import wait4mouse


#%%%# Keyboard Functions #%%%#


def keyFun(function:None, waitTime, string=""):
    # function
    if string != "":
        print(" ".join(["---",string,"---"]))
    time.sleep(waitTime)




#%%%#  Other Functions  #%%%#

def frac2num(fraction_str):
    if " " in fraction_str:  # Check if mixed fraction
        whole_part, fraction_part = fraction_str.split(' ')
        whole_part = int(whole_part)
        numerator, denominator = map(int, fraction_part.split('/'))
        result = whole_part + (numerator / denominator)
        return result
    elif "/" in fraction_str:  # Handle fractions without whole part
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
    else:
        return int(fraction_str)  # Handle integers


#%%%# Main Algorithm Functions #%%%#

def getData():
    appPin = 6               # Which number is the chrome tab in your pins at the bottom    ( 6 - After Excel)

    screwData = {"thread1": "8-32", 
                 "thread2": "10-32", 
                 "thread3": "1/4-20", 
                 "thread4": "", 
                 "thread5": "1/2-20",
                 "type1"  : "Button Head Screw",
                 "type2"  : "Countersink Screw",
                 "type3"  : "Socket Head Screw",
                 "type4"  : "Washer",
                 "type5"  : "Nut"}

    shape = screwData["thread3"]
    screwType = screwData["type1"]

    # Data inputs
    partNum = input("What is the part number: ")
    if "mcmaster" in partNum:
        partNum = partNum.replace("https://www.mcmaster.com/","")
        partNum = partNum.replace("/","")

    if "Screw" in screwType:                # Handle screws of variable length
        # Get Screw type
        len = input("Screw Length (fraction): ")

        # Get Document Name (L=Decimal)
        docName = [shape, "x", "{:.04f}".format(frac2num(len)), " ", screwType]
        docName = "".join(docName)

        # Get Decription (L=Fraction)
        docDesc = [shape, "x", len, " ", screwType]
        docDesc = "".join(docDesc)
    else:                                   # Handle nuts/washers
        diam, thr = shape.split("-")
        docName = [diam, " ", screwType]
        docName = "".join(docName)
        docDesc = docName

    return appPin, partNum, docName, docDesc

def importFromMcMC(pin, partNum):

    # Keypresses
    keyFun(windTap(str(pin)), 0.5)
    keyboard.press(Key.cmd)
    toggleKey(Key.up,3,0.5)
    toggleKey(Key.down,1,1)
    toggleKey(Key.up,1,1)
    keyFun(keyboard.release(Key.cmd), 1, "Fusion Opened")
    keyFun(ctrlTap("n"), 0.5, "New Studio Made")
    keyFun(ctrlShftTap("m"), 0.5 ,"McMaster Opened")

    # Fill in search box
    wait4mouse()
    typeOut(partNum,0.05)
    keyFun(toggleKey(Key.enter),0.5,"Item Searched")

    # Wait for the download click
    wait4mouse()
    wait4mouse()
    wait4mouse()
    time.sleep(5)
    keyFun(toggleKey(Key.enter), 0.5, "Item Imported")

def formatStudio(pin, partNum, docName, docDesc):
    
    # Save studio
    time.sleep(1)
    keyFun(ctrlTap("s"), 0.5)
    typeOut(docName,0.05)
    keyFun(toggleKey(Key.enter), 0.5, "Studio Saved")

    # Open studio properties
    wait4mouse()
    time.sleep(0.25)
    toggleKey(Key.down, 13, 0.05)
    keyFun(toggleKey(Key.enter), 0.5, "Properties Opened")

    # Part number
    wait4mouse()
    keyFun(ctrlTap("a"), 0.5)
    typeOut("McMC: ",0.05)
    typeOut(partNum,0.05)

    # Part description
    wait4mouse()
    keyFun(ctrlTap("a"), 0.5)
    typeOut(docDesc, 0.05)
    wait4mouse()
    time.sleep(1)
    # keyFun(toggleKey(Key.enter), 0.5, "Properties Saved")

    # Save studio
    keyFun(ctrlTap("s"), 0.5)
    typeOut("Properties Updated",0.05)
    keyFun(toggleKey(Key.enter), 0.5, "Studio w/ Prop. Saved")

def minimize():

    # Wait for exit
    wait4mouse()
    keyboard.press(Key.cmd)
    toggleKey(Key.down,3,1)
    keyFun(keyboard.release(Key.cmd), 1, "Fusion Minimized")




#%%%# Main Code #%%%#

# Establish controllers
keyboard = kController()
mouse = mController()

print(" ")
print("---------------------")
pin, partNum, docName, docDesc = getData()
importFromMcMC(pin, partNum)
formatStudio(pin, partNum, docName, docDesc)
minimize()

time.sleep(0.5)
print("--- Completedad ---")
print("-------------------")
print(" ")

#%%%# End of File #%%%#