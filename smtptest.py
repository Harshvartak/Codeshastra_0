import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login('ngoreach315@gmail.com', 'abbakaharmonium')
message = "Ae bhosadike"
s.sendmail("ngoreach315@gmail.com", "khandorvatsal@gmail.com", message)
s.quit()
