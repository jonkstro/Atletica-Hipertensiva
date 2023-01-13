from django.contrib import messages
from django.contrib.messages import constants
import re
# bibliotecas para email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from django.conf import settings

# REALIZAR FUNÇÕES DE AUXILIO AS VIEWS DO APP AUTENTICACAO

def password_is_valid(request, password, confirm_password):
    if len(password) < 6:
        messages.add_message(request, constants.ERROR, 'Sua senha deve conter 6 ou mais caractertes')
        # print(password, confirm_password)
        return False
    if not password == confirm_password:
        messages.add_message(request, constants.ERROR, 'As senhas não coincidem!')
        return False
    if not re.search('[A-Z]', password):
        messages.add_message(request, constants.ERROR, 'Sua senha não contem letras maiúsculas')
        return False
    if not re.search('[a-z]', password):
        messages.add_message(request, constants.ERROR, 'Sua senha não contem letras minúsculas')
        return False
    if not re.search('[1-9]', password):
        messages.add_message(request, constants.ERROR, 'Sua senha não contém números')
        return False
    return True


def enviar_email(para, mensagem):
    msg = MIMEMultipart()
    # setup the parameters of the message
    password = settings.EMAIL_HOST_PASSWORD
    msg['From'] = settings.EMAIL_HOST_USER
    msg['To'] = str(para)
    msg['Subject'] = "Não responda este e-mail | Atlética Hipertensiva"

    # add in the message body
    msg.attach(MIMEText(mensagem, 'plain'))

    #create server
    server = smtplib.SMTP('smtp.gmail.com: 587')
    
    server.starttls()
    
    # Login Credentials for sending the mail
    server.login(msg['From'], password)
    
    
    # send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    
    server.quit()
    
    print ("successfully sent email to %s:" % (msg['To']))


