from pydantic import BaseModel


class Singer(BaseModel):
    ArtistId: int
    Name: str

    class Config:
        orm_mode = True
