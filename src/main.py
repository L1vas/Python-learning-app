from fastapi import Depends, FastAPI, HTTPException, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session

import sqlite3

from starlette.templating import Jinja2Templates

from .database import get_db
from .models import Exercise, Lesson
from .data.level1_data import LEVEL1_LESSONS
from .data.level2_data import LEVEL2_LESSONS


app = FastAPI(title="Python Coach")

templates = Jinja2Templates(directory="src/templates")

app.mount("/static", StaticFiles(directory="src/static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/lessons/", response_model=None)
def read_lessons(db: Session = Depends(get_db)):
    lessons = db.query(Lesson).all()
    return lessons


@app.get("/lessons/{lesson_id}/exercises", response_model=None)
def read_exercises(
    lesson_id: int,
    db: Session = Depends(get_db),
):
    lesson = db.query(Lesson).filter(Lesson.id == lesson_id).first()

    if lesson is None:
        raise HTTPException(status_code=404, detail="Lesson not found")

    return lesson.exercises


@app.get("/lessons/{lesson_id}/exercises/{exercise_id}", response_class=HTMLResponse)
async def read_exercise(
    request: Request,
    lesson_id: int,
    exercise_id: int,
    db: Session = Depends(get_db),
):
    lesson = db.query(Lesson).filter(Lesson.id == lesson_id).first()
    if lesson is None:
        raise HTTPException(status_code=404, detail="Lesson not found")

    exercise = db.query(Exercise).filter(Exercise.id == exercise_id).first()
    if exercise is None:
        raise HTTPException(status_code=404, detail="Exercise not found")

    return templates.TemplateResponse("exercise.html", {"request": request, "lesson": lesson, "exercise": exercise})


@app.post("/run/", response_model=None)
async def run_code(request: Request, code: str = Form(...)):
    try:
        # For security reasons, we'll use Pyodide for execution
        import pyodide
        await pyodide.loadPackage('micropip')
        output = pyodide.runPython(code)
        return {"output": output}
    except Exception as e:
        return {"error": str(e)}


@app.post("/tutor/", response_model=None)
async def tutor_endpoint(request: Request, code: str = Form(...)):
    # For now, we'll just echo the code back
    # Later, integrate with Ollama and qwen2.5:14b
    return {"feedback": f"Your code: {code}"}


# Initialize database
@app.on_event("startup")
async def startup():
    db = next(get_db())
    try:
        populate_level1(db)
        populate_level2(db)
    finally:
        db.close()


def add_or_update_lesson(db: Session, title: str, content: str) -> Lesson:
    """Create a lesson if it does not exist, otherwise update its content."""
    lesson = db.query(Lesson).filter(Lesson.title == title).first()

    if lesson is None:
        lesson = Lesson(title=title, content=content)
        db.add(lesson)
    else:
        lesson.content = content

    return lesson


def populate_level1(db: Session) -> None:
    """Create or update all Level 1 lessons without creating duplicates."""
    for lesson_data in LEVEL1_LESSONS:
        add_or_update_lesson(
            db,
            lesson_data["title"],
            lesson_data["content"],
        )

    db.commit()


def populate_level2(db: Session) -> None:
    """Create or update all Level 2 lessons without creating duplicates."""
    for lesson_data in LEVEL2_LESSONS:
        add_or_update_lesson(
            db,
            lesson_data["title"],
            lesson_data["content"],
        )

    db.commit()

