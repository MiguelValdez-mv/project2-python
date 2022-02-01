import imp
from sqlalchemy.orm import Session
from typing import List

from .models import Albums
from .schemas import Album
from ..song.models import Songs
from ..song.schemas import Song


def get_album_by_id(db: Session, album_id: int) -> Album:
    """
    Permite obtener un albúm usando el id del mismo

    Parámetros
    ----------
    db (Session): Sesión de la base de datos
    album_id (int): Id del albúm

    Retorna
    -------
    Album: Album almacenado en la base de datos
    """

    return db.query(Albums).get(album_id)


def get_songs_from_an_album(db: Session, album_id: int) -> List[Song]:
    """
    Permite obtener la lista de canciones de un albúm

    Parámetros
    ----------
    db (Session): Sesión de la base de datos
    album_id (int): Id del albúm

    Retorna
    -------
    List[Song]: Lista de canciones de un albúm
    """

    return db.query(Songs).filter(Songs.AlbumId == album_id).all()
