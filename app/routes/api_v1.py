from fastapi import APIRouter
from app.routes import users, experts
from app.routes.upload import router as upload_router

api_router = APIRouter()
#health check
@api_router.get("/health")
async def health_check():
    return {"status": "healthy"}


# Register each sub-router with a prefix and tag
api_router.include_router(users.router, prefix="/users", tags=["Users"])
api_router.include_router(experts.router, prefix="/experts", tags=["Experts"])
api_router.include_router(upload_router, prefix="/upload", tags=["Upload"])

