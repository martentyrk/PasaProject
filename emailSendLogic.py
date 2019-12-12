#acc: PasaHinnavaatlus@gmail.com
#password: projectpasa123
#appPassword: lzrrolwzktcylhbc

#peaks võibolla ehitama üles nii et saadame meili
#HTMLi look'iga. Näeb parem välja ja rohkem customizable
#https://www.youtube.com/watch?v=JRCJ6RtE3xU selle abil tegin, HTML osa on 29:55

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


l = [3, 4, 5]

l.append(100)

print(l)


