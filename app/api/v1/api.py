from fastapi import APIRouter

from app.api.v1.endpoints import touch


api_router = APIRouter()

api_router.include_router(touch.router, prefix="/touch") 
