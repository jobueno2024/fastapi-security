from fastapi import FastAPI
from routers import httpbasic, apikeyheader, http_authorization_credentials

app = FastAPI()

app.include_router(httpbasic.router, prefix="/httpbasic", tags=["security"])
app.include_router(apikeyheader.router, prefix="/apikeyheader", tags=["security"])
app.include_router(http_authorization_credentials.router, prefix="/http_auth_credentials", tags=["security"])

@app.get("/")
async def root():
    return {"message": "Welcome to the API"}
