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
import re
import pathways as path

def renameFile(folder, start, end, inList=[]):

    adjustDirectory(folder, end)

    listA = os.listdir(folder)    # Get main list
    eCount = sum(end in fileName for fileName in listA)      # Count finished files
    print(eCount)               # Display finished files

    if len(inList) == 0:
        searchList = listA
    else:
        searchList = inList


    for fileName in searchList:          # For each file
        if ((start in fileName) & (end not in fileName)):               # if name includes code
            eCount += 1                                 # Increment eCount
            newPath = (folder+f"\\IMG{end}{eCount:04d}.PNG")       # Find new file name
            os.rename((folder+ "\\"+fileName), newPath)        # Set old path to new path
            print(newPath)                              # Display finished files

    print(eCount, end="\n\n")               # Display finished files



def adjustDirectory(folder, end):
    searchList = os.listdir(folder)    # Get main list
    existing_files = [fileName for fileName in searchList if end in fileName]
    if len(existing_files) > 0:
        existing_files.sort()
        finalNumber = re.findall(r"(\d+)", existing_files[-1])[-1]
        missing_files = [f"{i:04d}" for i in range(1, int(finalNumber)) if f"IMG{end}{i:04d}.PNG" not in existing_files]

        while len(missing_files) != 0:
            filename = f"IMG{end}{missing_files[0]}.PNG"
            missingPath = os.path.join(folder, filename)
            lastPath = os.path.join(folder, existing_files[-1])
            os.rename(lastPath, missingPath)

            searchList = os.listdir(folder)    # Get main list
            existing_files = [fileName for fileName in searchList if end in fileName]
            existing_files.sort()
            finalNumber = re.findall(r"(\d+)", existing_files[-1])[-1]
            missing_files = [f"{i:04d}" for i in range(1, int(finalNumber)) if f"IMG{end}{i:04d}.PNG" not in existing_files]
            




# renameFile(path.end)
renameFile(path.end, "_b_", "_DD_")
renameFile(path.end, "_M_", "_DD_")
renameFile(path.end, "_mmm", "_MU_")
renameFile(path.start, "_", "_a_")
