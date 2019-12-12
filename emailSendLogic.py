#acc: PasaHinnavaatlus@gmail.com
#password: projectpasa123
#appPassword: lzrrolwzktcylhbc


import smtplib
from email.message import EmailMessage

def emailSender(subject,body,addresstoWho):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = "PasaHinnavaatlus@gmail.com"
    msg["To"] = addresstoWho
    msg.set_content(body)
#Code below will send the email.
    with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
        smtp.login("PasaHinnavaatlus@gmail.com","lzrrolwzktcylhbc")
        smtp.send_message(msg)


