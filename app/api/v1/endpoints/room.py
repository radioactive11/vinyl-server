from redis import Redis
from fastapi import APIRouter, Depends, Response, status

from app.api import deps

from app.schema.room import (
    CreateRoom,
    DeleteRoom,
    RemovePlayer,
    UpdateScore,
    AddPlayer,
    RemovePlayer,
)
from app.core.room_handler import room

from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/create")
def _create(
    request_body: CreateRoom,
    response: Response,
    redis_client: Redis = Depends(deps.get_redis),
):

    room_creation_status = room.create(
        admin_id=request_body.admin_id,
        room_id=request_body.room_id,
        redis_client=redis_client,
    )

    message = f"Room with ID {request_body.room_id} created"
    response.status_code = status.HTTP_201_CREATED

    if not room_creation_status:
        message = f"Room with ID {request_body.room_id} already exists"
        response.status_code = status.HTTP_409_CONFLICT

    return {"message": message}


@router.delete("/delete")
def delete_room(
    request_body: DeleteRoom, redis_client: Redis = Depends(deps.get_redis)
):
    room.delete(request_body.room_id, redis_client)

    return {"message": f"deleted room {request_body.room_id}"}


@router.post("/add_player")
def add_player(request_body: AddPlayer, redis_client: Redis = Depends(deps.get_redis)):
    room.add_member(request_body.room_id, request_body.user_id, redis_client)

    return {"message": f"Added {request_body.user_id} to {request_body.room_id}"}


@router.post("/remove_player")
def remove_plater(
    request_body: RemovePlayer, redis_client: Redis = Depends(deps.get_redis)
):
    updated_players = room.remove_player(
        request_body.room_id, request_body.user_id, redis_client
    )

    return updated_players


@router.put("/update_score")
def update_score(
    request_body: UpdateScore, redis_client: Redis = Depends(deps.get_redis)
):
    updated_result = room.update_score(
        request_body.scores, request_body.room_id, redis_client
    )

    return {request_body.room_id: updated_result}
