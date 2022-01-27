from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_singers():
    pass


@router.get("/{id}/")
def get_albums_from_a_singer():
    pass
