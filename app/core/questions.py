from pprint import pprint
from sqlalchemy.orm import Session

from crud.tracks_crud import query_handler


class QuestionGenerator:
    def generate(self, limit: int):
        limit = min(len(self.__tracks), limit)
        # self.__tracks = self.__tracks[:limit]

        questions = []

        for item in self.__tracks:
            track_id = item["track"]["id"]
            cluster_id = item["track"]["cluster_id"]
            content_id = item["track"]["content_id"]

            url = f"https://listen.rezo.live/preview/{cluster_id}/{content_id}_96_p.mp4"
            name = item["track"]["name"]
            image = item["album"]["album_image"]

            temp_dict = {
                "name": name,
                "image": image,
                "url": url,
                "question_id": track_id,
            }
            questions.append(temp_dict)

        return questions

    def __init__(self, db: Session, playlist_tracks: list) -> None:
        self.__tracks = query_handler.intersect(db, playlist_tracks)
