import os

if os.name == "nt": #nt: windows os
        os.system("pip install -r src/configs/requirements.txt")
        os.system("python3 src\main.py")
else:
        os.system("pip install -r src/configs/requirements.txt")
        os.system("python3 src/main.py")     
  


