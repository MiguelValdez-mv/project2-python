from pydantic import BaseModel


class Song(BaseModel):
    TrackId: int
    Name: str
    AlbumId:  int
    MediaTypeId: int
    GenreId: int
    Composer: str
    Milliseconds: int
    Bytes: int
    UnitPrice: float

    class Config:
        orm_mode = True
