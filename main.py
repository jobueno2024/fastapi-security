from fastapi import FastAPI
from routers import httpbasic, security1

app = FastAPI()

app.include_router(httpbasic.router, prefix="/httpbasic", tags=["security"])
# app.include_router(security1.router, prefix="/security1", tags=["security"])

@app.get("/")
async def root():
    return {"message": "Welcome to the API"}
