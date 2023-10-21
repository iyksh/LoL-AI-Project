import pyautogui
import time
import os
import webbrowser

def click_img(imageName,confidenceNum):
    """Get a position of the center of an image, and click it"""
    numtry = 1
    while(True):
        time.sleep(1.5)
        if os.name == "nt":
            operatingSystem = "Windows"
            findImgLoc = pyautogui.locateOnScreen(f'.\src\images\{imageName}',grayscale=True,confidence=confidenceNum)
        
        else:
            operatingSystem = "Linux"
            findImgLoc = pyautogui.locateOnScreen(f'./src/images/{imageName}',grayscale=True,confidence=confidenceNum)
        
        if findImgLoc != None:
        
            findImgLoc = pyautogui.center(findImgLoc)
            imgX, imgY = findImgLoc
            pyautogui.click(imgX,imgY)
            print(f"image: {imageName}, found. Num of tries: {numtry}, confidence: {confidenceNum}, Operating System: {operatingSystem}")
            break
            
        else:
            print(f"image: {imageName}, not found. confidence: {confidenceNum}, num of tries:{numtry}, Operating System: {operatingSystem}")
            numtry += 1
            continue
            
def TryToBan(nameOfBanChamp):
    """Get a position of the center of an pre-defined images, and click in them to ban a champion"""
    click_img('searchChampion.png', 0.4)
    time.sleep(5)
    pyautogui.write(nameOfBanChamp)
    click_img('champion.png', 0.3)      
    time.sleep(1.5)
    click_img('banBottom.png', 0.6)


def TryToPickChamp(nameOfTheChampion):
        """Get a position of the center of an pre-defined images, and click in them to pick a champion"""

        time.sleep(5)
        click_img('searchChampion.png', 0.4)
        time.sleep(1)
        pyautogui.write(nameOfTheChampion)
        click_img('champion.png', 0.3)
        time.sleep(2)
        click_img('confirm.png', 0.5)
                
def AutoAccept_Match(nameOfTheChampion,nameOfBanChamp):
    
        click_img('findMatch.png', 0.7)
        click_img('aceitar.png', 0.5)
        time.sleep(10) #wait to enter lobby

        print("+++ Waiting ban selection +++\n")
        time.sleep(20); 
        TryToBan(nameOfBanChamp)
        time.sleep(5) #wait after ban
            
        print("+++ Waiting your time to pick +++\n")
        TryToPickChamp(nameOfTheChampion)


def open_runeSite(string):
    temporaryStr = list(string.split(" "))
    final_Str = "-".join(temporaryStr)
    
    url = "https://www.runas.lol/"+final_Str
    webbrowser.open(url)