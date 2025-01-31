import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from logger.log_csv import log_event
from vision_ocr.detect_import_save import find_import_save_button_ocr

SAVE_FILE_PATH = "savefile.txt"

def load_save_file(driver):
    """Carrega um arquivo de salvamento ao iniciar a automação."""
    try:
        log_event("UPLOAD", "Carregando salvamento do Cookie Clicker...")
        time.sleep(10)  # ✅ Mantido para garantir carregamento completo da página

        # Clica no botão de configurações
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="prefsButton"]/div'))).click()
        time.sleep(5)

        #  Tenta clicar no botão "Import Save" via Selenium
        try:
            import_save_btn = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Import save')]"))
            )
            import_save_btn.click()
        except TimeoutException:
            log_event("WARNING", "Botão 'Import Save' sumiu rápido. Tentando via OCR...")
            if not find_import_save_button_ocr(driver):
                log_event("ERRO", "Botão 'Import Save' não encontrado por nenhum método. Pulando carregamento do salvamento.")
                return

        time.sleep(2)

        # Aguarda e insere o código de salvamento no campo id="textareaPrompt"
        try:
            save_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "textareaPrompt"))  # Alterado para ID correto
            )
            with open(SAVE_FILE_PATH, "r", encoding="utf-8") as file:
                save_data = file.read()
            save_input.send_keys(save_data)
            log_event("INFO", "Código de salvamento inserido com sucesso.")
        except TimeoutException:
            log_event("ERRO", "Campo de entrada do salvamento não encontrado.")
            return

        time.sleep(1)

        # Aguarda e clica no botão de confirmação id="promptOption0"
        try:
            load_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "promptOption0"))  # Alterado para ID correto
            )
            load_btn.click()
            log_event("UPLOAD", "Salvamento carregado com sucesso!")
        except TimeoutException:
            log_event("ERRO", "Botão 'Load' não encontrado. O salvamento pode não ter sido carregado corretamente.")
            return

        time.sleep(1)

        try:
            WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="prefsButton"]/div'))).click()
            log_event("UPLOAD", "Fechando as options")
            return             time.sleep(5)
        except TimeoutException:
            log_event("ERRO", "Botão 'Options' não encontrado.")

    except Exception as e:
        log_event("ERRO", f"Erro ao carregar salvamento: {e}")
