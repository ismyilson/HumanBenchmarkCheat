from PIL import ImageGrab
import pyautogui
import time

white = (250, 250, 250)


def sequence_cheat():
    time.sleep(0.4)
    sequence = list()
    wait_time = 0.6
    for i in range(0, 22):
        sequence = _get_sequence(sequence, wait_time)
        wait_time += 0.5
        time.sleep(0.75)


def _get_sequence(sequence, wait_time):
    time.sleep(wait_time)
    image = ImageGrab.grab(bbox=(750, 260, 1150, 660))
    x = (1150 - 750) / 3
    sub_x = x / 2
    y = (660 - 260) / 3
    sub_y = y / 2

    time.sleep(0.5)

    for i in range(1, 4):
        for j in range(1, 4):
            val_x = (x * i) - sub_x
            val_y = (y * j) - sub_y
            if image.getpixel((val_x, val_y)) >= white:
                sequence.append((750 + val_x, 260 + val_y))

    for item in sequence:
        pyautogui.moveTo(item)
        pyautogui.click()

    return sequence