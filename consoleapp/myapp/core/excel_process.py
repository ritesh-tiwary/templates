from myapp.core.generic_process import GenericProcess


class ExcelProcess(GenericProcess):
    def __init__(self, file) -> None:
        super().__init__(file)
        self.file = file

    def process(self):
        self.to_excel(self.read_excel(), self.file)
        return {"filename": self.file, "filepath": self.filepath}
