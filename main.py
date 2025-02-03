from fastapi import FastAPI
from routers import httpbasic, apikeyheader

app = FastAPI()

app.include_router(httpbasic.router, prefix="/httpbasic", tags=["security"])
app.include_router(apikeyheader.router, prefix="/apikeyheader", tags=["security"])

@app.get("/")
async def root():
    return {"message": "Welcome to the API"}
