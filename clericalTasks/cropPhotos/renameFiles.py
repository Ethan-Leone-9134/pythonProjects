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

main = path.end             # Get target pathway
listA = os.listdir(main)    # Get main list
eCount = sum("_CC_" in fileName for fileName in listA)      # Count finished files
print(eCount)               # Display finished files

for fileName in listA:          # For each file
    if "_b_" in fileName:               # if name includes code
        eCount += 1                                 # Increment eCount
        newPath = (main+"\\IMG_CC_{:04d}.PNG".format(eCount))       # Find new file name
        os.rename((main+"\\"+fileName), newPath)        # Set old path to new path
        print(newPath)                              # Display finished files

print(eCount)               # Display finished files
