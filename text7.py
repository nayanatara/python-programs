#!/usr/bin/python3
import smtplib
s=smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login("nayanaputtadev@gmail.com","9945311055")
message="hello"
s.sendmail("nayanaputtadev@gmail.com","nayanaputtadev@gmail.com",message)
print("sucess")
s.quit()
