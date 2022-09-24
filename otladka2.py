'''
Этот проект на pyautogui должен запускать блокнот
Но почему-то код выдаёт ошибку
'''
import pyautogui
import time

press('win')
sleep(1)
write('notepad')
sleep(1)
press('enter')