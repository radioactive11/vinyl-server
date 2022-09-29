from redis import Redis


class Room:
    # All room related operations
    def add_member(self, room_id: str, user_id: str, redis_client: Redis):
        redis_client.lpush(f"room:{room_id}:members", user_id)
        redis_client.zadd(f"room:{room_id}:leaderboard", {user_id: 0})

    def update_score(self, scores: dict, room_id: str, redis_client: Redis):
        for player in scores.items():
            user_id, score_incr = player
            redis_client.zincrby(f"room:{room_id}:leaderboard", score_incr, user_id)

        updated_scores = redis_client.zrange(
            f"room:{room_id}:leaderboard", 0, -1, withscores=True
        )

        return updated_scores

    def delete(self, room_id: str, redis_client: Redis):
        """Delete a room

        Args:
            room_id (str): room ID to delete
            redis_client (Redis): redis client
        """
        redis_client.delete(
            f"room:{room_id}:members",
            f"room:{room_id}:admin",
            f"room:{room_id}:leaderboard",
        )
        redis_client.setbit(f"room:{room_id}", 1, 0)

    def remove_player(self, room_id: str, user_id: str, redis_client: Redis):
        redis_client.lrem(f"room:{room_id}:members", 0, user_id)

        return redis_client.lrange(f"room:{room_id}:members", 0, -1)

    def create(self, admin_id: str, room_id: str, redis_client: Redis) -> bool:
        """
        Creates a new room
        * Check if room with id exists
        * Reserves id, else returns False
        * Sets admin of room
        * Adds admin as a player of that room
        Args:
            admin_id (str): ID of the admin of the room
            room_id (str): ID of the room,
            redis_client (Redis): redis client

        Returns:
            bool: room creatation status
        """
        room_exists = redis_client.getbit(f"room:{room_id}", 1)

        if room_exists:
            return False

        redis_client.setbit(f"room:{room_id}", 1, 1)

        redis_client.set(f"room:{room_id}:admin", admin_id)
        redis_client.lpush(f"room:{room_id}:members", admin_id)
        redis_client.zadd(f"room:{room_id}:leaderboard", {admin_id: 0})

        return True


room = Room()
