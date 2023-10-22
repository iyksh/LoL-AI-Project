import webbrowser


class Runes:
    def __init__(self, champion: str, lane: str):
        self.champion = champion
        self.lane = lane

    def setChampion(self, champion):
        self.champion = champion

    def setLane(self, lane):
        self.lane = lane
    
    def open_runeSite(self):
        url = "https://runes.lol/champion/"+self.champion+"/runes/?lane="+self.lane
        webbrowser.open(url)
    