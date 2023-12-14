from myapp.core.run import Run
from myapp.logging import Logger
from myapp.core.email import Email
from myapp.core.cleanup import Cleanup


class Command:
	def run(self, args):
		"""
		Command:
		========
		myapp run --command test --date YYYYMMDD
		"""
		self.logger = Logger(args.command, __name__)
		self.logger.info(f"{'>>'*10} [COMMAND INITIATED] myapp run --command {args.command} --date {args.date} {'<<'*10}")
		Run(args).Run()
		self.logger.info(f"{'>>'*10} [COMMAND COMPLETED] myapp run --command {args.command} --date {args.date} {'<<'*10}")

	def email(self, args):
		"""
		Command:
		========
		myapp email --command test --date YYYYMMDD
		"""
		self.logger = Logger(args.command, __name__)
		self.logger.info(f"{'>>'*10} [COMMAND INITIATED] myapp email --command {args.command} --date {args.date} {'<<'*10}")
		Email(args).Send()
		self.logger.info(f"{'>>'*10} [COMMAND COMPLETED] myapp email --command {args.command} --date {args.date} {'<<'*10}")

	def cleanup(self, args):
		"""
		Command:
		========
		myapp cleanup --command test --date YYYYMMDD
		"""
		self.logger = Logger(args.command, __name__)
		self.logger.info(f"{'>>'*10} [COMMAND INITIATED] myapp cleanup --command {args.command} --date {args.date} {'<<'*10}")
		Cleanup(args).Clean()
		self.logger.info(f"{'>>'*10} [COMMAND COMPLETED] myapp cleanup --command {args.command} --date {args.date} {'<<'*10}")

