from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from . import repository
from ..song.schemas import Song

router = APIRouter()


@router.get(
    "/{album_id}/",
    response_model=List[Song],
    status_code=status.HTTP_200_OK
)
def get_songs_from_an_album(
    album_id: int,
    db: Session = Depends(get_db)
) -> List[Song]:
    """
    Permite obtener la lista de canciones de un albúm

    Parámetros
    ----------
    album_id (int): Id del albúm
    db (Session): Sesión de la base de datos

    Retorna
    -------
    List[Song]: Lista de canciones de un albúm
    """

    album = repository.get_album_by_id(db, album_id)

    if album is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Non-existent album"
        )

    return repository.get_songs_from_an_album(db, album_id)
