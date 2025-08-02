from fastapi import APIRouter, Depends, Cookie, Query
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_session
# from app.schemas.auth import (
#     RegistrationScheme,
#     LoginScheme,
#     UserDtoScheme,
#     SuccessResponse,
# )
# from app.services.auth import AuthService

router = APIRouter(prefix="/studentRecords", tags=["studentRecords"])