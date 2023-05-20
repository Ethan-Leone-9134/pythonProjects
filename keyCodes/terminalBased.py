"""
File Name   :  terminalBased.py
Author      :  Ethan Leone
Date        :  5/18/2023
Description :  Uses files to store personel data for key codes with the terminal

Usage:
- Ensure that the required libraries are installed by running 'pip install _______'.
- Update any custom modules.
- Run the script to perform the desired tasks.
"""

import time     # Track time and add delays
import fileInteractor as FI    # Custom module for storage

"""
Function List:
- generateNew
- addPunch
"""


# Terminal

def generateNew(pin: str):
    attributeList = ["Name", "Birthday", "Phone Number"]
    userData = {}  # Dictionary to store attribute-value pairs

    for attribute in attributeList:
        value = input(f"Enter {attribute}: ")
        userData[attribute] = value
    
    userData.update({"Pincode": pin, 
                        "creationDate": round(time.time()), 
                        "punches": [round(time.time())]})

    FI.writePin(pin, userData)        # Save user data


def addPunch(pin: str):
    userData = FI.readPin(pin)                 # Get user's informatino
    userData["punches"].append(round(time.time())) # Add punch to record
    FI.writePin(pin, userData)                 # Save user data


def main():

    print("N - New")                # Ask for interaction type
    print("P - Punch")
    print("S - Set")
    request = input("Enter the key for what you would like to do: ")

    pinList = FI.getPinList()              # Get list of pincodes in use
    pin = input("Input Pin Code: ")     # Ask for pincode

    if request.lower() == 'n':     # New Pincode

        while pin in pinList:     # Keep asking until entry is not in use
            pin = input("Pincode in use, Please try a different one: ")

        generateNew(pin)          # Create new pin
   
    elif request.lower() == 's':            # Set and show values

        while pin not in pinList:           # Keep asking until entry exists
            pin = input("Pincode does not exist, Please try a different one: ")

        userData = FI.readPin(pin)             # Get user's informatino

        for key, value in userData.items():     # Iterate over key-value pairs
            print("{}: {}".format(key, value))      # Output data for each key


        chosenKey = input("Choose a key: ")                 # Ask for key
        userData[chosenKey] = input("State new value: ")    # Ask for value
        FI.writePin(pin, userData)                             # Save user data

    elif request.lower() == 'p':            # Set and show values

        while pin not in pinList:           # Keep asking until entry exists
            pin = input("Pincode does not exist, Please try a different one: ")

        addPunch(pin)



main()
