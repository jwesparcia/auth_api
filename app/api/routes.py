from fastapi import APIRouter, HTTPException, status
from app.schemas.auth_schema import AuthRequest
from app.services.auth_service import signup_user, login_user

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post(
    "/signup",
    status_code=status.HTTP_201_CREATED
)
def signup(data: AuthRequest):

    result = signup_user(
        data.email,
        data.password
    )

    if not result["success"]:
        raise HTTPException(
            status_code=result["status_code"],
            detail=result["message"]
        )

    return result["data"]


@router.post("/login")
def login(data: AuthRequest):

    result = login_user(
        data.email,
        data.password
    )

    if not result["success"]:
        raise HTTPException(
            status_code=result["status_code"],
            detail=result["message"]
        )

    return result["data"]