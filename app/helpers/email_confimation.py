import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


class EmailConfirmation():

    def send_email(self, email_inst):
        email_from = 'nextnelson1234@gmail.com'
        email_password = os.getenv('EMAIL_PASSWORD')
        email_smtp_server = 'smtp.gmail.com'

        destination = email_inst

        subject = 'Teste - Email Python'

        msg = MIMEMultipart()
        msg['From'] = email_from
        msg['Subject'] = subject

        text = "Enviando Email con python de forma automatica"
        msg_text = MIMEText(text, 'html')
        msg.attach(msg_text)

        try:
            smtp = smtplib.SMTP(email_smtp_server, 587)
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(email_from, email_password)
            smtp.sendmail(email_from, destination, msg.as_string())
            smtp.quit()
            print('Email enviado exitosamente')
        except Exception as err:
            print(f'Falla en envio de email: {err}')
