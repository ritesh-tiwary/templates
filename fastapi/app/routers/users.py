from fastapi import APIRouter


router = APIRouter()

@router.get("/users/", tags=["users"])
async def get_users():
    return [{"UserName": "Rishu"}, {"UserName": "Ritesh"}]

@router.get("/users/me", tags=["users"])
async def get_current_users():
    return {"UserName": "Ritesh"}

@router.get("/users/{username}", tags=["users"])
async def get_user(username: str):
    return {"UserName": username}
