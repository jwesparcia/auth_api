from fastapi import APIRouter, Depends, HTTPException, Response, status

from app.api.dependencies import get_access_token, get_current_user
from app.schemas.auth_schema import AuthRequest
from app.services.auth_service import login_user, logout_user, signup_user

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


@router.post("/logout", status_code=status.HTTP_204_NO_CONTENT)
def logout(
    token: str = Depends(get_access_token),
    _current_user=Depends(get_current_user),
):
    result = logout_user(token)

    if not result["success"]:
        raise HTTPException(
            status_code=result["status_code"],
            detail=result["message"],
        )

    return Response(status_code=status.HTTP_204_NO_CONTENT)
