import os
import logging
from datetime import datetime
from myapp.config import Configuration


class Logger:
	def __init__(self, command, logger_name) -> None:
		self.logger_name = logger_name
		command = command.strip().upper()
		configuration = Configuration(command).get()
		log_dir = os.path.join(Configuration.LOG_DIR, command if configuration else "UNDEFINED")
		os.makedirs(log_dir, exist_ok=True)
		filename = f"MYAPP_{command}_{datetime.now().strftime('%Y%m%d__%H%M%S')}.log"
		self.log_file = os.path.join(log_dir, filename)

	def logger(self):
		logging.basicConfig(
			filename = self.log_file,
			format = "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
			level = logging.INFO
		)
		logger = logging.getLogger(self.logger_name)
		return logger

	def info(self, message):
		logger = self.logger()
		logger.info(message)
		print(message)

	def exception(self, message):
		logger = self.logger()
		logger.exception(message)
		print(message)

