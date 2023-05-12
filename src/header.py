import pyautogui
import time
def startFlex():
        pyautogui.click(121,77)
        time.sleep(2)
        pyautogui.click(251,282)
        pyautogui.click(232,639)
        time.sleep(0.1)
        pyautogui.click(552,732)
        time.sleep(3)
        pyautogui.click(552,732)
        print("clicked")

def startAram():
        pyautogui.click(121,77)
        time.sleep(2)
        
        pyautogui.click(502,263)
        time.sleep(0.1)
        pyautogui.click(552,732)
        time.sleep(3)
        pyautogui.click(552,732)
        print("clicked")

def getMousePos():
        time.sleep(2)
        currentMouseX, currentMouseY = pyautogui.position()
        print(currentMouseX,currentMouseY)
        

               
                
