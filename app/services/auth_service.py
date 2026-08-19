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