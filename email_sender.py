import smtplib
import smtplib
from email_credentials import *

def send_email(subject, body, from_email, password, to_email):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(from_email, password)
        message = f'Subject: {subject}\n\n{body}'
        server.sendmail(from_email, to_email, message)
        server.quit()
        print('Email sent successfully')
    except:
        print("Email couldn't be sent")
        pass


if __name__=='__main__':
    recipient = input("Please enter recepient's email: ")
    s = input('Please enter the subject of the email: ')
    b = input('Please enter the content of the email: ')
    send_email(s, b, myemail, mypassword, recipient)
