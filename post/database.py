from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from post.config import DatabaseConfig

config = DatabaseConfig()
engine = create_engine(config.url, echo=True)

Sessionlocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()


def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()
