from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
def mailer3(reciever_mail):
    msg = MIMEMultipart()
    message = "Someone has been reported in need of help in your area. Please check our website for the recent entries"
    msg['From'] = "ngoreach315@gmail.com"
    password='abbakaharmonium'
    msg['To'] = reciever_mail
    msg['Subject'] = "Someone is in need of help!"
    msg.attach(MIMEText(message, 'plain'))
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(msg['From'],password)

    s.sendmail(msg['From'],msg['To'],msg.as_string())
    s.quit()
