from PIL import ImageGrab
import pyautogui

green = (75, 219, 106)


def reaction_cheat():
    for i in range(0, 5):
        _react()
        pyautogui.click()


def _react():
    pixel = None
    while pixel != green:
        image = ImageGrab.grab(bbox=(300, 300, 301, 301))
        pixel = image.getpixel(xy=(0, 0))
    pyautogui.click()
