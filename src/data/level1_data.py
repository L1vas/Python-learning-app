from sqlalchemy.orm import Session
from src.database import get_db
from src.models import Lesson, Exercise, Quiz, Question

def populate_level1(db: Session):
    # Lesson 1: What Programming Is
    lesson1 = Lesson(title='Introduction to Programming', content='')
    db.add(lesson1)
    db.commit()
    db.refresh(lesson1)

    # Lesson 2: What Python Is
    lesson2 = Lesson(title='Introduction to Python', content='')
    db.add(lesson2)
    db.commit()
    db.refresh(lesson2)

    # Lesson 3: How Programs Work
    lesson3 = Lesson(title='Understanding Program Flow', content='')
    db.add(lesson3)
    db.commit()
    db.refresh(lesson3)

    # Lesson 4: Your First Python Program
    lesson4 = Lesson(title='Writing Your First Python Program', content='')
    db.add(lesson4)
    db.commit()
    db.refresh(lesson4)

    # Lesson 5: print()
    lesson5 = Lesson(title='Using the `print()` Function', content='')
    db.add(lesson5)
    db.commit()
    db.refresh(lesson5)

    # Lesson 6: Comments
    lesson6 = Lesson(title='Adding Comments to Your Code', content='')
    db.add(lesson6)
    db.commit()
    db.refresh(lesson6)

    # Lesson 7: Strings
    lesson7 = Lesson(title='Working with Strings', content='')
    db.add(lesson7)
    db.commit()
    db.refresh(lesson7)

    # Lesson 8: Numbers
    lesson8 = Lesson(title='Working with Numbers', content='')
    db.add(lesson8)
    db.commit()
    db.refresh(lesson8)

    # Lesson 9: Variables
    lesson9 = Lesson(title='Using Variables', content='')
    db.add(lesson9)
    db.commit()
    db.refresh(lesson9)

    # Lesson 10: Assigning Values
    lesson10 = Lesson(title='Assigning Values to Variables', content='')
    db.add(lesson10)
    db.commit()
    db.refresh(lesson10)

    # Lesson 11: Arithmetic
    lesson11 = Lesson(title='Performing Arithmetic Operations', content='')
    db.add(lesson11)
    db.commit()
    db.refresh(lesson11)