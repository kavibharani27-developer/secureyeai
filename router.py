from fastapi import APIRouter

from app.api.routes import cameras, events, references, video_analysis

api_router = APIRouter()
api_router.include_router(references.router)
api_router.include_router(cameras.router)
api_router.include_router(events.router)
api_router.include_router(video_analysis.router)
from app.api.routes import evidence
api_router.include_router(evidence.router)

from app.api.routes import live_detection
api_router.include_router(live_detection.router)
