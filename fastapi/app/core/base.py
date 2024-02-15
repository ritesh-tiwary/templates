from fastapi.app.core.lazy_loader import LazyLoader


class Base:
    def __init__(self) -> None:
        self.lazy_loader = LazyLoader()
        self.allowed_extensions = lazy_loader.load_config("ALLOWED_EXTENSIONS")
