import time 
import pyautogui as auto 


time.sleep(5)
with open('theText.txt' , 'r') as theFile:
    for line in theFile:
        auto.typewrite(line)
        auto.press('enter')

    