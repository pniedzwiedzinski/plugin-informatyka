import smtplib
import ssl


def send_mail_tls(message, receiver, sender, password, server, port=587):
    with smtplib.SMTP(server, port) as server:
        server.ehlo()
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, receiver, message)


def send_mail_ssl(message, receiver, sender, password, server, port=465):
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(server, port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, message)
