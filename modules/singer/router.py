from fastapi import APIRouter

router = APIRouter()


@router.get("/{id}/")
def get_songs_from_a_singer():
    pass
