from app.core.lazy_loader import LazyLoader


class Base:
    def __init__(self) -> None:
        lazy_loader = LazyLoader()
        self.allowed_extensions = lazy_loader.load_config("ALLOWED_EXTENSIONS")
        module_name = lazy_loader.load_config("MODULE_NAME").get("xml")
        class_name = lazy_loader.load_config("CLASS_NAME").get("xml")
        self.transformer = lazy_loader.load_class(module_name, class_name)
