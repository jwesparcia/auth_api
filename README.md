# Authentication API

## Swagger UI

Start the API and open [Swagger UI](http://localhost:8000/docs):

```powershell
venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

The protected routes use FastAPI's `HTTPBearer` security scheme. Select
**Authorize**, enter `Bearer <your JWT>` (or just the token, depending on the
Swagger UI prompt), and use **Try it out** on:

- `GET /protected/profile`
- `GET /protected/dashboard`
- `POST /auth/logout`

FastAPI exposes the corresponding OpenAPI schema at `/openapi.json`.
