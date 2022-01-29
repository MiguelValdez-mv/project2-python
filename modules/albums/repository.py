import imp
from sqlalchemy.orm import Session

from .models import Albums
from ..song.models import Songs


def get_album_by_id(db: Session, album_id: int):
    return db.query(Albums).get(album_id)


def get_songs_from_an_album(db: Session, album_id: int):
    return db.query(Songs).filter(Songs.AlbumId == album_id).all()
