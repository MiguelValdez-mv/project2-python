from sqlalchemy.orm import Session

from .models import Singers
from ..albums.models import Albums


def get_singers(db: Session):
    return db.query(Singers).all()


def get_singer_by_id(db: Session, id_singer: int):
    return db.query(Singers).get(id_singer)


def get_albums_from_a_singer(db: Session, id_singer: int):
    return db.query(Albums).filter(Albums.ArtistId == id_singer).all()
