import os
from typing import List
from myapp.config import Configuration


class Utils:
	def __init__(self, command, date) -> None:
		self.date = date.strip()
		self.command = command.strip().upper()

	def get_log_files(self) -> List[str]:
		"""
		Return list of log files
		"""
		log_dir = os.path.join(Configuration.LOG_DIR, self.command)
		log_files = [os.path.join(log_dir, f"MYAPP_{self.command}_{self.date}_*.log")]
		return log_files

