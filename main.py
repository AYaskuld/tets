import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.routes.user_routes import router as user_router
from src.database.client import init_db
from src.config.server import Server_Config

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

app = FastAPI(title="FastAPI Users API", lifespan=lifespan)

app.include_router(user_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=int(Server_Config.SERVER_PORT), reload=True)
