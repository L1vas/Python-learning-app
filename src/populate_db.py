from sqlalchemy.orm import Session

from .database import engine, get_db
from .models import Exercise, Lesson


def populate_database(db: Session) -> None:
    # Create the tables defined by the SQLAlchemy models.
    # Using the model metadata directly ensures Lesson and Exercise
    # are registered before create_all() runs.
    Lesson.metadata.create_all(bind=engine)

    # Check whether the database already contains lessons.
    existing_lesson = db.query(Lesson).first()

    if existing_lesson is not None:
        print("Database already contains lesson data.")
        print("Nothing to populate.")
        return

    # Create lessons first so their database IDs are generated.
    lesson1 = Lesson(
        title="Introduction to Python",
        content="Learn the basics of Python programming.",
    )

    lesson2 = Lesson(
        title="Variables and Data Types",
        content="Understand variables and different data types in Python.",
    )

    db.add_all([lesson1, lesson2])
    db.flush()

    # Now create exercises using the valid lesson IDs.
    exercise1_1 = Exercise(
        lesson_id=lesson1.id,
        instructions='Write a "Hello, World!" program.',
        starter_code='print("Hello, World!")',
        expected_output="Hello, World!",
    )

    exercise1_2 = Exercise(
        lesson_id=lesson1.id,
        instructions="Print your name to the console.",
        starter_code='print("Your Name")',
        expected_output="Your Name",
    )

    exercise2_1 = Exercise(
        lesson_id=lesson2.id,
        instructions="Create a variable `x` with the value 5.",
        starter_code="x = 5\nprint(x)",
        expected_output="5",
    )

    exercise2_2 = Exercise(
        lesson_id=lesson2.id,
        instructions="Create a string variable `name` with your name.",
        starter_code='name = "Your Name"\nprint(name)',
        expected_output="Your Name",
    )

    db.add_all(
        [
            exercise1_1,
            exercise1_2,
            exercise2_1,
            exercise2_2,
        ]
    )

    db.commit()

    print("Database populated successfully.")
    print("Created 2 lessons and 4 exercises.")


if __name__ == "__main__":
    db = next(get_db())

    try:
        populate_database(db)
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()