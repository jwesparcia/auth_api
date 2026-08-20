from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.services.auth_service import verify_user_token


security = HTTPBearer(auto_error=False)


def get_access_token(
    credentials: HTTPAuthorizationCredentials | None = Depends(security),
) -> str:
    """Extract a bearer token from the request or reject the request."""
    if not credentials or not credentials.credentials.strip():
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"error": "Access token required"},
            headers={"WWW-Authenticate": "Bearer"},
        )

    return credentials.credentials.strip()


def get_current_user(token: str = Depends(get_access_token)):
    """Verify the request token and return the authenticated Supabase user."""
    result = verify_user_token(token)

    if not result["success"]:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"error": "Invalid or expired token"},
            headers={"WWW-Authenticate": "Bearer"},
        )

    return result["user"]
