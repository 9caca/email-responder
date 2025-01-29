import imaplib
import email
from email.mime.text import MIMEText
import smtplib
import os
import logging
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Configuração básica do logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='email_auto_reply.log',
    filemode='a'
)

# Acessando as variáveis de ambiente
smtp_server = os.getenv("SMTP_SERVER")
smtp_port = os.getenv("SMTP_PORT")
email_user = os.getenv("EMAIL_USER")
email_password = os.getenv("EMAIL_PASSWORD")
imap_server = os.getenv ("IMAP_SERVER")
imap_port = os.getenv("IMAP_PORT")

# Lista de termos que indicam e-mails automáticos
AUTO_EMAIL_INDICATORS = ["no-reply", "noreply", "automatic", "do-not-reply", "no_reply"]

def is_auto_email(from_):
    #Verifica se o e-mail é automático com base no remetente.
    from_lower = from_.lower()
    return any(indicator in from_lower for indicator in AUTO_EMAIL_INDICATORS)

def check_and_reply_emails():
    try:
        # Conexão com o servidor IMAP
        mail = imaplib.IMAP4_SSL(imap_server, imap_port)
        mail.login(email_user, email_password)
        
        # Selecionar a caixa de entrada
        mail.select("inbox")
        
        # Pesquisar por e-mails não lidos
        status, messages = mail.search(None, 'UNSEEN')
        if status == "OK":
            for num in messages[0].split():
                # Buscar o e-mail pelo ID
                status, msg_data = mail.fetch(num, '(RFC822)')
                for response_part in msg_data:
                    if isinstance(response_part, tuple):
                        msg = email.message_from_bytes(response_part[1])
                        subject = msg['subject']
                        from_ = msg['from']
                        
                        # Log: E-mail recebido
                        logging.info(f"Novo e-mail recebido de: {from_} | Assunto: {subject}")

                        # Verificar se o e-mail é automático
                        if is_auto_email(from_):
                            logging.warning(f"Ignorando e-mail automático de: {from_} | Assunto: {subject}")
                        else:
                            # Enviar resposta automática
                            send_auto_reply(from_, subject)
                            logging.info(f"Resposta enviada para: {from_}")
                        
                        # Marcar o e-mail como lido (opcional)
                        mail.store(num, '+FLAGS', '\\Seen')
        
        # Fechar conexão
        mail.logout()
    except Exception as e:
        logging.error(f"Erro ao conectar ao servidor de e-mail: {str(e)}")

def send_auto_reply(to, subject):
    try:
        # Criar a mensagem de resposta
        reply_subject = f"Re: {subject}"
        reply_body = "Obrigado por entrar em contato. Esta é uma resposta automática."
        
        msg = MIMEText(reply_body)
        msg['Subject'] = reply_subject
        msg['From'] = email_user
        msg['To'] = to
        
        # Enviar o e-mail
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(email_user, email_password)
            server.sendmail(email_user, to, msg.as_string())
        
        print(f"Resposta enviada para: {to}")
    except Exception as e:
        print(f"Erro ao enviar resposta para {to}: {str(e)}")

if __name__ == "__main__":
    check_and_reply_emails()
