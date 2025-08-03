from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, validator


class StudentRecordBase(BaseModel):
    username: str
    course: int
    performance: bool
    duties: int
    transition: int
    general_cleaning: int

    class Config:
        from_attributes = True


class StudentRecordCreate(StudentRecordBase):
    @validator('course')
    def validate_course(cls, v):
        if v < 1 or v > 4:
            raise ValueError('Course must be between 1 and 4')
        return v

    @validator('duties', 'transition', 'general_cleaning')
    def validate_scores(cls, v):
        if v < 0 or v > 4:
            raise ValueError('Scores must be between 0 and 4')
        return v


class StudentRecordUpdate(BaseModel):
    username: Optional[str] = None
    course: Optional[int] = None
    performance: Optional[bool] = None
    duties: Optional[int] = None
    transition: Optional[int] = None
    general_cleaning: Optional[int] = None

    @validator('course', pre=True, always=True)
    def validate_course(cls, v):
        if v is not None and (v < 1 or v > 4):
            raise ValueError('Course must be between 1 and 4')
        return v

    @validator('duties', 'transition', 'general_cleaning', pre=True, always=True)
    def validate_scores(cls, v):
        if v is not None and (v < 0 or v > 4):
            raise ValueError('Scores must be between 0 and 4')
        return v


class StudentRecord(StudentRecordBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True