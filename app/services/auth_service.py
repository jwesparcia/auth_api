from app.core.config import supabase


def signup_user(email: str, password: str):
    try:
        response = supabase.auth.sign_up({
            "email": email,
            "password": password
        })

        return {
            "success": True,
            "data": {
                "user": response.user
            }
        }

    except Exception as e:
        return {
            "success": False,
            "status_code": 400,
            "message": str(e)
        }


def login_user(email: str, password: str):
    try:
        response = supabase.auth.sign_in_with_password({
            "email": email,
            "password": password
        })

        return {
            "success": True,
            "data": {
                "access_token": response.session.access_token,
                "refresh_token": response.session.refresh_token
            }
        }

    except Exception as e:
        print("Login error:", str(e))

        return {
            "success": False,
            "status_code": 401,
            "message": "Invalid login credentials"
        }


def verify_user_token(token: str):
    """Validate a request JWT against Supabase and return its user."""
    try:
        # Pass the request token explicitly; this must not rely on the
        # Supabase client's server-side session state.
        response = supabase.auth.get_user(jwt=token)

        if response is None or response.user is None:
            return {
                "success": False,
                "status_code": 401,
                "message": "Invalid or expired token"
            }

        return {
            "success": True,
            "user": response.user
        }

    except Exception:
        return {
            "success": False,
            "status_code": 401,
            "message": "Invalid or expired token"
        }