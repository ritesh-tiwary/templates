from myapp.utils import Utils
from myapp.logging import Logger
from myapp.config import Configuration
from myapp.core.lazy_loader import LazyLoader


class Base:
	def __init__(self, args) -> None:
		self.lazy_loader = LazyLoader()
		self.date = args.date.strip()
		self.command = args.command.strip().upper()
		self.utils = Utils(self.command, self.date)
		self.configuration = Configuration(self.command).get()
		self.allowed_extensions = lambda file: any(file.endswith(ext) for ext in self.lazy_loader.load_config("ALLOWED_EXTENSIONS"))

	def get_logger(self, logger_name):
		return Logger(self.command, logger_name)

