from fastapi import APIRouter

from . import category, strategy
from . import org
from . import user

api_v1_router = APIRouter()
# api_v1_router.include_router(category.router, prefix="/category", tags=["category"])
# api_v1_router.include_router(org.router, prefix="/org", tags=["org"])
api_v1_router.include_router(strategy.router, prefix="/strategy", tags=["strategy"])
