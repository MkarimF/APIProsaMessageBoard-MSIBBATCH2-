from .test_main import embedded_db, client

def test_post_create():
    with embedded_db():
        initial_user_data1 = {
            "id": 1,
            "username": "test_user1",
            "email": "test_email1",
            "password": "test_password1"}
        initial_user_data2 = {
            "id": 2,
            "username": "test_user2",
            "email": "test_email2",
            "password": "test_password2"}
        initial_post_user_data1={
            "id": 1,
            "user_id": 1,
            "title": "test_title1",
            "text": "test_text1"}
        initial_post_user_data2={
            "id": 2,
            "user_id": 2,
            "title": "test_title2",
            "text": "test_text2"}
        response = client.post("/user/", json=initial_user_data1)
        assert response.status_code == 200
        response2 = client.post("/user/", json=initial_user_data2)
        assert response2.status_code == 200
        user_exist = response.json()
        assert user_exist["username"] == initial_user_data1["username"]
        assert user_exist["email"] == initial_user_data1["email"]
        assert response.status_code == 200
        response3 = client.post("/login",json={"username": "test_user1", "password": "test_password1"})
        assert response3.status_code ==200 
        client.headers["authorization"] = f"Bearer {response3.json()['access_token']}"
        assert response3.status_code == 200
        response4= client.post("/post/",json=initial_post_user_data1)
        assert response4.status_code == 200
        response5= client.post("/post/",json=initial_post_user_data2)
        assert response5.status_code == 200
        user_data_post1 = response4.json()
        assert user_data_post1["title"] == initial_post_user_data1["title"]
        assert user_data_post1["text"] == initial_post_user_data1["text"]
        assert response4.status_code == 200
        user_data_post2 = response5.json()
        assert user_data_post2["title"] == initial_post_user_data2["title"]
        assert user_data_post2["text"] == initial_post_user_data2["text"]
        # assert response5.status_code == 200
        
def get_all_posts():
    with embedded_db():
        initial_user_data1 = {
            "id": 1,
            "username": "test_user1",
            "email": "test_email1",
            "password": "test_password1"}
        initial_user_data2 = {
            "id": 2,
            "username": "test_user2",
            "email": "test_email2",
            "password": "test_password2"}
        initial_post_user_data1={
            "id": 1,
            "user_id": 1,
            "title": "test_title1",
            "text": "test_text1"}
        initial_post_user_data2={
            "id": 2,
            "user_id": 1,
            "title": "test_title2",
            "text": "test_text2"}
        response = client.post("/user/", json=initial_user_data1)
        assert response.status_code == 200
        response2 = client.post("/user/", json=initial_user_data2)
        assert response2.status_code == 200
        user_exist = response.json()
        assert user_exist["username"] == initial_user_data1["username"]
        assert user_exist["email"] == initial_user_data1["email"]
        assert response.status_code == 200
        response3 = client.post("/login",json={"username": "test_user1", "password": "test_password1"})
        assert response3.status_code ==200 
        client.headers["authorization"] = f"Bearer {response3.json()['access_token']}"
        response4= client.post("/post/",json=initial_post_user_data1)
        assert response4.status_code == 200
        response5= client.post("/post/",json=initial_post_user_data2)
        assert response5.status_code == 200
        response6 = client.get("/post/")
        assert response6.status_code == 200
        assert response6.json()[0]["title"] == initial_post_user_data1["title"]
        assert response6.json()[0]["text"] == initial_post_user_data1["text"]
        assert response6.json()[1]["title"] == initial_post_user_data2["title"]
        assert response6.json()[1]["text"] == initial_post_user_data2["text"]
        assert response6.status_code == 200
        
def get_post_by_id():
    with embedded_db():
        initial_user_data1 = {
            "id": 1,
            "username": "test_user1",
            "email": "test_email1",
            "password": "test_password1"}
        initial_user_data2 = {
            "id": 2,
            "username": "test_user2",
            "email": "test_email2",
            "password": "test_password2"}
        initial_post_user_data1={
            "id": 1,
            "user_id": 1,
            "title": "test_title1",
            "text": "test_text1"}
        initial_post_user_data2={
            "id": 2,
            "user_id": 1,
            "title": "test_title2",
            "text": "test_text2"}
        response = client.post("/user/", json=initial_user_data1)
        assert response.status_code == 200
        response2 = client.post("/user/", json=initial_user_data2)
        assert response2.status_code == 200
        user_exist = response.json()
        assert user_exist["username"] == initial_user_data1["username"]
        assert user_exist["email"] == initial_user_data1["email"]
        assert response.status_code == 200
        response3 = client.post("/login",json={"username": "test_user1", "password": "test_password1"})
        assert response3.status_code ==200 
        client.headers["authorization"] = f"Bearer {response3.json()['access_token']}"
        response4= client.post("/post/",json=initial_post_user_data1)
        assert response4.status_code == 200
        response5= client.post("/post/",json=initial_post_user_data2)
        assert response5.status_code == 200
        response6 = client.get("/post/1")
        assert response6.status_code == 200
        assert response6.json()["title"] == initial_post_user_data1["title"]
        assert response6.json()["text"] == initial_post_user_data1["text"]
        assert response6.status_code == 200
        
