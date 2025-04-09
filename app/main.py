from contextlib import asynccontextmanager
from fastapi import FastAPI
from .models.base import Base
from .database import engine
from .middleware.ErrorHandlerMiddleware import ErrorHandlerMiddleware
from .routers import character
from .utils.seed_db import seed_db_if_needed

# Create all tables in the database
Base.metadata.create_all(bind=engine)

# Define the lifespan context manager
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: seed the database
    yield
    # Shutdown: clean up resources if needed

# Setup Server
app = FastAPI()

# Setup Middleware
app.add_middleware(ErrorHandlerMiddleware)

# Setup Routers
app.include_router(character.router)

# Seed the DB if needed.
seed_db_if_needed()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)