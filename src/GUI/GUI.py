import tkinter as tk
import ttkwidgets.autocomplete as ttka
from tkinter import ttk
import subprocess
from Lol import AcceptMatch, Runes

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
    subprocess.call([match.AutoAccept_Match(champ_to_play, champ_to_ban)])
    
def search_runes():
    input_window = tk.Toplevel(root)
    input_window.title("Search Runes")

    champ_label = tk.Label(input_window, text="Champion to search:")
    champ_combobox = ttka.AutocompleteCombobox(input_window, completevalues=campeoes_lol) 
    champ_combobox.set("aatrox")
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


root = tk.Tk()
root.title("AutoClicker")

button1 = tk.Button(root, text="Auto-Accept Match", command=start_game)
button5 = tk.Button(root, text="Search Runes", command=search_runes)

button1.pack()
button5.pack()

def startGui():
    root.geometry("720x720")
    root.mainloop()

startGui()
