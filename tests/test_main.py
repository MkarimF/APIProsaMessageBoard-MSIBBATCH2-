from contextlib import contextmanager
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from unittest.mock import patch
from sqlalchemy.pool import StaticPool

from post.database import Base
from post.main import app


client = TestClient(app)


@contextmanager
def embedded_db():
    engine = create_engine(
        "sqlite://",
        # echo=True,
        connect_args={'check_same_thread': False},
        poolclass=StaticPool
    )

    Sessionlocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

    with patch("post.database.Sessionlocal", Sessionlocal):
        Base.metadata.create_all(engine)
        yield engine