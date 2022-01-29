from sqlalchemy.orm import Session

from .models import Singers
from ..albums.models import Albums


def get_singers(db: Session):
    return db.query(Singers).all()


def get_singer_by_id(db: Session, singer_id: int):
    return db.query(Singers).get(singer_id)


def get_albums_from_a_singer(db: Session, singer_id: int):
    return db.query(Albums).filter(Albums.ArtistId == singer_id).all()
