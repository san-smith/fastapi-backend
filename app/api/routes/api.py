from fastapi import APIRouter

from app.api.routes import users, authentication

router = APIRouter()
router.include_router(authentication.router, tags=["authentication"], prefix="/users")
router.include_router(users.router, tags=["users"], prefix="/user")

# @router.get("/")
# def read_root():
#     return {"Hello": "World"}
