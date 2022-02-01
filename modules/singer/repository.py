from sqlalchemy.orm import Session
from typing import List

from ..singers.repository import get_albums_from_a_singer
from ..albums.repository import get_songs_from_an_album
from ..song.schemas import Song


def get_songs_from_a_singer(db: Session, singer_id: int) -> List[Song]:
    """
    Permite obtener la lista de canciones de un cantante

    Parámetros
    ----------
    db (Session): Sesión de la base de datos
    singer_id (int): Id del cantante

    Retorna
    -------
    List[Song]: Lista de canciones del cantante
    """

    songs = []
    albums = get_albums_from_a_singer(db, singer_id)

    for album in albums:
        album_songs = get_songs_from_an_album(db, album.AlbumId)

        songs.extend(album_songs)

    return songs
