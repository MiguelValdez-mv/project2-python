from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from . import repository
from ..song.schemas import Song
from modules import albums

router = APIRouter()


@router.get(
    "/{album_id}/",
    response_model=List[Song],
    status_code=status.HTTP_200_OK
)
def get_songs_from_an_album(
    album_id: int,
    db: Session = Depends(get_db)
):
    album = repository.get_album_by_id(db, album_id)

    if album is None:
        raise HTTPException(status_code=404, detail="Non-existent album")

    return repository.get_songs_from_an_album(db, album_id)
