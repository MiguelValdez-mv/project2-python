from sqlalchemy.orm import Session
from typing import List

from .models import Singers
from .schemas import Singer
from ..albums.models import Albums
from ..albums.schemas import Album


def get_singers(db: Session) -> List[Singer]:
    return db.query(Singers).all()


def get_singer_by_id(db: Session, singer_id: int) -> Singer:
    return db.query(Singers).get(singer_id)


def get_albums_from_a_singer(db: Session, singer_id: int) -> List[Album]:
    return db.query(Albums).filter(Albums.ArtistId == singer_id).all()
