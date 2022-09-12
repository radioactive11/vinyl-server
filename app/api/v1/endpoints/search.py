from fastapi import APIRouter, Depends

from app.api import deps

from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/artists")
def search_artist(
    q: str, limit: int = 10, offset: int = 0, db: Session = Depends(deps.get_db)
):
    return {"search": "working"}
