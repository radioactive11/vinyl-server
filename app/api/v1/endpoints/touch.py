from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def _touch():
    return {"hello": "world"}
