from sqlalchemy.orm import Session
from typing import List

from .models import Singers
from .schemas import Singer
from ..albums.models import Albums
from ..albums.schemas import Album


def get_singers(db: Session) -> List[Singer]:
    """
    Permite obtener la lista total de cantantes registrados

    Parámetros
    ----------
    db (Session): Sesión de la base de datos

    Retorna
    -------
    List[Singer]: Lista de cantantes
    """

    return db.query(Singers).all()


def get_singer_by_id(db: Session, singer_id: int) -> Singer:
    """
    Permite obtener un cantante usando el id del mismo

    Parámetros
    ----------
    db (Session): Sesión de la base de datos
    singer_id (int): Id del cantante

    Retorna
    -------
    Singer: Cantante almacenado en la base de datos
    """

    return db.query(Singers).get(singer_id)


def get_albums_from_a_singer(db: Session, singer_id: int) -> List[Album]:
    """
    Permite obtener la lista de albunes de un cantante

    Parámetros
    ----------
    db (Session): Sesión de la base de datos
    singer_id (int): Id del cantante

    Retorna
    -------
    List[Album]: Lista de albunes del cantante
    """

    return db.query(Albums).filter(Albums.ArtistId == singer_id).all()
