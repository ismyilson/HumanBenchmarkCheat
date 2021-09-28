from PIL import ImageGrab
import pytesseract
import pyautogui


def typing_cheat():
    image = ImageGrab.grab(bbox=(470, 400, 1430, 575))
    text = pytesseract.image_to_string(image, lang='eng')
    text = text.replace('\n', ' ')
    pyautogui.moveTo(550, 430)
    pyautogui.click()
    pyautogui.write(text)
