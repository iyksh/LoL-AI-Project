import os

os.system("pip install -r src/configs/requirements.txt")

if os.name == "nt": #nt: windows os
        os.system("python3 src\main.py")
else:
    os.system("python3 src/main.py")


