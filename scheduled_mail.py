import datetime as dt
import time
import smtplib
import os

EMAIL_ADDRESS = os.environ.get("acc")
EMAIL_PASSWORD = os.environ.get("pass")

def send_email():
    email_user = EMAIL_ADDRESS
    server = smtplib.SMTP ('smtp.gmail.com', 465)
    server.starttls()
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    #EMAIL
    message = 'sending this from python!'
    server.sendmail(email_user, email_user, message)
    server.quit()

print('Mail about to send')
send_time = dt.datetime(2022,2,14,10,35,0) # set your sending time in UTC
time.sleep(send_time.timestamp() - time.time())
send_email()
print('email sent')