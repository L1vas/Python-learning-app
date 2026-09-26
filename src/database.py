from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


# Project root directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Store the SQLite database in a dedicated data directory
DATA_DIR = PROJECT_ROOT / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

DATABASE_PATH = DATA_DIR / "python_coach.db"
DATABASE_URL = f"sqlite:///{DATABASE_PATH.as_posix()}"

# SQLite configuration for FastAPI
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base = declarative_base()


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
    Create all database tables.
    """
    Base.metadata.create_all(bind=engine)