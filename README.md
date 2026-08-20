# Supabase Authentication API

FastAPI authentication service backed by Supabase Auth. It provides signup and
login, validates bearer tokens with a reusable FastAPI dependency, protects
user routes, and supports logout.

## Requirements

- Python 3.11+
- A Supabase project

## Local setup

1. Clone the repository and enter the project directory.
2. Create and activate a virtual environment:

   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. Install dependencies:

   ```powershell
   python -m pip install -r requirements.txt
   ```

4. Create `.env` from the example and fill in values from Supabase Project
   Settings > API:

   ```powershell
   Copy-Item .env.example .env
   ```

   ```dotenv
   SUPABASE_URL=https://your-project.supabase.co
   SUPABASE_KEY=your-supabase-api-key
   ```

   `.env` is ignored by Git. Never commit Supabase keys or other secrets.

## Run the API

```powershell
venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

The API is available at `http://localhost:8000`. Interactive Swagger UI is at
[`/docs`](http://localhost:8000/docs), and the generated OpenAPI document is at
[`/openapi.json`](http://localhost:8000/openapi.json).

In Swagger UI, click **Authorize**, enter a Supabase access token, and use
**Try it out** on a protected endpoint. The bearer security scheme is applied
automatically to protected operations.

## API reference

| Method | Endpoint | Auth required | Purpose |
| --- | --- | :---: | --- |
| GET | `/` | No | Health message |
| GET | `/public/info` | No | Public information |
| POST | `/auth/signup` | No | Create a Supabase user |
| POST | `/auth/login` | No | Exchange credentials for tokens |
| POST | `/auth/logout` | Yes | Revoke the authenticated session |
| GET | `/protected/profile` | Yes | Return the authenticated user profile |
| GET | `/protected/dashboard` | Yes | Return protected dashboard data |

Protected endpoints expect:

```http
Authorization: Bearer <supabase-access-token>
```

## Swagger UI screenshot

Open `/docs` locally to view the Authorize button, bearer lock icons, and the
protected routes. A screenshot can be captured from that page after starting
the server.
