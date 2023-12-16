from app.core.base import Base


class Transformer(Base):
    def __init__(self) -> None:
        super().__init__()
        self.validate = lambda file: any(file.endswith(ext) for ext in self.allowed_extensions)

    def Transform(self):
        if self.validate("test.xml"): return self.transformer.transform()
