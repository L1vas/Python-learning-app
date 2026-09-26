from src.database import Base, engine
from src import models


def init_database() -> None:
    """Create all database tables."""
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully.")


if __name__ == "__main__":
    init_database()