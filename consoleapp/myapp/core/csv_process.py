import sys
from myapp.exception import ApplicationException
from myapp.core.generic_process import GenericProcess


class CsvProcess(GenericProcess):
    def __init__(self, command, file) -> None:
        super().__init__(file)
        self.file = file
        self.command = command.strip().upper()

    def process(self):
        try:
            self.to_csv(self.read_csv(), self.file)
        except Exception as e:
            raise ApplicationException(self.command, e, sys)
        else:
            return {"filename": self.file, "filepath": self.filepath}
