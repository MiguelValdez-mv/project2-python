from fastapi import APIRouter

from modules.singers.api import router as singers_router
from modules.albums.api import router as albums_router
from modules.singer.api import router as singer_router
from modules.song.api import router as song_router

router = APIRouter()

router.include_router(singers_router, prefix="/singers", tags=["Singers"])
router.include_router(albums_router, prefix="/albums", tags=["Albums"])
router.include_router(singer_router, prefix="/singer", tags=["Singer"])
router.include_router(song_router, prefix="/songs", tags=["Songs"])
