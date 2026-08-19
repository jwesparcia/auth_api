from app.core.config import supabase


def signup_user(email: str, password: str):

    if not email or not password:
        return {
            "success": False,
            "status_code": 400,
            "message": "Email and password are required"
        }

    try:
        response = supabase.auth.sign_up({
            "email": email,
            "password": password
        })

        return {
            "success": True,
            "status_code": 201,
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

    if not email or not password:
        return {
            "success": False,
            "status_code": 400,
            "message": "Email and password are required"
        }

    try:
        response = supabase.auth.sign_in_with_password({
            "email": email,
            "password": password
        })

        return {
            "success": True,
            "status_code": 200,
            "data": {
                "access_token": response.session.access_token,
                "refresh_token": response.session.refresh_token
            }
        }

    except Exception:
        return {
            "success": False,
            "status_code": 401,
            "message": "Invalid login credentials"
        }