from PIL import ImageGrab
import pyautogui

blue = (43, 135, 209)


def aim_cheat():
    pyautogui.moveTo((951, 430))
    pyautogui.click()
    for i in range(0, 30):
        image = ImageGrab.grab(bbox=(470, 250, 1350, 640))
        pyautogui.moveTo(_find_target(image))
        pyautogui.click()


def _find_target(image):
    for x in range(0, 880, 70):
        for y in range(0, 390, 70):
            if image.getpixel(xy=(x, y)) != blue:
                return x + 485, y + 260
