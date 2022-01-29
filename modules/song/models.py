from sqlalchemy import Column, Integer, String, Numeric

from database import Base


class Songs(Base):
    __tablename__ = "tracks"

    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer)
    MediaTypeId = Column(Integer)
    GenreId = Column(Integer)
    Composer = Column(String)
    Milliseconds = Column(Integer)
    Bytes = Column(Integer)
    UnitPrice = Column(Numeric(10, 2))
