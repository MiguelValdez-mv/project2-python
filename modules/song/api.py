from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from . import repository

router = APIRouter()


@router.get("/{song_id}/")
def get_details_of_a_song(
    song_id: int,
    db: Session = Depends(get_db)
):
    song = repository.get_song_by_id(db, song_id)

    if song is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Non-existent song"
        )

    return repository.get_details_of_a_song(db, song)
