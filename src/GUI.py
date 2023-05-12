import tkinter as tk
from tkinter import *
import subprocess
from acceptMatch import *
import os
import time
from header import *
from autoReport import *
from autoCait import *
from acceptAndPick import *
import webbrowser

def start_game():
    # Create a new window for input
    input_window = tk.Toplevel(root)
    input_window.title("Input Window")

    # Create the input fields and labels
    champ_label = tk.Label(input_window, text="Champion to play:")
    champ_entry = tk.Entry(input_window)
    ban_label = tk.Label(input_window, text="Champion to ban:")
    ban_entry = tk.Entry(input_window)

    # Create a button to start the game
    start_button = tk.Button(input_window, text="Start Game", command=lambda: start_game_with_champs(champ_entry.get(), ban_entry.get()))

    # Add the input fields, labels, and button to the window
    champ_label.pack()
    champ_entry.pack()
    ban_label.pack()
    ban_entry.pack()
    start_button.pack()

def report_enemies():
    alert_window = tk.Toplevel(root)
    alert_window.title("Alert")
    alert_button = tk.Button(alert_window, text="IN DEVELOPING")
    
    alert_button.pack()

def macro_cait():
    alert_window = tk.Toplevel(root)
    alert_window.title("Alert")
    alert_button = tk.Button(alert_window, text="IN DEVELOPING")
    
    alert_button.pack()


def start_game_with_champs(champ_to_play, champ_to_ban):
    print(champ_to_play,champ_to_ban)
    subprocess.call([AutoAccept_Two(champ_to_play, champ_to_ban)])
    
    
def auto_accept():
    subprocess.call([aramAccept()])
    
def search_runes():
    input_window = tk.Toplevel(root)
    input_window.title("Search Runes")
    
    champ_label = tk.Label(input_window, text="Champion to search:")
    champ_entry = tk.Entry(input_window)
    search_button = tk.Button(input_window, text="Search", command=lambda: openSite(champ_entry.get()))


    champ_label.pack()
    champ_entry.pack()
    search_button.pack()
    
    
    
def openSite(string):
    temporaryStr = list(string.split(" "))
    final_Str = "-".join(temporaryStr)
    
    url = "https://www.runas.lol/"+final_Str
    webbrowser.open(url)

# Create the GUI window and buttons
root = tk.Tk()
root.title("AutoClicker")

button1 = tk.Button(root, text="Auto-Accept Match + Choose Champion", command=start_game)
button2 = tk.Button(root, text="Report All Enemies", command=report_enemies)
button3 = tk.Button(root, text="Macro Cait", command=macro_cait)
button4 = tk.Button(root, text="Just Accept Match",command=auto_accept)
button5 = tk.Button(root, text= "Search Runes", command=search_runes)

button1.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()


# mainloop
def startGui():
    root.geometry("200x200")
    root.iconphoto(False, tk.PhotoImage(file='icon.png'))
    root.mainloop()
    



