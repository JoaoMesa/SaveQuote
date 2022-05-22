import pyautogui
import time
import datetime 

current_time = datetime.datetime.now() 
year = current_time.strftime("%Y ")
month = current_time.strftime("%B ")
hour = current_time.strftime("%H-")
minute = current_time.strftime("%M ")

printime = year + month + hour + minute

pyautogui.alert("Começando, selecione o texto")
time.sleep(8)

pyautogui.hotkey("ctrl","c")
pyautogui.press("win")
time.sleep(2)
pyautogui.write("Bloco")
time.sleep(2)
pyautogui.press("enter")
time.sleep(3)
pyautogui.hotkey("ctrl","v")
pyautogui.hotkey("ctrl","s")
pyautogui.write("Anotacao de {}.txt".format(printime))
time.sleep(1)
pyautogui.press("enter")
pyautogui.hotkey("alt","f4")