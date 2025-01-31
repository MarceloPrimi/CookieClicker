from selenium.webdriver.common.by import By
from logger.log_csv import log_event

def click_cookie(driver):
    """Clica rapidamente no cookie principal uma única vez (sem bloquear o loop)."""
    try:
        cookie = driver.find_element(By.ID, "bigCookie")
        cookie.click()
    except Exception as e:
        log_event("ERRO", f"Erro ao clicar no cookie: {e}")
#teste