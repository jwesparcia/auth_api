from fastapi import APIRouter, Header, HTTPException, status

router = APIRouter(
    prefix="/protected",
    tags=["Protected"]
)


@router.get("/profile")
def get_profile(authorization: str = Header(None)):

    # Check if Authorization header exists
    if not authorization:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={
                "error": "Access token required"
            }
        )

    # Check Bearer format
    if not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={
                "error": "Access token required"
            }
        )

    # Extract the token
    token = authorization.replace("Bearer ", "", 1)

    # Check if token is empty
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={
                "error": "Access token required"
            }
        )

    # Stage 2: Token is extracted but NOT verified yet
    return {
        "message": "Access granted to protected profile",
        "token_received": True
    }