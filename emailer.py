import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send(sender, recipient, password, subject, body):
    msg = MIMEMultipart()

    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient

    msg.attach(MIMEText(body, 'html'))

    print('Server init...')

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.set_debuglevel(0)
    server.ehlo()
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, recipient, msg.as_string())

    print('Email sent!')

    server.quit()
