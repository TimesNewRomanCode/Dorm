from datetime import datetime
from typing import Optional

from sqlalchemy import String, Boolean, DateTime, func, int
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class studentRecords(Base):
    __tablename__ = "studentRecords"

    username: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    course: Mapped[int] = mapped_column(int, unique=False, nullable=False)
    performance: Mapped[bool] = mapped_column(Boolean, nullable=False)
    duties: Mapped[int] = mapped_column(int, unique=False, nullable=False)
    transition: Mapped[int] = mapped_column(int, unique=False, nullable=False)
    general_cleaning: Mapped[int] = mapped_column(int, unique=False, nullable=False)

