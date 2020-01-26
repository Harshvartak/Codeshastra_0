from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
def mailer(ngo,reciever_mail,amount):
    msg = MIMEMultipart()
    message = "Thank you for donating to the NGO! We're sure you have made a difference in someone's life today!!! Here's acknowledging the amount of Rs. {} you have sent!".format(amount)
    msg['From'] = "ngoreach315@gmail.com"
    password='abbakaharmonium'
    msg['To'] = reciever_mail
    msg['Subject'] = "Thank you for donating to {}".format(ngo)
    msg.attach(MIMEText(message, 'plain'))
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(msg['From'],password)

    s.sendmail(msg['From'],msg['To'],msg.as_string())
    s.quit()
