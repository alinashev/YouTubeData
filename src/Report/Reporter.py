import os
import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase

import settings

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Reporter:
    @staticmethod
    def seng_report_to_email(file, recipient):
        subject: str = 'New Report'
        body: str = 'report'

        message: MIMEMultipart = MIMEMultipart()
        message["From"]: MIMEMultipart = settings.email_sender
        message["To"]: MIMEMultipart = recipient
        message["Subject"]:MIMEMultipart = subject

        message.attach(MIMEText(body, "plain"))

        with open(file, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {file}",
        )

        message.attach(part)
        text = message.as_string()

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(settings.email_sender, settings.email_pass)
            server.sendmail(settings.email_sender, recipient, text)