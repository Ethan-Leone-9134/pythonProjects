"""
File Name   :  Updated renameFiles.py
Author      :  [Me]
Date        :  5/19/2023
Description :  This script renames all files.

Usage:
- Update the 'pathways' module with the correct file folder pathways.
- Run the script to perform the desired image processing tasks.
"""

import os
import pathways as path

def renameFile(folder, start, end):
    listA = os.listdir(folder)    # Get main list
    eCount = sum(end in fileName for fileName in listA)      # Count finished files
    print(eCount)               # Display finished files

    for fileName in listA:          # For each file
        if (start in fileName) & (end not in fileName):               # if name includes code
            eCount += 1                                 # Increment eCount
            newPath = (folder+f"\\IMG{end}{eCount:04d}.PNG")       # Find new file name
            os.rename((folder+ "\\"+fileName), newPath)        # Set old path to new path
            print(newPath)                              # Display finished files

    print(eCount)               # Display finished files



renameFile(path.end, "_b_", "_CC_")
renameFile(path.start, "_", "_5_")