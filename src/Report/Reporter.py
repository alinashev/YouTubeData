import smtplib
import ssl
from datetime import datetime
from email import encoders
from email.mime.base import MIMEBase
from typing import Any

import settings

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Reporter:
    file: Any
    recipient: str

    def __init__(self, file, recipient) -> None:
        self.file = file
        self.recipient = recipient

    def send(self) -> None:
        time: datetime = datetime.utcnow()
        subject: str = 'Report: {year}-{month}-{day}-{hour}-{minute}-{second}'.format(year=time.year,
                                                                                      month=time.month,
                                                                                      day=time.day,
                                                                                      hour=time.hour,
                                                                                      minute=time.minute,
                                                                                      second=time.second
                                                                                      )
        body: str = 'report'

        message: MIMEMultipart = MIMEMultipart()
        message["From"]: MIMEMultipart = settings.email_sender
        message["To"]: MIMEMultipart = self.recipient
        message["Subject"]: MIMEMultipart = subject

        message.attach(MIMEText(body, "plain"))

        with open(self.file, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {self.file}",
        )

        message.attach(part)
        text = message.as_string()

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", settings.smtp_port, context=context) as server:
            server.login(settings.email_sender, settings.email_pass)
            server.sendmail(settings.email_sender, self.recipient, text)
