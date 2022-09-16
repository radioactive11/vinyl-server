from pydantic import BaseModel


class CreateRoom(BaseModel):
    admin_id: str
    room_id: str


class DeleteRoom(BaseModel):
    room_id: str


class AddPlayer(BaseModel):
    user_id: str
    room_id: str


class UpdateScore(BaseModel):
    room_id: str
    scores: dict
