import tkinter as tk
from tkinter import ttk
import subprocess
from Lol import header as h
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
    champ_combobox = ttk.Combobox(input_window, values=campeoes_lol)  
    champ_combobox.set("aatrox")  # Defina um valor padrão
    ban_label = tk.Label(input_window, text="Champion to ban:")
    ban_combobox = ttk.Combobox(input_window, values=campeoes_lol)  
    ban_combobox.set("aatrox")  # Defina um valor padrão
    start_button = tk.Button(input_window, text="Start Game", command=lambda: start_game_with_champs(champ_combobox.get(), ban_combobox.get()))

    champ_label.pack()
    champ_combobox.pack()
    ban_label.pack()
    ban_combobox.pack()
    start_button.pack()

def start_game_with_champs(champ_to_play, champ_to_ban):
    print(champ_to_play, champ_to_ban)
    subprocess.call([h.AutoAccept_Match(champ_to_play, champ_to_ban)])

def search_runes():
    input_window = tk.Toplevel(root)
    input_window.title("Search Runes")

    champ_label = tk.Label(input_window, text="Champion to search:")
    champ_combobox = ttk.Combobox(input_window, values=campeoes_lol) 
    champ_combobox.set("aatrox")  # Defina um valor padrão
    lane_label = tk.Label(input_window, text="Lane")
    lane_combobox = ttk.Combobox(input_window, values=["top", "jungle", "mid", "adc", "sup"])  
    lane_combobox.set("top")  # Defina um valor padrão
    search_button = tk.Button(input_window, text="Search", command=lambda: h.open_runeSite(champ_combobox.get(), lane_combobox.get()))

    champ_label.pack()
    champ_combobox.pack()
    lane_label.pack()
    lane_combobox.pack()
    search_button.pack()

root = tk.Tk()
root.title("AutoClicker")

button1 = tk.Button(root, text="Auto-Accept Match", command=start_game)
button5 = tk.Button(root, text="Search Runes", command=search_runes)

button1.pack()
button5.pack()

def startGui():
    root.geometry("300x200")
    root.mainloop()

startGui()
