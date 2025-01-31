# Cookie Clicker Bot

Este projeto é uma automação desenvolvida em Python para o jogo **Cookie Clicker**. O bot realiza cliques automáticos no cookie principal, compra upgrades e itens da loja, salva e carrega progresso, além de registrar logs de execução. Ele utiliza **Selenium** para interagir com o navegador e funcionalidades de OCR para elementos dinâmicos.

---

## Funcionalidades
- **Clique automático no cookie principal** com alta velocidade.
- **Compra de itens da loja** (priorizando itens mais baratos ou caros, conforme a regra definida).
- **Compra de upgrades disponíveis.**
- **Carregamento e exportação automática do progresso do jogo.**
- **Registro de logs** detalhados em um arquivo CSV.
- **Limpeza dos logs** com um script independente.
- **Estrutura modular** e fácil manutenção.

---

## Estrutura do Projeto

```plaintext
CookieClicker/
├── actions/
│   ├── buy_store_items.py        # Módulo para comprar itens da loja.
│   ├── buy_upgrades.py           # Módulo para comprar upgrades.
│   └── click_cookie.py           # Módulo para cliques automáticos no cookie.
├── driver/
│   ├── init_webdriver.py         # Inicializa o WebDriver para Selenium.
├── logger/
│   ├── log_csv.py                # Funções para registrar eventos em logs.
├── logs/
│   ├── bot_logs.csv              # Arquivo onde os logs são registrados.
│   ├── limpar_logs.py            # Script para limpar os logs.
├── save_data/
│   ├── load_save_file.py         # Carrega o progresso do jogo.
│   ├── save_and_download.py      # Exporta e salva o progresso do jogo.
├── vision_ocr/
│   ├── detect_import_save.py     # Detecta o botão "Import Save" usando OCR.
│   ├── detect_export_save.py     # Detecta o botão "Export Save" usando OCR.
├── web_cookie/
│   ├── web_cookie_open.py        # Abre o site e ajusta o idioma.
├── .env                          # Configurações de ambiente (URL do jogo, etc.).
├── main.py                       # Arquivo principal para executar o bot.
├── savefile.txt                  # Arquivo de salvamento do progresso do jogo.
