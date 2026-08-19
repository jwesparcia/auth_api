from fastapi import APIRouter

router = APIRouter(
    prefix="/public",
    tags=["Public"]
)


@router.get("/info")
def get_public_info():
    return {
        "message": "Welcome stranger! This info is public."
    }