from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from .database import Base, engine, get_db
from .models import Lesson


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create all database tables when the application starts.
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title="Python Coach",
    description="A web application for learning Python.",
    version="1.0.0",
    lifespan=lifespan,
)


@app.get("/")
def root():
    return {
        "message": "Welcome to Python Coach!",
        "status": "running",
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/lessons/")
def get_lessons(db: Session = Depends(get_db)):
    lessons = db.query(Lesson).all()

    return [
        {
            "id": lesson.id,
            "title": lesson.title,
            "content": lesson.content,
        }
        for lesson in lessons
    ]