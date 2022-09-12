from fastapi import APIRouter, Depends

from app.api import deps
from app.crud.artist_crud import artists

from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/artists")
def search_artist(
    q: str, limit: int = 10, offset: int = 0, db: Session = Depends(deps.get_db)
):

    items = artists.search_artist(db, q)
    return items
