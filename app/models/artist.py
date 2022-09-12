from sqlalchemy import SmallInteger, String
from sqlalchemy import ForeignKey, Column, Index, text
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import ARRAY

from app.db.base_class import Base


class Artists(Base):

    __tablename__ = "artists"

    __table_args__ = (
        Index(
            "artist_search_index",
            "artist_name",
            postgresql_ops={"artist_name": "gin_trgm_ops"},
            postgresql_using="gin",
        ),
    )

    id = Column("artist_id", String, primary_key=True)
    name = Column("artist_name", String, nullable=False)
    artist_genres = Column("artist_genres", ARRAY(String))
    popularity = Column("artist_popularity", SmallInteger)
    image = Column("artist_image", String)
    banner = Column("artist_banner", String, nullable=True)
