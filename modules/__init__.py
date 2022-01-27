from fastapi import APIRouter

from modules.singers.router import router as singers_router
from modules.albums.router import router as albums_router
from modules.singer.router import router as singer_router
from modules.song.router import router as song_router

router = APIRouter()

router.include_router(singers_router, prefix="/singers", tags=["Singers"])
router.include_router(albums_router, prefix="/albums", tags=["Albums"])
router.include_router(singer_router, prefix="/singer", tags=["Singer"])
router.include_router(song_router, prefix="/songs", tags=["Songs"])
