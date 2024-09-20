import pywhatkit as kit
import time

# Função para ler o arquivo
def ler_arquivo(caminho_arquivo):
    with open(caminho_arquivo, 'r') as file:
        linhas = file.readlines()
    return [linha.strip() for linha in linhas]

# Função para enviar mensagem via WhatsApp
def enviar_mensagem(contato, mensagem):
    # Envia a mensagem (agendada para 20 segundos após a execução)
    kit.sendwhatmsg_instantly(f"+{contato}", mensagem)
    time.sleep(20)  # Aguarda para evitar o bloqueio por múltiplas mensagens

# Caminho para o arquivo de texto
caminho_arquivo = ".\\teste.txt"
# Número do contato em formato internacional (Ex: +5511999999999 para Brasil)
contato_whatsapp = "5548920005078"

# Lê o arquivo e envia cada linha como uma mensagem
linhas = ler_arquivo(caminho_arquivo)

for linha in linhas:
    if linha:  # Verifica se a linha não está vazia
        enviar_mensagem(contato_whatsapp, linha)
        print(f"Mensagem enviada: {linha}")
