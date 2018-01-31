import guizero
import easygui
import os
import sys

from guizero import App, Box, TextBox, MenuBar
from easygui import msgbox, textbox
from os import system

#Global variables
thing = [ ]
woof = [ ]

#menubar functions
def File_New():
    easygui.textbox()
    #New file code here
    
def File_Open():
    woof = easygui.diropenbox(msg = None, title = None, default = None)
    
    print(woof)
    #prints var to console for debug
    
    search(woof)
    #executes search function?
    
    fow = open(choice, 'r')
    thing = fow.read()
    progress = thing
    main()
    
def File_Save():
    print("not made yet")
    #Save code here
    
def Edit_Function():
    functionE1 = easygui.msgbox("This part has not been made yet.", title = "Alert", ok_button = "Fine")
#end of menubar functions
    
#Open file functions
def search(retrieve):
    #prints for confirmation on startup of function
    print("retrieval signalled")
    
    os.chdir(retrieve)
    rescue = os.listdir(os.getcwd())
    print(rescue) #for debug
    
    #found = []
    
    currently = os.getcwd()
    msg = ("Chose a file from " + currently)
    title = "Open File"
    choices = rescue                                     #'\n'.join()
    choice = easygui.choicebox(msg, title, choices)
    
    #prints values of variables to console for debugging
    #print(choice, choices, msg, title, retrieve, rescue)
    print("current directory: " + str(os.getcwd()))
    print("choices are " + str(choices))
    print("chosen document: " + str(choice))
    
    
    #opens chosen file
    fow = open(choice, 'r')
    thing = fow.read()
    easygui.textbox(text = thing)

    
    
    

app = App()
guizero.MenuBar(app,
                     toplevel=["File"],
                     options=[
                         [ ["New File", File_New], ["Open File", File_Open], ["Save File", File_Save] ]
                         ])


app.display()

app.on_close(sys.exit([])) #closes app


