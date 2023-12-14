import os
import glob
from myapp.core.base import Base


class Cleanup(Base):
	def __init__(self, args) -> None:
		super().__init__(args)
		self.logger = self.get_logger(__name__)

	def Clean(self) -> None:
		if not self.configuration:
			self.logger.info(f"{self.command} - Commnad is not defined.")
			return

		self.logger.info(f"Deleting log files {'..'*20}")
		log_files = self.utils.get_log_files()
		self.delete(log_files)

	def delete(self, files) -> None:
		try:
			for file in files:
				for f in glob.glob(file):
					if os.path.isfile(f):
						os.remove(f)
						self.logger.info(f"Deleted - {os.path.basename(f)}")
					else:
						self.logger.info(f"{os.path.basename(f)} - File not found")
		except:
			pass
