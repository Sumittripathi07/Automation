import pyautogui
import time

pyautogui.hotkey('win','d')
pyautogui.hotkey('win')
pyautogui.write('calculater')
time.sleep(1)
pyautogui.hotkey('win', 'd')
pyautogui.sleep(1)

pyautogui.hotkey('win')

pyautogui.hotkey('alt', 'tab')
pyautogui.sleep(1)
pyautogui.hotkey('alt', 'tab')
pyautogui.hotkey('alt', 'tab')
# pyautogui.press('enter')