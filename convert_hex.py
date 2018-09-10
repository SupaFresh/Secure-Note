"""This file is for converting the text that is being
typed into hexidecimal"""

import sys
import tkinter as tk
import secure_note as secnote



def hideit():
    for letter in TextBox.value:
        txhx.translate(letter)

def translate(cool):
    
    if cool == "a":
        Textbox.append("1,")
        
    if cool == "b":
        Textbox.append("2,")
        
    if cool == "c":
        Textbox.append("3,")
        
    if cool == "d":
        Textbox.append("4,")
        
    if cool == "e":
        Textbox.append("5,")
        
    if cool == "f":
        Textbox.append("6,")
        
    if cool == "g":
        Textbox.append("7,")
        
    if cool == "h":
        Textbox.append("8,")
        
    if cool == "i":
        Textbox.append("9,")
        
    if cool == "j":
        Textbox.append("10,")
        
    if cool == "k":
        Textbox.append("11,")
        
    if cool == "l":
        Textbox.append("12,")
        
    if cool == "m":
        Textbox.append("13,")
        
    if cool == "n":
        Textbox.append("14,")
        
    if cool == "o":
        Textbox.append("15,")
        
    if cool == "p":
        Textbox.append("16,")
        
    if cool == "q":
        Textbox.append("17,")
        
    if cool == "r":
        Textbox.append("18,")
        
    if cool == "s":
        Textbox.append("19,")
        
    if cool == "t":
        Textbox.append("20,")
        
    if cool == "u":
        Textbox.append("21,")
        
    if cool == "v":
        Textbox.append("22,")
        
    if cool == "w":
        Textbox.append("23,")
        
    if cool == "x":
        Textbox.append("24,")
        
    if cool == "y":
        Textbox.append("25,")
        
    if cool == "z":
        Textbox.append("26,")
        
    if cool == " ":
        Textbox.append("\n")
    
