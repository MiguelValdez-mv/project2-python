from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from . import repository
from ..singers.repository import get_singer_by_id
from ..song.schemas import Song

router = APIRouter()


@router.get(
    "/{singer_id}/",
    response_model=List[Song],
    status_code=status.HTTP_200_OK
)
def get_songs_from_a_singer(
    singer_id: int,
    db: Session = Depends(get_db)
) -> List[Song]:
    """
    Permite obtener la lista de canciones de un cantante

    Parámetros
    ----------
    singer_id (int): Id del cantante
    db (Session): Sesión de la base de datos

    Retorna
    -------
    List[Song]: Lista de canciones del cantante
    """

    singer = get_singer_by_id(db, singer_id)

    if singer is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Non-existent singer"
        )

    return repository.get_songs_from_a_singer(db, singer_id)
