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


def mailer1(email,reciever_mail,amount):
    msg = MIMEMultipart()
    message = "Your work has been acknowledged by people! Someone has donated an amount of {} towards your trust!. Though we have already, you may send a mail to {} to thank them personally. Cheers! Keep up the good work!!".format(amount, email)
    msg['From'] = "ngoreach315@gmail.com"
    password='abbakaharmonium'
    msg['To'] = reciever_mail
    msg['Subject'] = "Someone put in money for your cause!"
    msg.attach(MIMEText(message, 'plain'))
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(msg['From'],password)

    s.sendmail(msg['From'],msg['To'],msg.as_string())
    s.quit()

def mailer4(ngo,reciever_mail,amount):
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
