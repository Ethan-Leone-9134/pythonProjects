


#%%%#  Import Statements #%%%#
import webbrowser
# from pynput.keyboard import Controller as kController
# from pynput.keyboard import Listener as kListener
from pynput.keyboard import Key
# from pynput.mouse import Controller as mController
# from pynput.mouse import Button
# from pynput.mouse import Listener as mListener
import time
import cmd
from specialTaps import *
from mouseTest import wait4mouse

#%%%# Custom Functions  #%%%#


#%%%#  Algorithm Functions  #%%%#

def openChrome(incog:str):
    toggleKey(Key.cmd)          # Open search window
    time.sleep(1)
    typeOut("Chrome",0.075)     # Ask for chrome
    time.sleep(5)
    print("--- Chrome Opening ---")

    if incog == "y":
        toggleKey(Key.right)
        toggleKey(Key.down,2,0.05)


    toggleKey(Key.enter)        # Submit chrome requst
    time.sleep(3)
    print("--- Chrome Open ---")

def openMyCourses(passCode):
    typeOut("mycourses.rit.edu/d2l/home",0.025)
    time.sleep(1)
    toggleKey(Key.enter)
    print("--- Login Opening ---")
    wait4mouse()                # Outer login menu
    time.sleep(3)
    print("--- Mycourses log-in started ---")
    typeOut("ejl6690",0.1)
    toggleKey(Key.tab, 1, 0.5)
    typeOut(passCode, 0.025)
    toggleKey(Key.enter, 1, 5)        # Submit request
    print("--- Mycourses log-in ended ---")
    wait4mouse()                # Confirm device
    time.sleep(5)

def openDrive(passCode):
    print("--- G Drive log-in has begun ---")
    ctrlTap("t")
    time.sleep(1)
    typeOut("https://accounts.google.com/v3/signin/identifier?continue=http%3A%2F%2Fdrive.google.com%2F%3Futm_source%3Den&ec=asw-drive-hero-goto&ifkv=AaSxoQwMC2uYsliSUEmEegZrXf13-iLLRzInarslc3LdpkJLUMO5QziliUgUvvoTfCQgXBa8XmwxpA&ltmpl=drive&passive=true&service=wise&usp=gtd&utm_campaign=web&utm_content=gotodrive&utm_medium=button&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S2080984173%3A1714695894854593&theme=mn&ddm=0",0.005)
    toggleKey(Key.enter, 1, 0.025)
    time.sleep(1)
    typeOut("ejl6690@g.rit.edu", 0.05)
    toggleKey(Key.enter, 1, 0.05)
    time.sleep(1)
    typeOut(passCode, 0.05)
    time.sleep(1)
    toggleKey(Key.enter, 1, 0.05)
    print("--- G Drive log-in has ended ---")


#%%%# Main Code  #%%%#

passCode = input("Password (*) : ")
incog = input("Sneaky (y/n) : ")

print("----------------------")
openChrome(incog)           # Open Chrome Application
openMyCourses(passCode)     # Open Mycourses in chrome
openDrive(passCode)         # Open google drive as a new tab
print("--------------------------------")
print(" ")

#%%%#   END  OF  SCRIPT   #%%%#