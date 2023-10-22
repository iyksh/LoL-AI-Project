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


def autocomplete(event):
    search_text = event.widget.get().lower()

    if len(search_text) >= 2:
        matches = [champion for champion in campeoes_lol if search_text in champion.lower()]
        event.widget['values'] = matches
        event.widget.event_generate('<Down>')


def create_autocomplete_combobox(parent, label_text, default_value):
    label = tk.Label(parent, text=label_text)
    combobox = ttk.Combobox(parent)
    combobox['values'] = campeoes_lol
    combobox.set(default_value)
    combobox.bind('<KeyRelease>', autocomplete)

    label.pack()
    combobox.pack()

    return combobox


def start_game():
    input_window = tk.Toplevel(root)
    input_window.title("Input Window")

    champ_combobox = create_autocomplete_combobox(input_window, "Champion to play:", "")
    ban_combobox = create_autocomplete_combobox(input_window, "Champion to ban:", "")

    start_button = tk.Button(input_window, text="Start Game", command=lambda: start_game_with_champs(champ_combobox.get(), ban_combobox.get()))

    start_button.pack()


def start_game_with_champs(champ_to_play, champ_to_ban):
    print(champ_to_play, champ_to_ban)
    subprocess.call([h.AutoAccept_Match(champ_to_play, champ_to_ban)])


def search_runes():
    input_window = tk.Toplevel(root)
    input_window.title("Search Runes")

    champ_combobox = create_autocomplete_combobox(input_window, "Champion to search:", "")
    lane_label = tk.Label(input_window, text="Lane")
    lane_combobox = ttk.Combobox(input_window, values=["top", "jungle", "middle", "bottom", "support"])
    lane_combobox.set("")

    search_button = tk.Button(input_window, text="Search", command=lambda: h.open_runeSite(champ_combobox.get(), lane_combobox.get()))

    lane_label.pack()
    lane_combobox.pack()
    search_button.pack()

def startGui():
    root.geometry("300x300")
    root.mainloop()
    
def teamFightTatics():
    window = tk.Tk()
    window.title("Under Construction")
    label = tk.Label(window, text="In Construction", font=("Arial", 20))
    label.pack(padx=20, pady=20)

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
