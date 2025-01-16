from fastapi import FastAPI
from routers import users, items, security1

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(items.router, prefix="/items", tags=["items"])
app.include_router(security1.router, prefix="/security1", tags=["users"])

@app.get("/")
async def root():
    return {"message": "Welcome to the API"}
