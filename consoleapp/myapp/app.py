from myapp.argument_parser import Parser


def main():
    parser = Parser().get()
    args = parser.parse_args()
    args.func(args)
	# try:
	# 	parser = Parser().get()
	# 	args = parser.parse_args()
	# 	args.func(args)
	# except AttributeError:
	# 	parser.print_help()
	# except Exception:
	# 	raise
