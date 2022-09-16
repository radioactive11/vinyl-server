from fastapi import APIRouter

from app.api.v1.endpoints import touch, search, room


api_router = APIRouter()

api_router.include_router(touch.router, prefix="/touch")
api_router.include_router(search.router, prefix="/search")
api_router.include_router(room.router, prefix="/room")
