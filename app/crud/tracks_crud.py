from sqlalchemy.orm import Session

from models.album import Albums
from models.artist import Artists
from models.tracks import Tracks


class TracksCRUD:
    def intersect(self, db: Session, tracks: list):
        query_result = (
            db.query(Tracks, Albums)
            .filter(Tracks.id.in_(tracks))
            .join(Albums, Tracks.album_id == Albums.id)
            .join(Artists, Artists.id == Albums.artist_id)
            .all()
        )

        results = []

        for item in query_result:
            track = item._asdict()["Tracks"]
            album = item._asdict()["Albums"]

            temp_dict = {"track": track.__dict__, "album": album.__dict__}

            results.append(temp_dict)

        return results


query_handler = TracksCRUD()
