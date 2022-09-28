from sqlalchemy import SmallInteger, String, Integer
from sqlalchemy import ForeignKey, Column, Index, text
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Albums(Base):

    __tablename__ = "albums"

    __table_args__ = (
        Index(
            "album_search_index",
            text("(album_name || ' ' || albums.artist_name)"),
            postgresql_ops={"artist_name": "gin_trgm_ops"},
            postgresql_using="gin",
        ),
    )

    id = Column("album_id", String, primary_key=True)
    name = Column("album_name", String, nullable=False)
    artist_name = Column("artist_name", String, nullable=False)
    album_image = Column("album_image", String, nullable=True)
    total_tracks = Column("total_tracks", SmallInteger)
    release_date = Column("album_release_date", Integer)
    popularity = Column("album_popularity", Integer)

    artist_id = Column("artist_id", ForeignKey("artists.artist_id"), nullable=False)

    tracks = relationship("Tracks", backref="Albums")
