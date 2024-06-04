# Enviando E-mails SMTP com Python
import os

from pathlib import Path
from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import smtplib

from dotenv import load_dotenv  # type: ignore

load_dotenv()

# Caminho arquivo
CAMINHO_HTML = Path(__file__).parent / 'aula190.html'


# Dados do remetente e destinatario
remetente = os.getenv('FROM_EMAIL', '')
destinatario = remetente


# Configurações SMTP
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_user = os.getenv('FROM_EMAIL', '')
smtp_password = os.getenv('EMAIL_PASSWORD', '')


# Mensagem de Texto
with CAMINHO_HTML.open('r', encoding='utf8') as file:
    text = file.read()
    template = Template(text)
    text_email = template.substitute(name='Duardo')

# Trasnformar nossa mensagem em MIMEMultiPart
mime_multipart = MIMEMultipart()
mime_multipart['from'] = remetente
mime_multipart['to'] = destinatario
mime_multipart['subject'] = 'Este é o assunto do e-mail'

corpo_email = MIMEText(text_email, 'html', 'utf8')
mime_multipart.attach(corpo_email)

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo()
    server.starttls()
    server.login(smtp_user, smtp_password)
    server.send_message(mime_multipart)
    print('E-mail enviado com sucesso!!')
