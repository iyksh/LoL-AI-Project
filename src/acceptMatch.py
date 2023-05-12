from acceptAndPick import *

def aramAccept(): 
    numtry = 1
    findMatchButtom()
    os.system("clear")
    os.system("cls")
    for i in range(1000):
        time.sleep(6) 
        findAcceptLoc = pyautogui.locateOnScreen('images/aceitar.png',grayscale=True,confidence=0.5)
                
        if findAcceptLoc != None:
                    print("Aceppt buttom find")
                    findAcceptLoc = pyautogui.center(findAcceptLoc)
                    findAcceptLocX, findAcceptLocY = findAcceptLoc
                    pyautogui.click(findAcceptLocX,findAcceptLocY)
                    os.system("clear")
                    os.system("cls")
                    break
                    
                    
                    
                    
        else:
                    print(f"Accept buttom not found, num tries:{numtry}")
                    numtry +=1
                

