import imaplib
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Acessando as variáveis de ambiente
smtp_server = os.getenv("SMTP_SERVER")
smtp_port = os.getenv("SMTP_PORT")
email_user = os.getenv("EMAIL_USER")
email_password = os.getenv("EMAIL_PASSWORD")
imap_server = os.getenv ("IMAP_SERVER")
imap_port = os.getenv("IMAP_PORT")

def list_email_folders():
    try:
        # Conexão com o servidor IMAP
        mail = imaplib.IMAP4_SSL(imap_server, imap_port)
        mail.login(email_user, email_password)
        
        # Listar pastas disponíveis
        status, folders = mail.list()
        if status == "OK":
            print("Pastas disponíveis:")
            for folder in folders:
                print(folder.decode())
        else:
            print("Erro ao listar pastas:", status)
        
        # Fechar conexão
        mail.logout()
    except Exception as e:
        print("Erro ao conectar ao servidor de e-mail:", str(e))

if __name__ == "__main__":
    list_email_folders()