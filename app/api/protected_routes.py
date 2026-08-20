from fastapi import APIRouter, Depends

from app.api.dependencies import get_current_user

router = APIRouter(
    prefix="/protected",
    tags=["Protected"]
)

@router.get("/profile")
def get_profile(current_user=Depends(get_current_user)):
    return {
        "id": current_user.id,
        "email": current_user.email,
        "created_at": current_user.created_at,
    }


@router.get("/dashboard")
def get_dashboard(current_user=Depends(get_current_user)):
    return {
        "message": "Welcome to your dashboard",
        "user_id": current_user.id,
    }
