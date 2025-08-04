from fastapi import FastAPI
from routers import router 

app = FastAPI(title="Dorm")
app.include_router(router)