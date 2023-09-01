# Standard Library
from typing import Generator, Optional

# External
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

# Project
from app.config import LOGGER
from app.config.config import (
    DATABASE_PORT,
    POSTGRES_DB,
    POSTGRES_HOSTNAME,
    POSTGRES_PASSWORD,
    POSTGRES_USER,
)


SQLALCHEMY_DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOSTNAME}:{DATABASE_PORT}/{POSTGRES_DB}"


engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db() -> Generator[Session, None, None]:
    db: Optional[Session] = None
    try:
        db = SessionLocal()
        LOGGER.info("Database session opened.")
        yield db
    except SQLAlchemyError as e:
        LOGGER.error(f"An error occurred: {e}")
    finally:
        if db is not None:
            db.close()
            LOGGER.info("Database session closed.")
