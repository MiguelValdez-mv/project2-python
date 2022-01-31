from sqlalchemy.orm import Session
from typing import List

from ..singers.repository import get_albums_from_a_singer
from ..albums.repository import get_songs_from_an_album
from ..song.schemas import Song


def get_songs_from_a_singer(db: Session, singer_id: int) -> List[Song]:
    songs = []
    albums = get_albums_from_a_singer(db, singer_id)

    for album in albums:
        album_songs = get_songs_from_an_album(db, album.AlbumId)

        songs.extend(album_songs)

    return songs
