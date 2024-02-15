from importlib import import_module


class LazyLoader:
    def __init__(self) -> None:
        self.loaded_config = None

    def load_config(self, key):
        if not self.loaded_config:
            self.loaded_config = {
                "ALLOWED_EXTENSIONS": ("txt", "csv", "xlsx", "zip")
            }

        return self.loaded_config.get(key)
