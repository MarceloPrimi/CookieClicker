Cookie Clicker Bot
Este projeto é uma automação desenvolvida em Python para o jogo Cookie Clicker. O bot realiza cliques automáticos no cookie principal, compra upgrades e itens da loja, salva e carrega progresso, além de registrar logs de execução. Ele utiliza Selenium para interagir com o navegador e funcionalidades de OCR para elementos dinâmicos.

Funcionalidades
Clique automático no cookie principal com alta velocidade.
Compra de itens da loja (priorizando itens mais baratos ou caros, conforme a regra definida).
Compra de upgrades disponíveis.
Carregamento e exportação automática do progresso do jogo.
Registro de logs detalhados em um arquivo CSV.
Limpeza dos logs com um script independente.
Estrutura modular e fácil manutenção.
Estrutura do Projeto
plaintext
Copiar
Editar
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
Configuração do Ambiente
1. Instalar dependências
Certifique-se de ter Python 3.9+ instalado e execute o seguinte comando:

bash
Copiar
Editar
pip install -r requirements.txt
2. Configurar o arquivo .env
Crie um arquivo .env na raiz do projeto com o seguinte conteúdo:

env
Copiar
Editar
COOKIECLICKER_URL=https://orteil.dashnet.org/cookieclicker/
3. Instalar o Tesseract OCR
Este projeto utiliza OCR para interagir com elementos dinâmicos. Instale o Tesseract:

Windows: Download do instalador
Linux:
bash
Copiar
Editar
sudo apt install tesseract-ocr
Mac:
bash
Copiar
Editar
brew install tesseract
Como Executar o Bot
Inicie o bot:
bash
Copiar
Editar
python main.py
O bot irá:
Carregar o progresso do jogo.
Realizar cliques automáticos.
Comprar upgrades e itens.
Exportar o progresso após o tempo definido (padrão: 30 segundos).
Scripts Independentes
1. Limpar logs
Para apagar o conteúdo de bot_logs.csv sem interferir no bot:

bash
Copiar
Editar
python logs/limpar_logs.py
Logs
Os logs são armazenados no arquivo logs/bot_logs.csv e incluem:

INFO: Informações gerais, como cliques, compras e progresso salvo.
ERRO: Erros encontrados durante a execução.
UPLOAD: Eventos relacionados ao carregamento e salvamento do progresso.
Regras de Compra
1. Itens da Loja
Compra o item de menor valor 3 vezes.
Compra o item de maior valor 1 vez.
Essa sequência ocorre a cada 5 segundos.
2. Upgrades
Upgrades disponíveis são comprados automaticamente a cada 5 segundos.
Dependências
Python 3.9+
Selenium
OpenCV
Pytesseract
dotenv
Possíveis Melhorias Futuras
Implementar detecção de eventos especiais no jogo.
Adicionar interface gráfica para monitorar e controlar o bot.
Tornar o bot configurável diretamente pelo arquivo .env.
