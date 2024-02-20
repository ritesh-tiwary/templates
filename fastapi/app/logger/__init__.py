import sys
from aiologger import Logger
from aiologger.formatters.base import Formatter
from aiologger.handlers.streams import AsyncStreamHandler
from app.logger.splunk_logger import SplunkLogger


SPLUNK_HEC_URL = "https://your_splunk_instance:port/services/collector/raw?token=your_token"

class Logger(Logger):
    def __init__(self, *args, name="fastapi-logger", enable_splunk=False, **kwargs):
        super().__init__(*args, name="fastapi-logger", **kwargs)

        if enable_splunk: 
            self.logger = SplunkLogger(SPLUNK_HEC_URL)
        else:
            formatter = Formatter('%(asctime)s [%(filename)15s] [line:%(lineno)3d] [%(name)s] %(levelname)s %(message)s')
            handler = AsyncStreamHandler()
            handler.formatter = formatter
            self.add_handler(handler)
