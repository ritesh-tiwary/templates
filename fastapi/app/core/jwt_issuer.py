import jwt
import uuid
from app.core.base import Base
from datetime import datetime, timedelta, timezone


class JwtIssuer(Base):
    def __init__(self) -> None:
        super().__init__()
        self.expiration_time = datetime.now(tz=timezone.utc)

    def issue_jwt_token(self) -> str:
        self.expiration_time = datetime.now(tz=timezone.utc) + timedelta(hours=1)
        payload = {"unique_name": self.user_name, "exp": self.expiration_time}
        unique_id = uuid.uuid5(uuid.NAMESPACE_DNS, self.host_name)
        headers = {"kid": str(unique_id)}
        jwt_token = jwt.encode(payload=payload, key=self.private_key_pem, algorithm="RS512", headers=headers)
        return jwt_token
    
    def is_token_valid(self, jwt_token) -> bool:
        try:
            jwt.decode(jwt=jwt_token, key=self.public_key_pem, algorithms="RS512")
        except jwt.ExpiredSignatureError:
            return False
        except jwt.exceptions.DecodeError:
            return False
        except jwt.exceptions.InvalidTokenError:
            return False
        else:
            return True
