from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
import sqlite3

app = FastAPI()

# Database connection function
def get_db():
    conn = sqlite3.connect('data/python_coach.db')
    try:
        yield conn
    finally:
        conn.close()

# User models and endpoints
class User(BaseModel):
    username: str
    password: str

@app.post("/register")
async def register(user: User, db: sqlite3.Connection = Depends(get_db)):
    cursor = db.cursor()
    # Hash the password (for demonstration purposes, use a simple hash function)
    password_hash = user.password  # TODO: Implement proper hashing
    cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (user.username, password_hash))
    db.commit()
    return {"message": "User registered successfully"}

@app.post("/login")
async def login(user: User, db: sqlite3.Connection = Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE username=?", (user.username,))
    user_db = cursor.fetchone()
    if not user_db or user_db[2] != user.password:  # TODO: Implement proper password verification
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    return {"message": "Login successful"}

# Lesson models and endpoints
class Lesson(BaseModel):
    title: str
    content: str

@app.get("/lessons/{lesson_id}")
async def get_lesson(lesson_id: int, db: sqlite3.Connection = Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM lessons WHERE id=?", (lesson_id,))
    lesson = cursor.fetchone()
    if not lesson:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Lesson not found")
    return {"id": lesson[0], "title": lesson[1], "content": lesson[2]}

@app.get("/lessons/")
async def list_lessons(db: sqlite3.Connection = Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM lessons")
    lessons = cursor.fetchall()
    return [{"id": lesson[0], "title": lesson[1]} for lesson in lessons]

# Run the database initialization script
if __name__ == "__main__":
    import init_db
