import pyautogui
import time
import os


class AcceptMatch:
    def __init__(self, championName, bannedChampion):
        self.championName = championName
        self.bannedChampion = bannedChampion
        self.os = os.name
    
    def TryToBan(self):
        """Tries to ban a champion"""
        click_img('searchChampion.png', 0.4, self.os)
        time.sleep(5)
        pyautogui.write(self.bannedChampion)
        click_img('champion.png', 0.5, self.os)      
        time.sleep(1.5)
        click_img('banBottom.png', 0.6, self.os)


    def TryToPickChamp(self):
        """Tries to pick a champion"""

        time.sleep(5)
        click_img('searchChampion.png', 0.4, self.os)
        time.sleep(1)
        pyautogui.write(self.championName)
        click_img('champion.png', 0.3, self.os)
        time.sleep(2)
        click_img('confirm.png', 0.5, self.os)
                    
    def AutoAccept_Match(self):
        click_img('findMatch.png', 0.5, self.os)
        click_img('aceitar.png', 0.5, self.os)
        time.sleep(10) #wait to enter lobby

        print("+++ Waiting ban selection +++\n")
        time.sleep(20); 
        self.TryToBan()
        time.sleep(5) #wait after ban
            
        print("+++ Waiting your time to pick +++\n")
        self.TryToPickChamp(self.bannedChampion)


def click_img(imageName,confidenceNum, os):
        """search a image on screen, and click it"""

        if os == "nt":
            operatingSys = "Windows"
            imgX, imgY = Windows_locate_img(imageName, confidenceNum, operatingSys)
            pyautogui.click(imgX,imgY)
            
        else:
            operatingSystem = "Linux"
            imgX, imgY = Linux_locate_img(imageName, confidenceNum, operatingSys)
            pyautogui.click(imgX,imgY)
            

def Windows_locate_img(imageName, confidenceNum, operatingSys):
    """Get the central position of an image on windows OS, and return its coordinates"""

    numtry = 1
    while(True):
        findImgLoc = pyautogui.locateOnScreen(f'.\src\images\{imageName}',grayscale=True,confidence=confidenceNum)
        
        time.sleep(1.5)
        if findImgLoc != None:
            findImgLoc = pyautogui.center(findImgLoc)
            print(f"image: {imageName}, found. Num of tries: {numtry}, confidence: {confidenceNum}, Operating System: {operatingSys}")
            return findImgLoc
                
        else:
            print(f"image: {imageName}, not found. confidence: {confidenceNum}, num of tries:{numtry}, Operating System: {operatingSys}")
            numtry += 1
            continue

def Linux_locate_img(imageName, confidenceNum, operatingSys):
    """Get the central position of an image on a Linux OS, and return its coordinates"""

    numtry = 1
    while(True):
        time.sleep(1.5)
            
        findImgLoc = pyautogui.locateOnScreen(f'./src/images/{imageName}',grayscale=True,confidence=confidenceNum)
            
        if findImgLoc != None:
            
            findImgLoc = pyautogui.center(findImgLoc)
            print(f"image: {imageName}, found. Num of tries: {numtry}, confidence: {confidenceNum}, Operating System: {operatingSys}")
            return findImgLoc
                
        else:
            print(f"image: {imageName}, not found. confidence: {confidenceNum}, num of tries:{numtry}, Operating System: {operatingSys}")
            numtry += 1
            continue
