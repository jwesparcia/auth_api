from fastapi import FastAPI

from app.api.routes import router as auth_router
from app.api.public_routes import router as public_router
from app.api.protected_routes import router as protected_router


app = FastAPI(
    title="Authentication API",
    description="API with Supabase Authentication",
    version="1.0.0"
)


app.include_router(auth_router)
app.include_router(public_router)
app.include_router(protected_router)


@app.on_event("startup")
async def startup_event():
    print("Server running and connected to Supabase")


@app.get("/")
def root():
    return {
        "message": "Authentication API is running"
    }