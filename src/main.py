


from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session



from .database import get_db
from .models import Lesson, Exercise
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount('/static', StaticFiles(directory='src/static'), name='static')































@app.get('/lessons/', response_model=list[Lesson])
def read_lessons(db: Session = Depends(get_db)):
    lessons = db.query(Lesson).all()
    return lessons

@app.get('/lessons/{lesson_id}/exercises', response_model=list[Exercise])
def read_exercises(lesson_id: int, db: Session = Depends(get_db)):
    lesson = db.query(Lesson).filter(Lesson.id == lesson_id).first()
    if lesson is None:
        raise HTTPException(status_code=404, detail='Lesson not found')
    return lesson.exercises
