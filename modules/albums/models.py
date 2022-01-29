from sqlalchemy import Column, Integer, String, ForeignKey

from database import Base


class Albums(Base):
    __tablename__ = "albums"

    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey("artists.ArtistId"))
