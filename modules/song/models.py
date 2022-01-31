from sqlalchemy import Column, Integer, String, Numeric, ForeignKey

from database import Base


class Songs(Base):
    __tablename__ = "tracks"

    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("albums.AlbumId"))
    MediaTypeId = Column(Integer, ForeignKey("media_types.MediaTypeId"))
    GenreId = Column(Integer, ForeignKey("genres.GenreId"))
    Composer = Column(String)
    Milliseconds = Column(Integer)
    Bytes = Column(Integer)
    UnitPrice = Column(Numeric(10, 2))


class Genres(Base):
    __tablename__ = "genres"

    GenreId = Column(Integer, primary_key=True)
    Name = Column(String)


class Media_Types(Base):
    __tablename__ = "media_types"

    MediaTypeId = Column(Integer, primary_key=True)
    Name = Column(String)
