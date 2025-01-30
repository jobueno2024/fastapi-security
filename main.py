from fastapi import FastAPI
from routers import httpbasic

app = FastAPI()

app.include_router(httpbasic.router, prefix="/httpbasic", tags=["security"])

@app.get("/")
async def root():
    return {"message": "Welcome to the API"}
