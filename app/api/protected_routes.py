from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.responses import JSONResponse
from app.services.auth_service import verify_user_token

router = APIRouter(
    prefix="/protected",
    tags=["Protected"]
)

security = HTTPBearer(auto_error=False)


@router.get("/profile")
def get_profile(
    credentials: HTTPAuthorizationCredentials | None = Depends(security)
):
    if not credentials or not credentials.credentials:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"error": "Access token required"}
        )

    token = credentials.credentials.strip()

    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"error": "Access token required"}
        )

    # Verify token
    result = verify_user_token(token)

    if not result["success"]:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"error": "Invalid or expired token"}
        )

    user = result["user"]

    return {
        "id": user.id,
        "email": user.email,
        "created_at": user.created_at
    }
