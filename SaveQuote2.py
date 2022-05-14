#Segunda Versão, finalizada

import pyautogui
import time
import datetime
import pyperclip

current_time = datetime.datetime.now() 
year = current_time.strftime("%Y, ")
month = current_time.strftime("%B ")
day = current_time.strftime("%d at ")
hour = current_time.strftime("%H-")
minute = current_time.strftime("%M")

printime = year + month + day + hour + minute

pyautogui.alert("Select the text in 5 seconds after closing this window.")
time.sleep(5)
pyautogui.hotkey("ctrl","c")

copy = pyperclip.paste()

with open("{}.txt".format(printime), "w", encoding="utf-8") as ArqEdit:
    ArqEdit.write(copy)

pyautogui.alert("Done, look if everything went allright in the file.")