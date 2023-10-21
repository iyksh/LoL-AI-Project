import webbrowser


class Runes:
    def __init__(self, champion, lane):
        self.champion = champion
        self.lane = lane

    def open_runeSite(self):
        print(self.champion, self.lane)

        url = "https://runes.lol/champion/"+self.champion+"/runes/?lane="+self.lane
        webbrowser.open(url)

    