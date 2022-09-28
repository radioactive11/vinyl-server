from sqlalchemy import String, Float
from sqlalchemy import ForeignKey, Column, Index, text
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Tracks(Base):

    __tablename__ = "tracks"
    __table_args__ = (
        Index(
            "track_search_index",
            text("(track_name || ' ' || tracks.artist_name)"),
            postgresql_ops={"artist_name": "gin_trgm_ops"},
            postgresql_using="gin",
        ),
    )

    # Meta details
    id = Column("track_id", String, primary_key=True)
    name = Column("track_name", String, nullable=False)
    artist_name = Column("artist_name", String, nullable=False)

    # CDN details
    cdn_id = Column("cdn_id", String, nullable=True)
    cluster_id = Column("cluster_id", String, nullable=True)
    content_id = Column("content_id", String, nullable=True)

    album_id = Column("album_id", ForeignKey("albums.album_id"), nullable=False)
