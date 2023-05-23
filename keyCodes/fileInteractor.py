"""
File Name   :  fileInteraction.py
Author      :  Ethan Leone
Date        :  05/19/2023
Description :  This module is for interacting with filez

Usage:
- Ensure that the required libraries are installed by running 'pip install _______'.
- Update any custom modules.
- Run the script to perform the desired tasks.
"""


import os       # Interact with other files
import json     # Convert dictionaries to files

"""
- File Functions
    - currPath      : Gets the path for the json files
    - getPinList    : Gets the list of keyCodes in use
    - readPin       : Read a json file
    - writePin      : Save a dictionary
"""


def currPath() -> str:
    """
    Function gets the path for the json files
    Inputs:
        none
    Outputs:
        (str)  :   File path for json folder
    """

    filePath = os.path.abspath(__file__)       # Get the absolute path of the current file
    dirPath = os.path.dirname(filePath)        # Get the directory containing the current file
    return str(dirPath + r"\keyFiles")


def getPinList() -> list:
    """
    Function gets the list of keyCodes in use
    Inputs:
        none
    Outputs:
        (list)  :   All keyCodes in use
    """
    files = os.listdir(currPath())                 # Get all files in the current directory
    json_files = [file.replace('.json', '') for file in files if file.endswith('.json')]   # Filter JSON files
    
    return json_files

        
def testPin(pin: str):
    if pin in getPinList():
        return 1
    else:
        return 0


def readPin(pin: str) -> dict:
    filepath = str(currPath()) + r"\{}.json".format(pin)
    
    with open(filepath, "r") as file:    # Load the JSON data from the file
        json_data = file.read()
    dataList = json.loads(json_data)       # Convert JSON string to a list of dictionaries
    keyList = ["Pincode", "Name", "Birthday", "Phone Number", "E-Mail", "Address", "creationDate", "punches"]
    userInfo = {key: dataList.get(key, "") for key in keyList}
    return userInfo


def writePin(pin:str, user: dict):
    json_data = json.dumps(user)
    filepath = str(currPath()) + r"\{}.json".format(pin)
    with open(filepath, "w") as file:
        file.write(json_data)

