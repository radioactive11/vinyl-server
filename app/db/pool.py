import redis
from redis import Redis

from app.core.config import redis_settings


class RedisHandler(object):
    shared_state = {}

    def __init__(self) -> None:
        self.__dict__ = self.shared_state

    def redis_connect(self) -> Redis:
        connection_pool = redis.ConnectionPool.from_url(
            url=redis_settings.REDIS_CONN_STRING
        )
        return redis.Redis(connection_pool=connection_pool)
