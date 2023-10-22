import tkinter as tk
import ttkwidgets.autocomplete as ttka
from tkinter import ttk
import subprocess
from Lol import AcceptMatch, Runes
from tft import geneticAlgorithm as ga

campeoes_lol = [
    "aatrox", "ahri", "akali", "akshan", "alistar", "amumu", "anivia", "annie", "aphelios", "ashe",
    "aurelion sol", "azir", "bard", "bel'veth", "blitzcrank", "brand", "braum", "briar", "caitlyn",
    "camille", "cassiopeia", "cho'gath", "corki", "darius", "diana", "dr. mundo", "draven", "ekko",
    "elise", "evelynn", "ezreal", "fiddlesticks", "fiora", "fizz", "galio", "gangplank", "garen", "gnar",
    "gragas", "graves", "gwen", "hecarim", "heimerdinger", "illaoi", "irelia", "ivern", "janna",
    "jarvan iv", "jax", "jayce", "jhin", "jinx", "k'sante", "kai'sa", "kalista", "karma", "karthus",
    "kassadin", "katarina", "kayle", "kayn", "kennen", "kha'zix", "kindred", "kled", "kog'maw", "leblanc",
    "lee sin", "leona", "lillia", "lissandra", "lucian", "lulu", "lux", "malphite", "malzahar", "maokai",
    "master yi", "milio", "miss fortune", "mordekaiser", "morgana", "naafiri", "nami", "nasus", "nautilus",
    "neeko", "nidalee", "nilah", "nocturne", "nunu e willump", "olaf", "orianna", "ornn", "pantheon", "poppy",
    "pyke", "qiyana", "quinn", "rakan", "rammus", "rek'sai", "rell", "renata glasc", "renekton", "rengar",
    "riven", "rumble", "ryze", "samira", "sejuani", "senna", "seraphine", "sett", "shaco", "shen", "shyvana",
    "singed", "sion", "sivir", "sivir", "skarner", "sona", "soraka", "swain", "sylas", "syndra", "tahm kench",
    "taliyah", "talon", "taric", "teemo", "thresh", "tristana", "trundle", "tryndamere", "twisted fate",
    "twitch", "udyr", "urgot", "varus", "vayne", "veigar", "vel'koz", "vex", "vi", "viego", "viktor",
    "vladimir", "volibear", "warwick", "wukong", "xayah", "xerath", "xin zhao", "yasuo", "yone", "yorick", "yuumi",
    "zac", "zed", "zeri", "ziggs", "zilean", "zoe", "zyra"
]

def start_game():
    input_window = tk.Toplevel(root)
    input_window.title("Input Window")

    champ_label = tk.Label(input_window, text="Champion to play:")
    champ_combobox = ttka.AutocompleteCombobox(input_window, completevalues=campeoes_lol)  
    ban_label = tk.Label(input_window, text="Champion to ban:")
    ban_combobox = ttka.AutocompleteCombobox(input_window, completevalues=campeoes_lol)  
    start_button = tk.Button(input_window, text="Start Game", command=lambda: start_game_with_champs(champ_combobox.get(), ban_combobox.get()))

    champ_label.pack()
    champ_combobox.pack()
    ban_label.pack()
    ban_combobox.pack()
    start_button.pack()


def start_game_with_champs(champ_to_play, champ_to_ban):
    print(champ_to_play,champ_to_ban)
    match = AcceptMatch.AcceptMatch(champ_to_play, champ_to_ban)
    subprocess.call([match.AutoAccept_Match()])
    
def search_runes():
    input_window = tk.Toplevel(root)
    input_window.title("Search Runes")

    champ_label = tk.Label(input_window, text="Champion to search:")
    champ_combobox = ttka.AutocompleteCombobox(input_window, completevalues=campeoes_lol) 
    champ_combobox.set("")
    lane_label = tk.Label(input_window, text="Lane")
    lane_combobox = ttka.AutocompleteCombobox(input_window, completevalues=['top', 'jungle', 'middle', 'bottom', 'support'])
    lane_combobox.set("top")
    runes = Runes.Runes(champ_combobox.get(), lane_combobox.get())
    search_button = tk.Button(input_window, text="Search", command=lambda: set_runes_params(champ_combobox.get(), lane_combobox.get(), runes))

    champ_label.pack()
    champ_combobox.pack()
    lane_label.pack()
    lane_combobox.pack()
    search_button.pack()

def set_runes_params(champion, lane, runes : Runes.Runes):
    runes.setChampion(champion)
    runes.setLane(lane)
    runes.open_runeSite()

def startGui():
    root.geometry("300x200")
    root.mainloop()
    
def teamFightTatics():
    champions,y = ga.algorithm("src/tft/champions.txt", 100, 8, 20, 3)
    window = tk.Tk()
    window.title("Champion-List")

    champion_frame = tk.Frame(window)
    champion_frame.pack(padx=20, pady=20)

    # Create a label for the champion list
    champion_label = tk.Label(champion_frame, text="List of Champions", font=("Arial", 20))
    champion_label.pack(pady=(5, 10))

    # Create a listbox widget to display the champions
    champion_listbox = tk.Listbox(champion_frame, selectmode=tk.SINGLE)
    champion_listbox.pack(fill=tk.BOTH, expand=True)

    # Populate the listbox with champions from the 'champions' vector
    for champion in champions:
        champion_listbox.insert(tk.END, champion)

    # Create a scrollbar for the listbox
    scrollbar = tk.Scrollbar(champion_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    champion_listbox.config(yscrollcommand=scrollbar.set, justify="center")
    scrollbar.config(command=champion_listbox.yview)

    # Create a label for the 'y' value
    y_label = tk.Label(window, text=f"Fitness: {y}", font=("Arial", 8))
    y_label.pack(padx=20, pady=(10, 20))

    # Run the tkinter main loop
    window.mainloop()

    # Run the tkinter main loop
    window.mainloop()


root = tk.Tk()
root.title("AutoClicker")
buttonAAM = tk.Button(root, text="Auto-Accept Match", command=start_game,  width=50, height=2)
buttonTFT = tk.Button(root, text="Teamfight Tactics", command=teamFightTatics,  width=40, height=2)
buttonSR = tk.Button(root, text="Search Runes", command=search_runes,  width=30, height=2)

buttonAAM.pack()
buttonTFT.pack()
buttonSR.pack()

startGui()
