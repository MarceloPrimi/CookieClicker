import os
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from driver.init_webdriver import init_webdriver
from logger.log_csv import log_event

# Carrega variáveis do .env
load_dotenv()
COOKIECLICKER_URL = os.getenv("COOKIECLICKER_URL", "https://orteil.dashnet.org/cookieclicker/")

def web_cookie_open():
    """Abre o site do Cookie Clicker, maximiza a tela e escolhe o idioma."""
    driver = init_webdriver()  # Inicializa o WebDriver

    try:
        driver.get(COOKIECLICKER_URL)
        driver.maximize_window()

        try:
            linguage_portugues = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="langSelect-EN"]'))
            )
            linguage_portugues.click()  # Agora realmente muda o idioma
            log_event("INFO", "Idioma alterado para Português.")

        except Exception:
            log_event("WARNING", "Botão de idioma não encontrado. Continuando no idioma padrão.")

        return driver  # Retorna o WebDriver ativo (Agora está no local correto)

    except Exception as e:
        log_event("ERRO", f"Erro ao inicializar o site: {e}")
        return None  # Retorna `None` se houver falha
