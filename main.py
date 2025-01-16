import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Acessando as variáveis de ambiente
smtp_server = os.getenv("SMTP_SERVER")
smtp_port = os.getenv("SMTP_PORT")
email_user = os.getenv("EMAIL_USER")
email_password = os.getenv("EMAIL_PASSWORD")

print(f"SMTP Server: {smtp_server}")
print(f"SMTP Port: {smtp_port}")