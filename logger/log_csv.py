import csv
import os
from datetime import datetime

LOG_FILE = "logs/bot_logs.csv"

# Criar o arquivo CSV se ele não existir
if not os.path.exists("logs"):
    os.makedirs("logs")

if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "Tipo", "Mensagem"])  # Cabeçalhos do CSV


def log_event(tipo, mensagem):
    """Registra um evento no arquivo CSV."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Print para depuração no console
    if tipo == "ERRO":
        print(f"❌ {mensagem}")
    elif tipo == "UPGRADE":
        print(f"🆙 {mensagem}")
    elif tipo == "SAVE":
        print(f"💾 {mensagem}")
    elif tipo == "DOWNLOAD":
        print(f"📥 {mensagem}")
    elif tipo == "UPLOAD":
        print(f"📤 {mensagem}")
    else:
        print(f"🔹 {mensagem}")

    # Escrever no CSV
    with open(LOG_FILE, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, tipo, mensagem])
