from PIL import ImageGrab, ImageOps
import pyautogui
import pytesseract
import re
import time


def number_memory_cheat():
    for i in range(0, 20):
        _remember_number(i)


def _remember_number(level):
    pos_x_start = 880 - (level * 24)
    pos_x_end = 1030 + (level * 23.25)
    timer = 1.5 + (level * 0.93)

    image = ImageGrab.grab(bbox=(pos_x_start, 365, pos_x_end, 482))
    image = image.point(lambda p: p > 250 and 255)
    image = ImageOps.invert(image)
    number = pytesseract.image_to_string(image, lang='eng', config='--psm 13 digits').strip()
    number = re.sub("[^0-9]", "", number)
    time.sleep(timer)
    pyautogui.moveTo(935, 425)
    pyautogui.click()
    pyautogui.write(number)
    pyautogui.press("enter")
    pyautogui.moveTo(930, 570)
    pyautogui.click()