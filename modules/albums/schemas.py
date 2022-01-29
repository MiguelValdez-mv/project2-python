from pydantic import BaseModel


class Album(BaseModel):
    AlbumId: int
    Title: str
    ArtistId: int

    class Config:
        orm_mode = True
