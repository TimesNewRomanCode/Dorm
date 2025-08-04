from fastapi import APIRouter

router = APIRouter(prefix="/studentRecords", tags=["studentRecords"])

@router.get("/")
def hello_world():
    return {"message": "Hello World"}