from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
def mailer(person,reciever_mail):
    msg = MIMEMultipart()
    message = "Thank you for registering {} into our website".format(person)
    msg['From'] = "ngoreach315@gmail.com"
    password='abbakaharmonium'
    msg['To'] = reciever_mail
    msg['Subject'] = "Thank you mail"
    msg.attach(MIMEText(message, 'plain'))
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(msg['From'],password)

    s.sendmail(msg['From'],msg['To'],msg.as_string())
    s.quit()
