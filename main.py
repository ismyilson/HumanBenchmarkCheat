import pyautogui
import pytesseract
import sequence_cheat

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def _press_start_button():
    pyautogui.moveTo(930, 585)
    pyautogui.click()


if __name__ == '__main__':
    _press_start_button()
    sequence_cheat.sequence_cheat()
