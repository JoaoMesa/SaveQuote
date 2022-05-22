#Segunda Versão, 1º Update

import pyautogui
import time
import datetime
import pyperclip
from easygui import *

current_time = datetime.datetime.now() 
year = current_time.strftime("%Y, ")
month = current_time.strftime("%B ")
day = current_time.strftime("%d at ")
hour = current_time.strftime("%H-")
minute = current_time.strftime("%M")

printime = year + month + day + hour + minute

pyautogui.alert("Select the text in 5 seconds after closing this alert.")
time.sleep(5)
pyautogui.hotkey("ctrl","c")

copy = pyperclip.paste()

message = "Would you like to give the file a name?"

title = "SaveQuote"

output = ynbox(message, title)


if output:
    
    name = pyautogui.prompt("Type the file name here(Don't type .txt or another extension)")
    with open("{}.txt".format(name), "w", encoding="utf-8") as ArqEdit:
        ArqEdit.write(copy)
else:
    with open("{}.txt".format(printime), "w", encoding="utf-8") as ArqEdit:
        ArqEdit.write(copy)

pyautogui.alert("Done. See if there was any error in the file")