from PIL import ImageGrab, ImageOps
import pyautogui
import pytesseract
import time

chimp_continue_btn = (950, 550)
chimp_start_x = 605
chimp_start_y = 220
chimp_size_x = 65
chimp_size_y = 60
chimp_separator_x = chimp_size_x + 25
chimp_separator_y = chimp_size_y + 30


def chimp_cheat():
    for i in range(0, 30):
        _chimp_calc()


def _chimp_calc():
    numbers = list()
    chimp_current_x = chimp_start_x
    chimp_current_y = chimp_start_y
    for y in range(0, 5):
        for x in range(0, 8):
            image = ImageGrab.grab(
                bbox=(chimp_current_x, chimp_current_y, chimp_current_x + chimp_size_x, chimp_current_y + chimp_size_y))

            is_empty = image.getcolors(1)
            if is_empty:
                chimp_current_x += chimp_separator_x
                continue

            image = image.point(lambda p: p > 250 and 255)
            image = ImageOps.invert(image)
            number = pytesseract.image_to_string(image, lang='eng', config='--psm 13 digits').strip()

            if number.isnumeric():
                numbers.append((int(number), (chimp_current_x, chimp_current_y)))

            chimp_current_x += chimp_separator_x

        chimp_current_x = chimp_start_x
        chimp_current_y += chimp_separator_y

    numbers.sort()
    for data in numbers:
        pyautogui.moveTo(data[1])
        pyautogui.click()

    pyautogui.moveTo(chimp_continue_btn)
    pyautogui.click()
    time.sleep(0.1)
