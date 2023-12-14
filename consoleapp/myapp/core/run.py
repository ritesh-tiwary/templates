import os
from myapp.core.base import Base
from myapp.core.process_manager import ProcessManager


class Run(Base):
	def __init__(self, args) -> None:
		super().__init__(args)
		self.args = args
		self.logger = self.get_logger(__name__)		

	def Run(self) -> None:
		if not self.configuration:
			self.logger.info(f"{self.command} - Command is not defined.")
			return

		with ProcessManager(self.args) as p:
			for f in p:
				f = f.replace("YYYYMMDD", self.date)
				file_extension = os.path.splitext(f)[1]
				if self.allowed_extensions(file_extension):
					module_name = self.lazy_loader.load_config("MODULE_NAME").get(file_extension)
					class_name = self.lazy_loader.load_config("CLASS_NAME").get(file_extension)
					processor = self.lazy_loader.load_class(module_name, class_name, f) if class_name else None
					result = processor.process()
					self.logger.info(f'File : {result["filename"]}\nPath : {result["filepath"]}\n')
				else:
					self.logger.info(f'{f} - Invalid file')
