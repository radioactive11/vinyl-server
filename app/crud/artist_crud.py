from typing import List

from sqlalchemy.orm import Session
from sqlalchemy import text

from app.models.artist import Artists


class ArtistCRUD:
    def search_artist(self, db: Session, q: str) -> List:
        return (
            db.query(Artists.id, Artists.name, Artists.image)
            .filter(text("artist_name % :q"))
            .params(q=q)
            .order_by(Artists.popularity.desc())
            .all()
        )


artists = ArtistCRUD()
