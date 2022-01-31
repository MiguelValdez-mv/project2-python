from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from . import repository
from .schemas import Singer
from ..albums.schemas import Album

router = APIRouter()


@router.get(
    "/",
    response_model=List[Singer],
    status_code=status.HTTP_200_OK
)
def get_singers(db: Session = Depends(get_db)) -> List[Singer]:
    return repository.get_singers(db)


@router.get(
    "/{singer_id}/",
    response_model=List[Album],
    status_code=status.HTTP_200_OK
)
def get_albums_from_a_singer(
    singer_id: int,
    db: Session = Depends(get_db)
) -> List[Album]:
    singer = repository.get_singer_by_id(db, singer_id)

    if singer is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Non-existent singer"
        )

    return repository.get_albums_from_a_singer(db, singer_id)
