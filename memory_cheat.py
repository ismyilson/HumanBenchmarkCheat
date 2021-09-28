from PIL import ImageGrab
import time
import pyautogui

white = (250, 250, 250)


def memory_cheat():
    time.sleep(0.70)
    for i in range(0, 20):
        _do_memory_cheat()


def _do_memory_cheat():
    image = ImageGrab.grab(bbox=(750, 260, 1150, 660))
    time.sleep(1.5)
    squares = _get_squares()
    squares_to_click = list()
    x = (1150 - 750) / squares
    sub_x = x / 2
    y = (660 - 260) / squares
    sub_y = y / 2
    for i in range(1, squares + 1):
        for j in range(1, squares + 1):
            val_x = (x * i) - sub_x
            val_y = (y * j) - sub_y
            if image.getpixel((val_x, val_y)) >= white:
                pyautogui.moveTo((750 + val_x, 260 + val_y))
                pyautogui.click()

    time.sleep(1.5)


def _get_squares():
    image = ImageGrab.grab(bbox=(750, 260, 1150, 660))
    colors = image.getcolors()
    squares = 3
    while squares < 50:
        if [item for item in colors if item[0] == 8 * (squares ** 2)]:
            return squares
        else:
            squares += 1

    return 0
