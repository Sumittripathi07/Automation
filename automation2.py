import pyautogui
import time

pyautogui.hotkey('win','d')
pyautogui.hotkey('win')
pyautogui.write('calculater')
time.sleep(1)
pyautogui.hotkey('win')
pyautogui.write('chrome')
pyautogui.hotkey('enter')

