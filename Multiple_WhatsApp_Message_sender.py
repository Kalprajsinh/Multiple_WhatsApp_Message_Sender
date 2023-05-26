import pyautogui
import time 
import pywhatkit

pywhatkit.sendwhatmsg("+919876543210","1. this is Message",17,35)
for i in range(2,21):
    pyautogui.typewrite(str(i)+". this is Message")
    pyautogui.press("enter")