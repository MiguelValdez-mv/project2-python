from fastapi import APIRouter

router = APIRouter()


@router.get("/{id}/")
def get_details_of_a_song():
    pass
