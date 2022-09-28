from fastapi import APIRouter


router = APIRouter()


@router.get("/artist/{id}/tracks")
def tracks_of_artist():
    pass
