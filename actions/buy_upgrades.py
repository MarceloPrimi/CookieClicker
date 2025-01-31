import time
from selenium.webdriver.common.by import By
from logger.log_csv import log_event

last_upgrade_time = 0  # Variável global para rastrear o tempo da última compra de upgrade

def buy_upgrades(driver):
    """Compra automaticamente os upgrades disponíveis na loja a cada 5 segundos."""
    global last_upgrade_time  # Permite modificar a variável global

    if time.time() - last_upgrade_time < 25:  # Aguarda 25 segundos entre as compras de upgrade
        return

    try:
        upgrades = driver.find_elements(By.CSS_SELECTOR, "#upgrades div.enabled")

        for upgrade in upgrades:
            try:
                upgrade.click()
            except:
                continue  # Ignora erros individuais

        log_event("INFO", "Upgrades comprados com sucesso.")
        last_upgrade_time = time.time()  # Atualiza o tempo da última compra de upgrade

    except Exception as e:
        log_event("ERRO", f"Erro ao acessar os upgrades: {e}")
