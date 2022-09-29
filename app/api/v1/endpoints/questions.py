from fastapi import APIRouter, Depends, Response, status

from sqlalchemy.orm import Session
from redis import Redis

from app.api import deps
from core.questions import QuestionGenerator
from schema.questions import GenerateQuestions, FetchQuestions, CheckAnswer

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

    for question in questions:
        track_id = question["question_id"]
        track_name = question["name"]
        redis_client.set(f"track_id:{track_id}", track_name)

    redis_client.set(f"room:{request_body.room_id}:questions", json.dumps(questions))

    return {"questions": questions}


@router.post("/check")
def check_answer(request_body: CheckAnswer, redis_client=Depends(deps.get_redis)):
    actual = redis_client.get(f"track_id:{request_body.question_id}")
    if actual is None:
        return {"result": "False"}

    actual = actual.decode()
    if actual.lower() == request_body.answer.lower():
        return {"result": "True"}

    return {"result": "False"}


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
