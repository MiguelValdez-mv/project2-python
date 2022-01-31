from typing import Optional
from pydantic import BaseModel


class Song(BaseModel):
    TrackId: int
    Name: str
    AlbumId:  int
    MediaTypeId: int
    GenreId: int
    Composer: Optional[str]
    Milliseconds: int
    Bytes: Optional[int]
    UnitPrice: float

    class Config:
        orm_mode = True


class SongDetails(Song):
    GenreName: str
    MediaTypeName: str

    class Config:
        orm_mode = True
