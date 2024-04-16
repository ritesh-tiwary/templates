from app.logger import Logger
from functools import lru_cache
from typing import List, Annotated
from app.core.jwt_issuer import JwtIssuer
from app.models import ValidateTokenModel
from app.dependencies import get_request_id_header
from fastapi import APIRouter, Depends, HTTPException, status


router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
    dependencies=[Depends(get_request_id_header)],
    responses={404: {"Description": "Not found"}}
    )

logger = Logger()

@lru_cache
def get_jwt_issuer() -> JwtIssuer:
    return JwtIssuer()

@router.post("/token", status_code=status.HTTP_201_CREATED)
async def jwt_token(jwt_issuer: Annotated[JwtIssuer, Depends(get_jwt_issuer)]):
    """
    Endpoint to generate access token.

    - **X-Request-Id**: A 36-character UUID (Universal Unique Identifier) is hexadecimal number that is generated for each request.

            7cd35adb-1484-2348-df3e-f077cd6ff34d
    """
    try:
        jwt_token = jwt_issuer.issue_jwt_token()
        logger.info("Token generated successfully.")
        return {"token": jwt_token}
    except Exception as exc:
        logger.error(f"Failed to generate token: {exc}")
        raise HTTPException(status_code = status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"{str(exc)} - Error occured while processing the request")

@router.post("/checktoken", status_code=status.HTTP_200_OK)
async def check_token(token: ValidateTokenModel, jwt_issuer: Annotated[JwtIssuer, Depends(get_jwt_issuer)]):
    """
    Endpoint to generate access token.

    - **X-Request-Id**: A 36-character UUID (Universal Unique Identifier) is hexadecimal number that is generated for each request.

            7cd35adb-1484-2348-df3e-f077cd6ff34d
    """
    try:
        is_valid = jwt_issuer.is_token_valid(token.token)
        logger.info("Token validated successfully.")
        return {"is_valid": is_valid}
    except Exception as exc:
        logger.error(f"Failed to validate token: {exc}")
        raise HTTPException(status_code = status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"{str(exc)} - Error occured while processing the request")
