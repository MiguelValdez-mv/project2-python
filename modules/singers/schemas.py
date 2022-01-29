from pydantic import BaseModel
from typing import Optional


class Singer(BaseModel):
    ArtistId: int
    Name: Optional[str]

    class Config:
        orm_mode = True
