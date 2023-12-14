import os


class Configuration:
	SERVER = os.getenv("SERVER")
	SENDER = os.getenv("SENDER")
	RECEIVER = os.getenv("RECEIVER")
	LOG_DIR	= os.getenv("LOG_DIR")
	INBOUND	= os.getenv("INBOUND")
	OUTBOUND = os.getenv("OUTBOUND")
	TRACEBACK = eval(os.getenv("TRACEBACK"))

	def __init__(self, command) -> None:
		self.command = command

	def get(self) -> dict:
		"""
		Return job configuration
		"""
		expr = os.getenv(self.command)
		if expr and expr.__ne__(""):
			return eval(expr)
