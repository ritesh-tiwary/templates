import logging
from aiologger import Logger
from aiologger.records import LogRecord
from app.logger.splunk_logger import SplunkLogger


SPLUNK_HEC_URL = "https://your_splunk_instance:port/services/collector/raw?token=your_token"


# # Create a custom filter to include context variables in log records
# class ContextFilter(Filter):
#     def __init__(self, context):
#         self.context = context

#     async def filter(self, record: LogRecord) -> bool:
#         record.extra.update(self.context)
#         return True


# # Create a custom formatter to format log messages
# class CustomFormatter(Formatter):
#     async def format(self, record: LogRecord) -> str:
#         return f"{record.extra.get('request_id', '')}: {record.msg}"


# Create a logger instance
class AppLogger(Logger):
    def __init__(self, logger = None):
        self.logger = Logger.with_default_handlers(name="file_uploader", level=logging.INFO)
        if logger: self.logger = SplunkLogger(SPLUNK_HEC_URL, logger)
