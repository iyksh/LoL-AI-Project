import pyautogui
import time

from pynput.keyboard import Listener, Key
import logging



def cait():
    
    logging.basicConfig(filename="key_log.txt", level=logging.DEBUG, format='%(asctime)s: %(message)s')

    def on_press(key):
        if key == Key.space:
            
            findEnemy = pyautogui.locateOnScreen('images/enemyHealth.png',grayscale=False,confidence=0.3)
            
            while findEnemy != None:
                print("enemy found")
                
                currentMouseX, currentMouseY = pyautogui.position()
                findEnemy = pyautogui.center(findEnemy)
                enemyX, enemyY = findEnemy
                pyautogui.click(enemyX,enemyY,button="RIGHT")
                
                time.sleep(0.4)
                pyautogui.click(currentMouseX,currentMouseY,button="RIGHT")
                
                VerifyUnpressed = on_release(key)
                if VerifyUnpressed == 1:
                    print("ESPAÇO SOLTO")
                    break
                
            else:
                print("enemy Not found")
                

    def on_release(key):
        if key == Key.space:
            return 1
        


    
    with Listener(on_press=on_press,on_release=on_release) as listener:  # Create an instance of Listener
        listener.join()  # Join the listener thread to the main thread to keep waiting for keys
