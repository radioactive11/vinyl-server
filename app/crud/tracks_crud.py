from sqlalchemy.orm import Session

from models.album import Albums
from models.artist import Artists
from models.tracks import Tracks


class TracksCRUD:
    def intersect(self, db: Session, tracks: list):
        return (
            db.query(Tracks)
            .filter(Tracks.id.in_(tracks))
            .join(Albums, Tracks.album_id == Albums.id)
            .join(Artists, Artists.id == Albums.artist_id)
            .all()
        )
