#python
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .models import Base, User, Lesson, Exercise
from .data.level1_data import LEVEL1_LESSONS
from .data.level2_data import LEVEL2_LESSONS


# Project root directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Store the SQLite database in a dedicated data directory
DATA_DIR = PROJECT_ROOT / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

DATABASE_PATH = DATA_DIR / "python_coach.db"
DATABASE_URL = f"sqlite:///{DATABASE_PATH.as_posix()}"


# SQLite configuration
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)


SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


def get_db():
    """
    Provide a database session for FastAPI dependencies.
    """
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


def init_db():
    """
    Create all database tables and populate Level 1 and Level 2 data.
    """

    # Create database tables
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    try:
        # Populate Level 1 lessons
        for lesson_data in LEVEL1_LESSONS:
            lesson = Lesson(
                title=lesson_data["title"],
                content=lesson_data["content"],
            )

            db.add(lesson)
            db.flush()

            for exercise_data in lesson_data.get("exercises", []):
                exercise = Exercise(
                    lesson_id=lesson.id,
                    instructions=exercise_data.get("instructions", ""),
                    starter_code=exercise_data.get("starter_code", ""),
                    expected_output=exercise_data.get("expected_output", ""),
                )

                db.add(exercise)

        # Populate Level 2 lessons
        for lesson_data in LEVEL2_LESSONS:
            lesson = Lesson(
                title=lesson_data["title"],
                content=lesson_data["content"],
            )

            db.add(lesson)
            db.flush()

            for exercise_data in lesson_data.get("exercises", []):
                exercise = Exercise(
                    lesson_id=lesson.id,
                    instructions=exercise_data.get("instructions", ""),
                    starter_code=exercise_data.get("starter_code", ""),
                    expected_output=exercise_data.get("expected_output", ""),
                )

                db.add(exercise)

        # Save everything
        db.commit()

        print("Database initialized successfully.")
        print(f"Database location: {DATABASE_PATH}")

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


if __name__ == "__main__":
    init_db()