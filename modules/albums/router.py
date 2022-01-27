from fastapi import APIRouter

router = APIRouter()


@router.get("/{id}/")
def get_songs_from_an_album():
    pass
