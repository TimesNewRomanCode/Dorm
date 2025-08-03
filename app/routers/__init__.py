from fastapi import APIRouter
from .studentRecords import router as studentRecords_router



router = APIRouter(prefix="/api")

router.include_router(studentRecords_router)

