import time
import os
from dotenv import load_dotenv
from save_data.load_save_file import load_save_file
from save_data.save_and_download import save_and_download
from actions.click_cookie import click_cookie
from actions.buy_store_items import buy_store_items
from actions.buy_upgrades import buy_upgrades
from logger.log_csv import log_event
from web_cookie.web_cookie_open import web_cookie_open

# Carrega variáveis do .env
load_dotenv()
COOKIECLICKER_URL = os.getenv("COOKIECLICKER_URL", "https://orteil.dashnet.org/cookieclicker/")

def executar_por_tempo(driver, segundos):
    """Executa as ações do bot pelo tempo especificado em segundos."""
    log_event("INFO", f"Iniciando execução por {segundos} segundos...")

    start_time = time.time()

    while time.time() - start_time < segundos:
        click_cookie(driver)  # Agora o clique no cookie é chamado constantemente
        buy_store_items(driver)  # Compra itens disponíveis na loja
        buy_upgrades(driver)  # Compra upgrades disponíveis

    log_event("INFO", "Tempo de execução concluído.")

def main():
    """Executa o bot do Cookie Clicker e depois exporta o salvamento."""

    driver = web_cookie_open()  # Inicializa o WebDriver e abre o site

    if driver is None:  # Se houver erro ao abrir o site, encerra o programa
        log_event("ERRO", "Erro ao entrar no site.")
        return

    try:
        # Carrega o progresso salvo antes de iniciar as ações
        load_save_file(driver)
        time.sleep(5)

        # Executa as ações definidas por segundos
        executar_por_tempo(driver, 100)

        log_event("INFO", "Salvando progresso...")

        # Salva e baixa o progresso automaticamente
        save_and_download(driver)

    except Exception as e:
        log_event("ERRO", f"Erro fatal: {e}")

    finally:
        driver.quit()  # Fecha o navegador corretamente
        log_event("INFO", "Bot finalizado.")

if __name__ == "__main__":
    main()  # 🚀 Inicia o bot
