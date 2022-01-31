import imp
from sqlalchemy.orm import Session
from typing import List

from .models import Albums
from .schemas import Album
from ..song.models import Songs
from ..song.schemas import Song


def get_album_by_id(db: Session, album_id: int) -> Album:
    return db.query(Albums).get(album_id)


def get_songs_from_an_album(db: Session, album_id: int) -> List[Song]:
    return db.query(Songs).filter(Songs.AlbumId == album_id).all()
