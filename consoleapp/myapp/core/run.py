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
			print(*p)
		
