
import smtplib

EMAIL_ADDRESS = 'rpacomsys2@outlook.co.th'
EMAIL_PASSWORD = 'comsys1234'

with smtplib.SMTP('smtp-mail.outlook.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    subject = 'Hello'
    body = 'this is for testing the smtp'

    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail(EMAIL_ADDRESS, 'mailbotcomsys@gmail.com', msg)
