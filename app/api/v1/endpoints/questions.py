from fastapi import APIRouter, Depends, Response, status

from sqlalchemy.orm import Session
from redis import Redis

from app.api import deps
from core.questions import QuestionGenerator
from schema.questions import GenerateQuestions, FetchQuestions

import json

router = APIRouter()


@router.post("/create")
def create_question(
    request_body: GenerateQuestions,
    db: Session = Depends(deps.get_db),
    redis_client: Redis = Depends(deps.get_redis),
):
    qg = QuestionGenerator(db, request_body.track_ids)
    questions = qg.generate(10)

    redis_client.set(f"room:{request_body.room_id}:questions", json.dumps(questions))

    return {"status": "ok"}


@router.post("/fetch")
def fetch_questions(
    request_body: FetchQuestions,
    response: Response,
    redis_client: Redis = Depends(deps.get_redis),
):
    questions = redis_client.get(f"room:{request_body.room_id}:questions")

    if questions is None:
        response.status_code = status.HTTP_204_NO_CONTENT
        return {}

    questions_json = json.loads(questions)

    return questions_json
