import tkinter as tk
from tkinter import *
import subprocess
from Lol import header as h

def start_game():

    input_window = tk.Toplevel(root)
    input_window.title("Input Window")

    champ_label = tk.Label(input_window, text="Champion to play:")
    champ_entry = tk.Entry(input_window)
    ban_label = tk.Label(input_window, text="Champion to ban:")
    ban_entry = tk.Entry(input_window)
    start_button = tk.Button(input_window, text="Start Game", command=lambda: start_game_with_champs(champ_entry.get(), ban_entry.get()))

    champ_label.pack()
    champ_entry.pack()
    ban_label.pack()
    ban_entry.pack()
    start_button.pack()

def start_game_with_champs(champ_to_play, champ_to_ban):
    print(champ_to_play,champ_to_ban)
    subprocess.call([h.AutoAccept_Match(champ_to_play, champ_to_ban)])
    
def search_runes():
    input_window = tk.Toplevel(root)
    input_window.title("Search Runes")
    
    champ_label = tk.Label(input_window, text="Champion to search:")
    champ_entry = tk.Entry(input_window)
    lane_label = tk.Label(input_window, text="Lane")
    lane_entry = tk.Entry(input_window)
    search_button = tk.Button(input_window, text="Search", command=lambda: h.open_runeSite(champ_entry.get(), lane_entry.get()))

    lane_label.pack()
    lane_entry.pack()
    champ_label.pack()
    champ_entry.pack()
    search_button.pack()
    
    
root = tk.Tk()
root.title("AutoClicker")

button1 = tk.Button(root, text="Auto-Accept Match", command=start_game)
button5 = tk.Button(root, text= "Search Runes", command=search_runes)

button1.pack()
button5.pack()


def startGui():
    root.geometry("200x200")
    root.mainloop()
    



