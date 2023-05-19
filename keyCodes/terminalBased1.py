"""
File Name   :  terminalBased1.py
Author      :  Ethan Leone
Date        :  5/18/2023
Description :  This script performs image processing on multiple files, moving them from a start to end folder.

Usage:
- Ensure that the required libraries are installed by running 'pip install _______'.
- Update any custom modules.
- Run the script to perform the desired tasks.
"""

import time
import os
import json


def currPath() -> str:
    file_path = os.path.abspath(__file__)       # Get the absolute path of the current file
    return os.path.dirname(file_path)        # Get the directory containing the current file

def getPinList():
    files = os.listdir(currPath())                 # Get all files in the current directory
    json_files = [file.replace('.json', '') for file in files if file.endswith('.json')]   # Filter JSON files
    
    return json_files


class personData:
    def __init__(self, pin):
        self.name = input("User Name: ")
        self.birthday = input("Birthday: ")
        self.pin = pin
        self.createDate = time.time()
        self.punches = [time.time()]

    def punchIn(self):
        self.punches += [time.time()]


        
def readPin(pin: str) -> dict:
    filepath = str(currPath()) + r"\{}.json".format(pin)
    
    with open(filepath, "r") as file:    # Load the JSON data from the file
        json_data = file.read()
    data_list = json.loads(json_data)       # Convert JSON string to a list of dictionaries
    return data_list


def writePin(pin:str, user: dict):
    json_data = json.dumps(user)
    filepath = str(currPath()) + r"\{}.json".format(pin)
    with open(filepath, "w") as file:
        file.write(json_data)




def main():

    print("N - New")                # Ask for interaction type
    print("P - Punch")
    print("S - Set")
    request = input("Enter the key for what you would like to do: ")

    pinList = getPinList()              # Get list of pincodes in use
    pin = input("Input Pin Code: ")     # Ask for pincode

    if request.lower() == 'n':    # New Pincode

        while pin in pinList:               # Keep asking until entry is not in use
            pin = input("Pincode in use, Please try a different one: ")

        user = personData(pin)              # Generate class object
        writePin(pin, user.__dict__)        # Save user data
   
    elif request.lower() == 's':            # Set and show values

        while pin not in pinList:           # Keep asking until entry exists
            pin = input("Pincode does not exist, Please try a different one: ")

        userData = readPin(pin)             # Get user's informatino

        for key in userData:                # Output data for each key
            print("{}: {}".format(key, userData[key]))

        chosenKey = input("Choose a key: ")                 # Ask for key
        userData[chosenKey] = input("State new value: ")    # Ask for value
        writePin(pin, userData)                             # Save user data

    elif request.lower() == 'p':            # Set and show values

        while pin not in pinList:           # Keep asking until entry exists
            pin = input("Pincode does not exist, Please try a different one: ")

        userData = readPin(pin)                 # Get user's informatino
        userData["punches"].append(round(time.time())) # Add punch to record
        writePin(pin, userData)                 # Save user data



main()
