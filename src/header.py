import pyautogui
import time

def getPos_andClick(imageName,confidenceNum):
    numtry = 1
    while(True):
        time.sleep(1.5)
        findImgLoc = pyautogui.locateOnScreen(f'images/{imageName}',grayscale=True,confidence=confidenceNum)
        
        if findImgLoc != None:
        
            findImgLoc = pyautogui.center(findImgLoc)
            imgX, imgY = findImgLoc
            pyautogui.click(imgX,imgY)
            print(f"image: {imageName}, found. Num of tries: {numtry}, confidence: {confidenceNum}")
            break
            
        else:
            print(f"image: {imageName}, not found. confidence: {confidenceNum}, num of tries:{numtry}")
            numtry += 1
            continue
            
def TryToBan(nameOfBanChamp):
    getPos_andClick('searchChampion.png', 0.4)
    time.sleep(5)
    pyautogui.write(nameOfBanChamp)
    getPos_andClick('champion.png', 0.3)      
    time.sleep(1.5)
    getPos_andClick('banBottom.png', 0.6)


def TryToPickChamp(nameOfTheChampion):
        time.sleep(5)
        getPos_andClick('searchChampion.png', 0.4)
        time.sleep(1)
        pyautogui.write(nameOfTheChampion)
        getPos_andClick('champion.png', 0.3)
        time.sleep(2)
        getPos_andClick('confirm.png', 0.5)
                
def AutoAccept_Two(nameOfTheChampion,nameOfBanChamp):
    
        getPos_andClick('findMatch.png', 0.7)
        getPos_andClick('aceitar.png', 0.5)
        time.sleep(10) #wait to enter lobby

        print("+++ Waiting ban selection +++\n")
        time.sleep(20); 
        TryToBan(nameOfBanChamp)
        time.sleep(5) #wait after ban
            
        print("+++ Waiting your time to pick +++\n")
        TryToPickChamp(nameOfTheChampion)