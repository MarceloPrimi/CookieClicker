import os
import csv
from logger.log_csv import log_event

# 📌 Caminho absoluto para o arquivo dentro da pasta `logs`
BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # Caminho até a raiz do projeto
LOG_FILE = os.path.join(BASE_DIR, "logs", "bot_logs.csv")


def limpar_logs():
    """Apaga os registros do log, mantendo o cabeçalho."""
    if not os.path.exists(LOG_FILE):
        log_event("ERRO", f"O arquivo '{LOG_FILE}' não foi encontrado. Criando um novo...")

    try:
        # 🔹 Lê o cabeçalho do arquivo, se existir
        header = ["Timestamp", "Tipo", "Mensagem"]
        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                linhas = list(reader)
                if len(linhas) > 0:
                    header = linhas[0]  # Mantém o cabeçalho original

        # 🔹 Reescreve o arquivo apenas com o cabeçalho
        with open(LOG_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(header)  # Escreve o cabeçalho novamente

        log_event("INFO", "Todos os logs foram apagados com sucesso.")

    except Exception as e:
        log_event("ERRO", f"Erro ao limpar os logs: {e}")


if __name__ == "__main__":
    limpar_logs()  # 🚀 Executa o script quando chamado diretamente
