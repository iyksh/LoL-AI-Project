import os

if os.name == "nt": #nt: windows os
        os.system("pip install -r src/configs/requirements.txt")
        try:
                os.system("python3 src\main.py")        
        finally:
                os.system("cls")
                print("python3 maybe not installed, trying with python")
                os.system("python src\main.py")
        
        


elif os.name == "Linux":
        os.system("pip install -r src/configs/requirementsLinux.txt")
        try:
                os.system("python3 src/main.py")     
        finally:
                os.system("clear")
                print("python3 maybe not installed, trying with python")
                os.system("python src/main.py")

  
else:
        print("OS not supported")

