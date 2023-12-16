from myapp.core.base import Base


class ProcessManager(Base):
	def __init__(self, args) -> None:
		super().__init__(args)
		self.logger = self.get_logger(__name__)

	def __enter__(self):
		return self.configuration.get("Files")

	def __exit__(self, exc_type, exc_message, exc_traceback):
		if exc_message and exc_type.__name__.__ne__("ApplicationException"):
			error_message = f"\nApplication Exception\n{'**'*50}\n{'Error Type'.ljust(14)}: {exc_type.__name__}\nError Message : {exc_message}\n{'Line No'.ljust(14)}: {exc_traceback.tb_lineno}\n{'File'.ljust(14)}: {exc_traceback.tb_frame.f_code.co_filename}\n{'**'*50}\n"
			self.logger.exception(error_message)
