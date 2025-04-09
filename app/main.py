from fastapi import FastAPI
from .models.base import Base
from .database import engine
from .middleware import error_handler
from .routers import character

Base.metadata.create_all(bind=engine)

# Setup Server
app = FastAPI()

# Setup Middleware
app.add_middleware(error_handler)

# Setup Routers
app.include_router(character.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)