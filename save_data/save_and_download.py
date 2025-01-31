import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from logger.log_csv import log_event
from vision_ocr.detect_export_save import find_export_save_button_ocr  # 📌 Importação da visão computacional

SAVE_FILE_PATH = "savefile.txt"

def save_and_download(driver):
    """Exporta o salvamento do Cookie Clicker e salva no arquivo savefile.txt."""
    try:
        log_event("UPLOAD", "Exportando salvamento do Cookie Clicker...")
        time.sleep(2)

        # 📌 Clica no botão de configurações
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="prefsButton"]/div'))).click()
        time.sleep(2)

        # 📌 Tenta clicar no botão "Export Save" via Selenium
        try:
            export_save_btn = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Export save')]"))
            )
            export_save_btn.click()
        except TimeoutException:
            log_event("WARNING", "Botão 'Export Save' sumiu rápido. Tentando via OCR...")
            if not find_export_save_button_ocr(driver):
                log_event("ERRO", "Botão 'Export Save' não encontrado por nenhum método. Não foi possível exportar o salvamento.")
                return

        time.sleep(2)

        # 📌 Aguarda o campo de exportação do salvamento (id="textareaPrompt")
        try:
            save_output = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "textareaPrompt"))  # Campo de exportação
            )
            save_data = save_output.get_attribute("value")  # Captura o texto do salvamento
            log_event("INFO", "Código de salvamento copiado com sucesso.")
        except TimeoutException:
            log_event("ERRO", "Campo de exportação do salvamento não encontrado.")
            return

        # 📌 Salva o progresso no arquivo savefile.txt
        try:
            with open(SAVE_FILE_PATH, "w", encoding="utf-8") as file:
                file.write(save_data)
            log_event("UPLOAD", "Salvamento atualizado no arquivo savefile.txt!")
        except Exception as e:
            log_event("ERRO", f"Erro ao escrever no arquivo savefile.txt: {e}")
            return

        time.sleep(1)

        # 📌 Clica no botão de fechar (id="promptOption0") para sair da caixa de exportação
        try:
            close_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "promptOption0"))
            )
            close_btn.click()
            log_event("INFO", "Janela de exportação fechada com sucesso.")
        except TimeoutException:
            log_event("WARNING", "Não foi possível fechar a janela de exportação.")

    except Exception as e:
        log_event("ERRO", f"Erro ao exportar o salvamento: {e}")
