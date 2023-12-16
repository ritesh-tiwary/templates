import sys
from myapp.logging import Logger
from myapp.config import Configuration


def disable_traceback():
	if sys.platform.__eq__("linux"):
		sys.stderr = open("/dev/null", "w")
	elif sys.platform.__eq__("win32"):
		sys.stderr = open("nul", "w")

def error_message_details(error_logger, error, error_details: sys) -> str:
	exc_type, _, exc_tb = error_details.exc_info()
	code_filename = exc_tb.tb_frame.f_code.co_filename
	error_message = f"\nApplication Exception\n{'**'*50}\n{'Error Type'.ljust(14)}: {exc_type.__name__}\nError Message : {error}\n{'Line No'.ljust(14)}: {exc_tb.tb_lineno}\n{'File'.ljust(14)}: {code_filename}\n{'**'*50}\n"
	error_logger.exception(error_message)
	return error_message


class ApplicationException(Exception):
	def __init__(self, command, error, error_details: sys) -> None:
		self.logger = Logger(command, __name__)
		if Configuration.DISABLE_TRACEBACK: disable_traceback()
		self.error_message = error_message_details(self.logger, error, error_details)
