import time
from selenium.webdriver.common.by import By
from logger.log_csv import log_event

last_purchase_time = 0  # Variável global para rastrear o tempo da última compra


def buy_store_items(driver):
    """Compra automaticamente os itens da loja seguindo a regra de menor valor 3x e maior valor 1x a cada 5 segundos."""
    global last_purchase_time  # Permite modificar a variável global

    if time.time() - last_purchase_time < 30:  # Aguarda 5 segundos entre as compras
        return

    try:
        store_items = driver.find_elements(By.CSS_SELECTOR, "#store div.product.unlocked.enabled")
        store_items_sorted = sorted(store_items, key=lambda item: int(item.get_attribute("id").replace("product", "")))

        cheapest_item = store_items_sorted[0]  # Item mais barato
        most_expensive_item = store_items_sorted[-1]  # Item mais caro

        # Compra o item mais barato 3 vezes
        for _ in range(3):
            try:
                cheapest_item.click()
            except:
                continue

        log_event(f"Item", f"Item comprado "".")

        # Compra o item mais caro 1 vez
        try:
            most_expensive_item.click()
        except:
            pass

    except Exception as e:
        log_event("ERRO", f"Erro ao acessar a loja: {e}")
