from sqlalchemy.orm import Session

from .models import Songs, Genres, Media_Types
from .schemas import Song


def get_song_by_id(db: Session, song_id: int):
    return db.query(Songs).get(song_id)


def get_details_of_a_song(db: Session, song: Song):
    genre = db.query(Genres).get(song.GenreId)
    media_type = db.query(Media_Types).get(song.MediaTypeId)

    return {**song.__dict__, "genre_name": genre.Name, "media_type_name": media_type.Name}
