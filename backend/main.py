from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine
from . import models
from .routers import users, claims

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="SkillGraph API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(claims.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to SkillGraph API"}

@app.get("/health")
def health_check():
    return {"status": "ok"}
