import os
import platform
os.system('clear')
os.system("git pull")
b = platform.architecture()[0]
if b == '64bit':
    __import__("liz").Instagram()
    
elif b == '32bit':
    print(" TYPE pytho run.py to switch to 32bit")
