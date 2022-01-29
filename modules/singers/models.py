from sqlalchemy import Column, Integer, String

from database import Base


class Singers(Base):
    __tablename__ = "artists"

    ArtistId = Column(Integer, primary_key=True, index=True)
    Name = Column(String)
