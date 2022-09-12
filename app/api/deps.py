from typing import Generator

from fastapi import Header, Response, HTTPException
from fastapi.encoders import jsonable_encoder

from app.db.sesison import SessionLocal


import os
import json
from dotenv import load_dotenv

load_dotenv()


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db

    except Exception as e:
        print(e)

    finally:
        db.close()
