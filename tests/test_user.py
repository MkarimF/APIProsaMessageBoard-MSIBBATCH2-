# def test_create_user(client, embedded_db):
#     initial_user_data = {
#         "username": "test_user",
#         "email": "test_user@prosa.ai",
#         "password": "test_password"
#     }

#     # create user
#     response = client.post("/user/", json=initial_user_data)
#     assert response.status_code == 200
#     # assert user data
#     user_data = response.json()
#     assert user_data["username"] == initial_user_data["username"]
#     assert user_data["email"] == initial_user_data["email"]


# def test_get_id_user(client, embedded_db):
#     initial_user_data = {
#         "id": 1,
#         "username": "test_user",
#         "email": "test@prosa.ai",
#         "password": "test_password"}
#     # create user
#     response = client.post("/user/", json=initial_user_data)
#     assert response.status_code == 200
#     user_data1 = response.json()
#     assert user_data1["username"] == initial_user_data["username"]
#     assert user_data1["email"] == initial_user_data["email"]
#     assert response.status_code == 200
#     # login user
#     response2 = client.post("/login", json={"username": "test_user", "password": "test_password"})
#     # auth user
#     client.headers["authorization"] = f"Bearer {response2.json()['access_token']}"
#     # get user by id
#     response3 = client.get("/user/1")
#     assert response3.status_code == 200
#     # assert user_data
#     user_data = response3.json()
#     assert user_data["username"] == initial_user_data["username"]
#     assert user_data["email"] == initial_user_data["email"]


# def test_get_all_users(client, embedded_db):
#     initial_user_data1 = {
#         "id": 1,
#         "username": "test_user1",
#         "email": "email1",
#         "password": "test_password1",
#     }
#     initial_user_data2 = {
#         "id": 2,
#         "username": "test_user2",
#         "email": "email2",
#         "password": "test_password2"}

#     # create user 1
#     response = client.post("/user/", json=initial_user_data1)
#     assert response.status_code == 200
#     # create user 2
#     response2 = client.post("/user/", json=initial_user_data2)
#     assert response2.status_code == 200
#     user_data1 = response.json()
#     assert user_data1["username"] == initial_user_data1["username"]
#     assert user_data1["email"] == initial_user_data1["email"]
#     assert response.status_code == 200
#     # login user
#     response3 = client.post("/login", json={"username": "test_user1", "password": "test_password1"})
#     assert response3.status_code == 200
#     # auth user
#     client.headers["authorization"] = f"Bearer {response3.json()['access_token']}"
#     assert response3.status_code == 200
#     # show user
#     response4 = client.get("/user/")
#     assert response4.status_code == 200
#     # assert user data
#     user_data = response4.json()
#     assert user_data[0]["username"] == initial_user_data1["username"]
#     assert user_data[0]["email"] == initial_user_data1["email"]
#     assert user_data[1]["username"] == initial_user_data2["username"]
#     assert user_data[1]["email"] == initial_user_data2["email"]
#     assert response4.status_code == 200
