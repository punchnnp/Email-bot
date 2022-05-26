
import os
import pandas as pd
import smtplib
from PIL import Image, ImageDraw, ImageFont
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

df = pd.read_excel('mailbot.xlsx')

EMAIL_ADDRESS = 'rpacomsys@outlook.co.th'
EMAIL_PASSWORD = 'comsys1234'

with smtplib.SMTP('smtp-mail.outlook.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    for i in df.iterrows():
        name = i[1]["Name"]
        receiver_email = i[1]["email"]

        message = MIMEMultipart()
        message["From"] = EMAIL_ADDRESS
        message["To"] = receiver_email
        message["Subject"] = f'Congratulation {name}'
        # message["Bcc"] = receiver_email  # Recommended for mass emails
        body = "Congratulation of blahhhhh"
        # Add body to email
        message.attach(MIMEText(body, "plain"))

        print(f"Now editing certificate for {name}")
        text_y_position = 700
        img = Image.open('certificate.png')
        image_width = img.width
        image_height = img.height
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype('PinyonScript-Regular.ttf', 100)
        text_width, _ = draw.textsize(name, font=font)
        draw.text(((image_width - text_width) / 2, text_y_position), name, font=font, fill=(0, 0, 0))
        img.save("{}.png".format(name))

        filename = "{}.png".format(name)

        with open(filename, "rb") as attachment:
            # Add file as application/octet-stream
            # Email client can usually download this automatically as attachment
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        # Encode file in ASCII characters to send by email
        encoders.encode_base64(part)

        # Add header as key/value pair to attachment part
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )

        # Add attachment to message and convert message to string
        message.attach(part)
        text = message.as_string()

        print(f"Sending email to {name} at {receiver_email}")
        smtp.sendmail(EMAIL_ADDRESS, str(i[1]["email"]), text)

        print(f"Deleting image {filename}")
        os.remove(filename)

print("All done :)")