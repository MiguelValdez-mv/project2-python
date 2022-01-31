from sqlalchemy.orm import Session

from .models import Songs, Genres, MediaTypes
from .schemas import Song, SongDetails


def get_song_by_id(db: Session, song_id: int) -> Song:
    return db.query(Songs).get(song_id)


def get_details_of_a_song(db: Session, song: Song) -> SongDetails:
    genre = db.query(Genres).get(song.GenreId)
    media_type = db.query(MediaTypes).get(song.MediaTypeId)

    return {**song.__dict__, "GenreName": genre.Name, "MediaTypeName": media_type.Name}
