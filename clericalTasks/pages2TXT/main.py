
import os
import pydoc

import docx
from docx import Document
import convertapi
import PyPDF2

def getTextWord(fileName):
    doc = docx.Document(fileName)  # Get file information
    fullTxt = []  # Initialize text storing variable
    valid = 1  # Initialize varied font logical
    for temp in doc.paragraphs:  # For each paragraph
        fullTxt.append(temp.text)  # Add text to variable
        for temp2 in temp.runs:  # For each paragraph's font data
            # print(temp.text)
            if temp2.font.bold is True:
                valid = 0
            if temp2.font.italic is True:
                valid = 0
            if temp2.font.underline is True:
                valid = 0
            if temp.alignment is not None:
                valid = 0

    return '\n'.join(fullTxt), valid

# def getTextPages(fileName):
#     convertapi.api_secret = '<YOUR SECRET HERE>'
#     txt = convertapi.convert('txt', {'File': fileName}, 'pages')
#     return txt

def getTextPages(fileName):
    txt = PyPDF2.PdfFileReader(fileName)
    return txt


def word2txtDoc(fileName):
    [oldText, valid] = getTextWord(fileName)
    print(valid)
    if valid:
        rplName = fileName.replace(".docx",", Edited.docx")
        newPath = fileName.replace(".docx",".txt")  # File Path
        newDoc = open(newPath, "w")
        newDoc.write(oldText)
        # os.rename(fileName, rplName)


max = 1
min = 0
totalRange = max - min
for num in range(totalRange):
    numb = min + num
    filep = r"C:\Users\zaper\Downloads\OG PAGES DOCS\Found, G , F\testout23.docx"
    # getTextWord(filep)
    word2txtDoc(filep)


print('Complete')



