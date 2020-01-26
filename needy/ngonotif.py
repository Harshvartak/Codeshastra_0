from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
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
