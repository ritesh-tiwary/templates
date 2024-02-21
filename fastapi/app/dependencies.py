from uuid import UUID
from typing import Annotated
from fastapi import Header, HTTPException


async def get_request_id_header(X_Request_Id: Annotated[str, Header()]):
    try:
        UUID(X_Request_Id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid Header - X-Request-Id")

async def get_checksum_header(X_Checksum: Annotated[str, Header()]):
    if len(X_Checksum).__ne__(32):
        raise HTTPException(status_code=400, detail="Invalid Header - X-Checksum")
