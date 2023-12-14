import os
import sys
import socket
import smtplib

from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from myapp.core.base import Base
from myapp.config import Configuration
from myapp.exception import ApplicationException

class Email(Base):
	def __init__(self, args) -> None:
		super().__init__(args)
		self.logger = self.get_logger(__name__)

	def subject(self) -> str:
		subject = f"SUCCESS - {self.command} Process Status Update for {self.date}"
		return subject

	def body(self) -> str:
		body = f"Hi, </br></br>{self.command} process for date {self.date} is completed successfully. </br></br>"
		body += "Thank you,</br><b>Application Support Team</b>"
		return body

	def Send(self) -> None:
		server = smtplib.SMTP(Configuration.SERVER, 587)
		server.ehlo()
		server.starttls()

		message = MIMEMultipart()
		message["Subject"] = self.subject()
		message["From"] = Configuration.SENDER
		message["To"] = ", ".join(Configuration.RECEIVER)
		mime_text = MIMEText(self.body(), "html")
		message.attach(mime_text)

		server.sendmail(Configuration.SENDER, Configuration.RECEIVER, message.as_string())
		self.logger.info("Email send successfully.")

