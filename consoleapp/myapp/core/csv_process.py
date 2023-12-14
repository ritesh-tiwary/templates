from myapp.core.generic_process import GenericProcess


class CsvProcess(GenericProcess):
    def __init__(self, file) -> None:
        super().__init__(file)
        self.file = file

    def process(self):
        self.to_csv(self.read_csv(), self.file)
        return {"filename": self.file, "filepath": self.filepath}
