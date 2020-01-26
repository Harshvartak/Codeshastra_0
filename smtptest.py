import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login('ngoreach315@gmail.com', 'abbakaharmonium')
message = "Test email"
s.sendmail("ngoreach315@gmail.com", "vartak.harsh@gmail.com", message)
s.quit()
