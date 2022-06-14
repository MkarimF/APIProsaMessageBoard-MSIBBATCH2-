import json
from contextlib import contextmanager
from urllib import response
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
        yield


def test_create_user():
    with embedded_db():
        initial_user_data = {
            "username": "test_user",
            "email": "test_user@prosa.ai",
            "password": "test_password"
        }
        response = client.post("/user/", json=initial_user_data)
        assert response.status_code == 200
        user_data = response.json()
        assert user_data["username"] == initial_user_data["username"]
        assert user_data["email"] == initial_user_data["email"]

def test_get_id_user():
    with embedded_db():
        initial_user_data = {
            "id": 1,
            "username": "test_user",
            "email": "test@prosa.ai",
            "password": "test_password"}
        response = client.post("/user/", json=initial_user_data)
        assert response.status_code == 200
        user_exist = response.json()
        assert user_exist["username"] == initial_user_data["username"]
        assert user_exist["email"] == initial_user_data["email"]
        assert response.status_code == 200
        response2 = client.post("/login",json={"username": "test_user", "password": "test_password"})
        client.headers["authorization"] = f"Bearer {response2.json()['access_token']}"
        response3 = client.get("/user/1")
        assert response3.status_code == 200       
        user_data = response3.json()
        assert user_data["username"] == initial_user_data["username"]
        assert user_data["email"] == initial_user_data["email"]

# def test_login():
#     with embedded_db():
#         initial_user_data = {
#             "username": "test_user",
#             "email": "anton"}
#         client.authenticate(initial_user_data)
#         response = client.get("/user/", json=initial_user_data)
#         assert response.status_code == 200
        
