from .test_main import embedded_db, client

def test_create_comment():
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
        initial_comment_user_data1={
            "id": 1,
            "creator_id": 1,
            "post_id": 1,
            "text": "test_text1"}
        
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
        response6= client.post("/comment/",json=initial_comment_user_data1)
        assert response6.status_code == 200

def test_get_comment_by_id():
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
        initial_comment_user_data1={
            "id": 1,
            "creator_id": 1,
            "post_id": 1,
            "text": "test_text1"}
        
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
        response6= client.post("/comment/",json=initial_comment_user_data1)
        assert response6.status_code == 200
        response7= client.get("/comment/1")
        assert response7.status_code == 200
        
def test_get_comment_all():
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
        initial_comment_user_data1={
            "id": 1,
            "creator_id": 1,
            "post_id": 1,
            "text": "test_text1"}
        initial_comment_user_data2={
            "id": 2,
            "creator_id": 1,
            "post_id": 1,
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
        response6= client.post("/comment/",json=initial_comment_user_data1)
        assert response6.status_code == 200
        response8= client.post("/comment/",json=initial_comment_user_data2)
        assert response8.status_code == 200
        response7= client.get("/comment/")
        assert response7.status_code == 200
        