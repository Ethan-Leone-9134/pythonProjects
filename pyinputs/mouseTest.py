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

# %%%# Import Statements #%%%#

import webbrowser
from pynput.keyboard import Controller as kController
from pynput.keyboard import Listener as kListener
from pynput.keyboard import Key
from pynput.mouse import Controller as mController
from pynput.mouse import Button
from pynput.mouse import Listener as mListener
import threading



def wait4mouse():

    event = threading.Event()
    listenType = 0
    

    def on_m_click(x, y, button, pressed):
        if pressed and (button == Button.left or button == Button.right):
            nonlocal listenType
            # You can add your desired actions here after the left mouse button is pressed
            event.set()
            listenType = 1
            print("--- Mouse is Pressed ->-")
            return False  # Stop the listener
    
    def on_k_press(key):
        if key == Key.esc:
            nonlocal listenType
            event.set()
            listenType = 2
            print("Escape key pressed")
            return False  # Stop the listener


    print("-<- Waiting on Mouse ---")   

    # Start listeners for both mouse and keyboard
    mouse_listener = mListener(on_move=None, on_click=on_m_click, on_scroll=None)
    mouse_listener.start()

    keyboard_listener = kListener(on_press=on_k_press)
    keyboard_listener.start()

    event.wait()

    # Stop both listeners
    mouse_listener.stop()
    keyboard_listener.stop()

    if listenType == 2:
        listenType = 0
        raise  # Raise the exception to immediately stop the program


mouse = mController()


# %%%# End of File #%%%#
