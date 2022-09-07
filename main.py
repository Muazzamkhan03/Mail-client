import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import private

if __name__ == "__main__":
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

    server.ehlo()

    server.login(private.mail, private.password)

    msg = MIMEMultipart()
    msg['From'] = 'MailClient'
    msg['To'] = private.recipient
    msg['Subject'] = 'Test'

    with open('message.txt', 'r') as f:
        message = f.read()

    msg.attach(MIMEText(message, 'plain'))

    server.sendmail(private.mail, private.recipient, msg.as_string())
