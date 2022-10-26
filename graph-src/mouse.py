import pyautogui
import time
import os
import subprocess

# command1 = subprocess.Popen(['C:/Windows/notepad.exe'])
# # os.spawnl(os.P_NOWAIT, "C:/Windows/notepad.exe", [""])
# time.sleep(1)

# pyautogui.click(100, 100)
# pyautogui.moveTo(100, 150)
# pyautogui.moveRel(0, 10)  # move mouse 10 pixels down
# pyautogui.dragTo(100, 150)
# pyautogui.dragRel(0, 10)  # drag mouse 10 pixels down

# pyautogui.moveTo(100, 100)
# time.sleep(1)

# pyautogui.click(100, 100)
# time.sleep(1)

# pyautogui.moveTo(200, 200)
# time.sleep(1)

# pyautogui.click(200, 200)
# time.sleep(1)


x, y = pyautogui.locateCenterOnScreen("5.png")
print(x, y)
pyautogui.moveTo(x, y)
