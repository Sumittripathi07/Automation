import pyautogui
import time
pyautogui.hotkey('win','d')
pyautogui.hotkey('win')
pyautogui.write('Google Chrome')
pyautogui.press('enter')

time.sleep(1)

pyautogui.write('https://www.youtube.com/channel/UCGt6YxqAddqOfNOKyrYB9Ug')
pyautogui.press('enter')
