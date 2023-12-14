from importlib import import_module


class LazyLoader:
    def __init__(self) -> None:
        self.loaded_classes = {}
        self.loaded_config = None

    def load_class(self, module_name, class_name, file):
        if class_name not in self.loaded_classes:
            module = import_module(module_name)
            class_obj = getattr(module, class_name)
            self.loaded_classes[class_name] = class_obj(file)

        return self.loaded_classes[class_name]

    def load_config(self, key):
        if not self.loaded_config:
            self.loaded_config = {
                "ALLOWED_EXTENSIONS": (".csv", ".xlsx"),
                "MODULE_NAME": {".csv": "myapp.core.csv_process", ".xlsx": "myapp.core.excel_process"},
                "CLASS_NAME": {".csv": "CsvProcess", ".xlsx": "ExcelProcess"}
            }

        return self.loaded_config.get(key)
