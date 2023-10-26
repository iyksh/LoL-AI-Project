import os
import subprocess

if os.name == "nt":  # Windows OS
    requirements_file = "src/configs/requirements.txt"
    main_script = "src\\main.py"
    python_executable = "python3"

    try:
        subprocess.run(["pip", "install", "-r", requirements_file], check=True)
        subprocess.run([python_executable, main_script], check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        os.system("cls")
        print(f"{python_executable} maybe not installed, trying with python")
        os.system("python " + main_script)

elif os.name == "posix":  # Linux
    requirements_file = "src/configs/requirementsLinux.txt"
    main_script = "src/main.py"
    python_executable = "python3"

    try:
        subprocess.run(["pip", "install", "-r", requirements_file], check=True)
        subprocess.run([python_executable, main_script], check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        os.system("clear")
        print(f"{python_executable} maybe not installed, trying with python")
        os.system("python " + main_script)

else:
    print("OS not supported")
