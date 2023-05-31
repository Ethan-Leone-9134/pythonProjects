


#%% IMPORT STATEMENTS ###

import os               # For operating system related functionalities
import time             # For time-related operations
import cv2              # For computer vision tasks
import numpy as np      # For numerical operations and array manipulation
import pytesseract      # For optical character recognition (OCR) using Tesseract
from PIL import Image, ImageFilter, ImageEnhance  # For image processing and manipulation
import pathways as path             # Custom file containing file folder pathways
import pyperclip as clip        # Used to copy and paster



#%% Define Functions%%#

def formatImage(imagePath: str) -> Image.Image:
    """
    Function opens and formats a given file
    Inputs:
        imagePath (str) : File path for the image that will be cropped
    Outputs:
        (image)         : Optimized image to scan
    """

    # Open File
    rawimage = Image.open(imagePath)        # Open image as rgba
    image = rawimage.convert('RGB')         # Fix file type to rgb
    pixels = np.array(image)                # Convert image to numpy array

    # Preprocessing for OCR
    grayscale_image = cv2.cvtColor(pixels, cv2.COLOR_RGB2GRAY)
    _, binary_image = cv2.threshold(grayscale_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    # Text enhancement
    sharpened_image = cv2.filter2D(binary_image, -1, kernel=np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]]))  # Sharpen image using a kernel
    enhanced_image = cv2.bitwise_not(sharpened_image)  # Invert the image to make text appear black

    denoised_image = cv2.GaussianBlur(enhanced_image, (3, 3), 0)
    equalized_image = cv2.equalizeHist(denoised_image)
    
    return equalized_image


def getPhrase(typeList: set) -> set:
    """
    Scan input list and add any similar values, also lower case everything

    Inputs :
        typeList (set) - Given list to add onto
    
    Ouputs : 
        phrases  (set) - Final filled up list
    """

    directory = {"fruit": {'apple', 'banana', 'orange', 'grape', 'lime'},
                 "feet": {"soles", "toes", "foot"},
                 "pits": {"sniff", "ripe", "smell", "sweat", "gym"},
                 "BBC" : {"black"},
                 "suck": {"blow"},
                 "cum" : {"facial", "sperm"}
                 }

    phrases = set()                         # Generate set
    for type in typeList:                   # For each input
        phrases.add(type.lower())               # Add input to output
        if type in directory.keys():            # Does input have other possible keywords
            for subValue in directory[type]:        # For each sub value
                phrases.add(subValue)                   # Add to main set

    return phrases


#%% main() %%# 
# Initializations
pytesseract.pytesseract.tesseract_cmd = path.ocr    # Call text reader
np.set_printoptions(threshold=np.inf)               # Prevents truncation of data # type: ignore
print(" ")
indexList = []
pathList = []
phrases = getPhrase({"lick", "feet", "pits"})

truth = time.time()
# Main Loop 
for number in range(1, 120):                            # For each value (Note: Includes low, Excludes Top
    fileName = f"\\IMG_DD_{number:04d}.PNG"
    originPath = path.end + fileName        # File Path
    if os.path.exists(originPath):                              # Does the file exist
        try:
            # alpha = time.time()
            picture = formatImage(originPath)                           # Open image file
            # print(time.time() - alpha)
            title = pytesseract.image_to_string(picture, lang="eng")    # Get text
            # print(time.time() - alpha)
            if any(phrase in title.lower() for phrase in phrases):      # Are any of the phrases in the title
                indexList.append(number)                                    # Add index to list
                pathList.append(fileName)
        except:
            pass

    if number % 5  == 0:  print(number, end="  -  ", flush=True)    # Give output for every 5th iteration
    if number % 25 == 24: print("\n")                               # Break the line

    # print(" ")

outputList = [f"name:{index:04d}" for index in indexList]   # Format the list of indecies
searchStr = ' OR '.join(outputList)                         # Generate desired string

print("\n\n" + searchStr + "\n")  # Print spacer and desired string
clip.copy(searchStr)
print(time.time() - truth)
print(" ")
print(pathList)

