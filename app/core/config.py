from threading import local
from typing import List, Dict, Optional
from typing_extensions import Self

from pydantic import AnyHttpUrl, BaseSettings, PostgresDsn

import os
from dotenv import load_dotenv


class DBSettings:
    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    def __init__(self, mode: str) -> None:
        load_dotenv()

        if mode == "local":

            self.POSTGRES_SERVER = os.getenv("LOCAL_DATABASE_URL")
            self.POSTGRES_USER = os.getenv("LOCAL_DB_USER")
            self.POSTGRES_PASSWORD = os.getenv("LOCAL_DB_PASSWORD")
            self.POSTGRES_DB = os.getenv("LOCAL_DB_NAME")

        elif mode == "prod":
            self.POSTGRES_SERVER = os.getenv("PROD_DATABASE_URL")
            self.POSTGRES_USER = os.getenv("PROD_DB_USER")
            self.POSTGRES_PASSWORD = os.getenv("PROD_DB_PASSWORD")
            self.POSTGRES_DB = os.getenv("PROD_DB_NAME")

        else:
            raise ValueError("mode should be local or prod")


class RedisSettings:
    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_DB: int

    def __init__(self, mode: str = "prod") -> None:
        load_dotenv()

        if mode == "prod":
            self.REDIS_HOST = os.getenv("REDIS_HOST")
            self.REDIS_PORT = os.getenv("REDIS_PORT")
            self.REDIS_DB = 0
            self.REDIS_USER = os.getenv("REDIS_USER")
            self.REDIS_PW = os.getenv("REDIS_PW")
            self.REDIS_CONN_STRING = os.getenv("REDIS_CONNECTION_STRING")

        if mode == "local":
            self.REDIS_HOST = os.getenv("REDIS_HOST")
            self.REDIS_PORT = os.getenv("REDIS_PORT")
            self.REDIS_DB = 0
            self.REDIS_USER = os.getenv("REDIS_USER")
            self.REDIS_PW = os.getenv("REDIS_PW")
            self.REDIS_CONN_STRING = "redis://localhost:6379/0"


db_settings = DBSettings("prod")
redis_settings = RedisSettings("local")