def delete_post_by_id():
    with embedded_db():
        initial_user_data1 = {
            "id": 1,
            "username": "test_user1",
            "email": "test_email1",
            "password": "test_password1"}
        initial_user_data2 = {
            "id": 2,
            "username": "test_user2",
            "email": "test_email2",
            "password": "test_password2"}
        initial_post_user_data1={
            "id": 1,
            "user_id": 1,
            "title": "test_title1",
            "text": "test_text1"}
        initial_post_user_data2={
            "id": 2,
            "user_id": 1,
            "title": "test_title2",
            "text": "test_text2"}
        response = client.post("/user/", json=initial_user_data1)
        assert response.status_code == 200
        response2 = client.post("/user/", json=initial_user_data2)
        assert response2.status_code == 200
        user_exist = response.json()
        assert user_exist["username"] == initial_user_data1["username"]
        assert user_exist["email"] == initial_user_data1["email"]
        assert response.status_code == 200
        response3 = client.post("/login",json={"username": "test_user1", "password": "test_password1"})
        assert response3.status_code ==200 
        client.headers["authorization"] = f"Bearer {response3.json()['access_token']}"
        response4= client.post("/post/",json=initial_post_user_data1)
        assert response4.status_code == 200
        response5= client.post("/post/",json=initial_post_user_data2)
        assert response5.status_code == 200
        response6 = client.delete("/post/2")
        assert response6.status_code == 200
        assert response6.json()["title"] == initial_post_user_data1["title"]
        assert response6.json()["text"] == initial_post_user_data1["text"]
        assert response6.status_code == 200
        assert response6.json()["title"] == initial_post_user_data2["title"]
        assert response6.json()["text"] == initial_post_user_data2["text"]
        assert response6.status_code == 200
        
def update_post_by_id():
    with embedded_db():
        initial_user_data1 = {
                "id": 1,
                "username": "test_user1",
                "email": "test_email1",
                "password": "test_password1"}
        initial_user_data2 = {
            "id": 2,
            "username": "test_user2",
            "email": "test_email2",
            "password": "test_password2"}
        initial_post_user_data1={
            "id": 1,
            "user_id": 1,
            "title": "test_title1",
            "text": "test_text1"}
        initial_post_user_data2={
            "id": 2,
            "user_id": 1,
            "title": "test_title2",
            "text": "test_text2"}
        initial_post_user_data_update={
            "title": "test_title_update",
            "text": "test_text_update"}
        
        response = client.post("/user/", json=initial_user_data1)
        assert response.status_code == 200
        response2 = client.post("/user/", json=initial_user_data2)
        assert response2.status_code == 200
        user_exist = response.json()
        assert user_exist["username"] == initial_user_data1["username"]
        assert user_exist["email"] == initial_user_data1["email"]
        assert response.status_code == 200
        response3 = client.post("/login",json={"username": "test_user1", "password": "test_password1"})
        assert response3.status_code ==200 
        client.headers["authorization"] = f"Bearer {response3.json()['access_token']}"
        response4= client.post("/post/",json=initial_post_user_data1)
        assert response4.status_code == 200
        response5= client.post("/post/",json=initial_post_user_data2)
        assert response5.status_code == 200
        response6 = client.put("/post/1",json=initial_post_user_data_update)
        assert response6.status_code == 200
        assert response6.json()["title"] == initial_post_user_data_update["title"]
        assert response6.json()["text"] == initial_post_user_data_update["text"]
        assert response6.status_code == 200
        assert response6.json()["title"] == initial_post_user_data1["title"]
        assert response6.json()["text"] == initial_post_user_data1["text"]
        assert response6.status_code == 200
        assert response6.json()["title"] == initial_post_user_data2["title"]
        assert response6.json()["text"] == initial_post_user_data2["text"]
        assert response6.status_code == 200