from PIL import ImageGrab, ImageChops
import pyautogui
import time

image_seen_btn = (890, 510)
image_new_btn = (975, 510)


def verbal_memory_cheat():
    images = list()
    for i in range(0, 170):
        image = ImageGrab.grab(bbox=(750, 375, 1150, 475))
        if _image_seen(image, images):
            pyautogui.moveTo(image_seen_btn)
            pyautogui.click()
        else:
            images.append(image)
            pyautogui.moveTo(image_new_btn)
            pyautogui.click()

        time.sleep(0.1)


def _image_seen(image, images):
    for saved_image in images:
        if not ImageChops.difference(image, saved_image).getbbox():
            return True

    return False
