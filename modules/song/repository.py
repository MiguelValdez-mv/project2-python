from sqlalchemy.orm import Session

from .models import Songs, Genres, MediaTypes
from .schemas import Song, SongDetails


def get_song_by_id(db: Session, song_id: int) -> Song:
    """
    Permite obtener una cancion usando el id del mismo

    Parámetros
    ----------
    db (Session): Sesión de la base de datos
    song_id (int): Id de la canción

    Retorna
    -------
    Song: Canción almacenada en la base de datos
    """

    return db.query(Songs).get(song_id)


def get_details_of_a_song(db: Session, song: Song) -> SongDetails:
    """
    Permite obtener los detalles de una canción (todos los campos
    de su tabla junto con el género y el tipo de media)

    Parámetros
    ----------
    db (Session): Sesión de la base de datos
    song_id (int): Id de la canción

    Retorna
    -------
    SongDetails: Detalles de la canción
    """

    genre = db.query(Genres).get(song.GenreId)
    media_type = db.query(MediaTypes).get(song.MediaTypeId)

    return {**song.__dict__, "GenreName": genre.Name, "MediaTypeName": media_type.Name}
