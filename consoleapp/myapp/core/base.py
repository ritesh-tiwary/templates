from myapp.utils import Utils
from myapp.logging import Logger
from myapp.config import Configuration


class Base:
	def __init__(self, args) -> None:
		self.date = args.date.strip()
		self.command = args.command.strip().upper()
		self.utils = Utils(self.command, self.date)
		self.configuration = Configuration(self.command).get()

	def get_logger(self, logger_name):
		return Logger(self.command, logger_name)

