from fastapi import FastAPI
from app.api.routes import router as auth_router

app = FastAPI(
    title="Authentication API",
    description="API with Supabase Authentication",
    version="1.0.0"
)

app.include_router(auth_router)


@app.get("/")
def root():
    return {
        "message": "Authentication API is running"
    }