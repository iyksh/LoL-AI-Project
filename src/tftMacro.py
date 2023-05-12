import time
import pyautogui

def getPos_andClick(imageName,confidenceNum,side):
    numtry = 1
    while(True):
        time.sleep(1.5)
        findImgLoc = pyautogui.locateOnScreen(f'tft/{imageName}',grayscale=True,confidence=confidenceNum)
        
        if findImgLoc != None:
        
            findImgLoc = pyautogui.center(findImgLoc)
            imgX, imgY = findImgLoc
            pyautogui.click(imgX,imgY,button=side)
            print(f"image: {imageName}, found. Num of tries: {numtry}, confidence: {confidenceNum}")
            return findImgLoc
            break
            
        else:
            print(f"image: {imageName}, not found. confidence: {confidenceNum}, num of tries:{numtry}")
            numtry += 1
            return 0
            continue

def getPos_andClick_Without_Return(imageName,confidenceNum):
    numtry = 1
    while(True):
        time.sleep(1.5)
        findImgLoc = pyautogui.locateOnScreen(f'tft/{imageName}',grayscale=True,confidence=confidenceNum)
        
        if findImgLoc != None:
        
            findImgLoc = pyautogui.center(findImgLoc)
            imgX, imgY = findImgLoc
            pyautogui.click(imgX,imgY)
            print(f"image: {imageName}, found. Num of tries: {numtry}, confidence: {confidenceNum}")
            return findImgLoc
            break
            
        else:
            print(f"image: {imageName}, not found. confidence: {confidenceNum}, num of tries:{numtry}")
            numtry += 1
            continue


def PlayAndAcceptMatch():
        getPos_andClick_Without_Return('findMatch.png', 0.7)
        getPos_andClick_Without_Return('aceitar.png', 0.5)
        
def buy_lvl_one_champ():
    getPos_andClick('lvl1.png', 0.6, 'LEFT')
    return 1
    
def buy_lvl_two_champ():
    getPos_andClick('lvl2.png', 0.6, 'LEFT')
    return 2
    
def buy_lvl_three_champ():
    getPos_andClick('lvl3.png', 0.6, 'LEFT')
    return 3
    
def buy_lvl_four_champ():
    getPos_andClick('lvl4.png', 0.6, 'LEFT')
    return 4

def buy_lvl_five_champ():
    getPos_andClick('lvl5.png', 0.6, 'LEFT')
    return 5
    


def buy_Interval():
    for rounds in range(3):
        
        for item in range(3):
            verifyItem = getPos_andClick('item.png', 0.5, 'RIGHT')
            time.sleep(4)
        
        #Buy champ
        
        
            verify = buy_lvl_two_champ()
            if verify == 0:
                verify_two = buy_lvl_three_champ()
                if verify_two == 0:
                    verify_Three = buy_lvl_three_champ()
                    if verify_Three == 0:
                        verify_four = buy_lvl_four_champ()
                        if verify_four == 0:
                            buy_lvl_five_champ()
            
        time.sleep(40)

def restart():
    time.sleep(10)
    getPos_andClick('exit.png', 0.7, 'LEFT')
    getPos_andClick_Without_Return('playAgain.png', 0.5)
    time.sleep(5)
    Game_Panel()


def Game_Panel():

    PlayAndAcceptMatch()
    for i in range(50):
        buy_Interval()
    
    
    restart()
   
Game_Panel()