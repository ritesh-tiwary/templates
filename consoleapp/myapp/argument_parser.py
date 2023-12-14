import myapp
import argparse
from datetime import datetime
from myapp.command import Command


class Parser:
	def __init__(self) -> None:
		self.command = Command()

	def get(self) -> argparse.ArgumentParser:
		parser = argparse.ArgumentParser(myapp.__app_name__)
		parser.add_argument("--version", action="version", version=myapp.__version__)
		subparsers = parser.add_subparsers()

		run_parser = subparsers.add_parser("run")
		run_parser.add_argument("--command", required=True, help="Command Name")
		run_parser.add_argument("--date", default=datetime.strftime(datetime.now().date(), "%Y%m%d"), help="Order Date [YYYYMMDD]")
		run_parser.set_defaults(func=self.command.run)

		email_parser = subparsers.add_parser("email")
		email_parser.add_argument("--command", required=True, help="Command Name")
		email_parser.add_argument("--date", default=datetime.strftime(datetime.now().date(), "%Y%m%d"), help="Order Date [YYYYMMDD]")
		email_parser.set_defaults(func=self.command.email)

		cleanup_parser = subparsers.add_parser("cleanup")
		cleanup_parser.add_argument("--command", required=True, help="Command Name")
		cleanup_parser.add_argument("--date", default=datetime.strftime(datetime.now().date(), "%Y%m%d"), help="Order Date [YYYYMMDD]")
		cleanup_parser.set_defaults(func=self.command.cleanup)

		return parser

