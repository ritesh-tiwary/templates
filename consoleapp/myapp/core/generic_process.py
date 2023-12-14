import os
from re import sub
from pandas import read_csv
from pandas import read_excel
from functools import partial
from myapp.config import Configuration
from abc import ABC, abstractclassmethod


class GenericProcess(ABC):
    def __init__(self, file) -> None:
        super().__init__()
        self.read_csv = partial(read_csv, os.path.join(Configuration.INBOUND, file))
        self.read_excel = partial(read_excel, os.path.join(Configuration.INBOUND, file))
        self.sanitize_column_name = lambda column_name: sub(r"\s+|[^a-zA-Z0-9_.-]", "_", column_name)

    @abstractclassmethod
    def process(self):...

    def to_csv(self, df, file) -> None:
        df.columns = list(map(self.sanitize_column_name, df.columns))
        self.filepath = os.path.join(Configuration.OUTBOUND, file)
        df.to_csv(self.filepath, index=False)

    def to_excel(self, df, file) -> None:
        df.columns = list(map(self.sanitize_column_name, df.columns))
        self.filepath = os.path.join(Configuration.OUTBOUND, file)
        df.to_excel(self.filepath, index=False)
