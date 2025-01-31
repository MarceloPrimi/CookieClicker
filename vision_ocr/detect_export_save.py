import cv2
import numpy as np
import pytesseract
from logger.log_csv import log_event

#️ Ajuste o caminho do Tesseract se necessário
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def find_export_save_button_ocr(driver):
    """
    Usa OCR para identificar o botão 'Export Save' na tela.

    Parâmetros:
        driver: WebDriver do Selenium

    Retorno:
        True -> Se o botão "Export Save" foi encontrado
        False -> Se não foi encontrado
    """
    log_event("INFO", "Tentando encontrar o botão 'Export Save' com OCR...")

    # Captura uma screenshot da página
    screenshot = driver.get_screenshot_as_png()
    image = cv2.imdecode(np.frombuffer(screenshot, np.uint8), cv2.IMREAD_COLOR)

    # Converte para cinza e melhora contraste para OCR
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    # Aplica OCR
    text = pytesseract.image_to_string(binary, lang="eng")

    # Procura pelo texto "Export Save"
    if "Export Save" in text:
        log_event("INFO", "Botão 'Export Save' identificado por OCR! Clique manual pode ser necessário.")
        return True  # OCR encontrou o botão
    else:
        log_event("ERRO", "Botão 'Export Save' não encontrado via OCR.")
        return False  # OCR não encontrou
