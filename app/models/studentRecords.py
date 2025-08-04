from sqlalchemy import String, Boolean, Integer
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class studentRecords(Base):
    __tablename__ = "studentRecords"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    course: Mapped[int] = mapped_column(Integer, nullable=False)
    performance: Mapped[bool] = mapped_column(Boolean, nullable=False)
    duties: Mapped[int] = mapped_column(Integer, nullable=False)
    transition: Mapped[int] = mapped_column(Integer, nullable=False)
    general_cleaning: Mapped[int] = mapped_column(Integer, nullable=False)

