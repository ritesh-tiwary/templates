from functools import lru_cache
from app.settings import Settings
from app.core.lazy_loader import LazyLoader


class Base:
    def __init__(self) -> None:
        self.settings = self.get_settings()
        self.user_name = self.settings.user_name
        self.host_name = self.settings.host_name
        self.public_key_pem = self.get_public_key_pem()
        self.private_key_pem = self.get_private_key_pem()
        self.lazy_loader = LazyLoader()
        self.allowed_extensions = self.lazy_loader.load_config("ALLOWED_EXTENSIONS")

    @lru_cache
    def get_settings(self) -> Settings:
        return Settings()

    @lru_cache
    def get_public_key_pem(self) -> bytes:
        with open(self.settings.public_key, "rb") as f:
            public_key_pem = f.read()
        return public_key_pem

    @lru_cache
    def get_private_key_pem(self) -> bytes:
        with open(self.settings.private_key, "rb") as f:
            private_key_pem = f.read()
        return private_key_pem
