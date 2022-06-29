def test_create_comment(client, embedded_db):
    initial_user_data1 = {
        "username": "test_user1",
        "email": "test_email1",
        "password": "test_password1"}
    initial_post_data1 = {
        "title": "test_title1",
        "text": "test_text1"}
    initial_comment1 = {
        "text": "test_text1"}

    # create user 1
    response = client.post("/user/", json=initial_user_data1)
    assert response.status_code == 200

    # inisialisasi user 1
    user_data = response.json()
    assert user_data["username"] == initial_user_data1["username"]
    assert user_data["email"] == initial_user_data1["email"]
    assert response.status_code == 200
    # login user 1
    response3 = client.post("/login", json={"username": "test_user1", "password": "test_password1"})
    assert response3.status_code == 200
    client.headers["authorization"] = f"Bearer {response3.json()['access_token']}"
    # create post user 1
    response4 = client.post("/post/", json=initial_post_data1)
    assert response4.status_code == 200
    
    # create comment user 1
    post_data = response4.json()
    post_id = post_data["id"]
    response5 = client.post("/comment/", json={"post_id": post_id, "text":initial_comment1["text"]})
    assert response5.status_code == 200


def test_get_comment_by_id(client, embedded_db):
    initial_user_data1 = {
        "username": "test_user1",
        "email": "test_email1",
        "password": "test_password1"}
    initial_post_data1 = {
        "title": "test_title1",
        "text": "test_text1"}
    initial_comment1 = {
        "text": "test_text1"}

    # create user 1
    response = client.post("/user/", json=initial_user_data1)
    assert response.status_code == 200
    
    # inisialisasi user 
    user_data = response.json()
    assert user_data["username"] == initial_user_data1["username"]
    assert user_data["email"] == initial_user_data1["email"]
    assert response.status_code == 200
    
    # login user 
    response3 = client.post("/login", json={"username": "test_user1", "password": "test_password1"})
    assert response3.status_code == 200
    
    # post auth user dan access token
    client.headers["authorization"] = f"Bearer {response3.json()['access_token']}"
    
    # create post user 1
    response4 = client.post("/post/", json=initial_post_data1)
    assert response4.status_code == 200
    
    # create comment
    post_data = response4.json()
    post_id = post_data["id"]
    response5 = client.post("/comment/", json={"post_id": post_id, "text":initial_comment1["text"]})
    assert response5.status_code == 200
    
    
    
    # show comment by id
    comment_data = response5.json()
    comment_id = comment_data["id"]
    response6 = client.get(f"/comment/{comment_id}")
    assert response6.status_code == 200


def test_get_comment_all(client, embedded_db):
    initial_user_data1 = {
        "username": "test_user1",
        "email": "test_email1",
        "password": "test_password1"}
    initial_user_data2 = {
        "username": "test_user2",
        "email": "test_email2",
        "password": "test_password2"}
    initial_post1 = {
        "title": "test_title1",
        "text": "test_text1"}
    initial_post2 = {
        "title": "test_title2",
        "text": "test_text2"}
    initial_comment1 = {
        "text": "test_text1"}
    initial_comment2 = {
        "text": "test_text2"}
    
    # create user 1
    response = client.post("/user/", json=initial_user_data1)
    assert response.status_code == 200
    
    # create user 2
    response2 = client.post("/user/", json=initial_user_data2)
    assert response2.status_code == 200
    
    # inisialisasi user 1
    user_data = response.json()
    assert user_data["username"] == initial_user_data1["username"]
    assert user_data["email"] == initial_user_data1["email"]
    assert response.status_code == 200
    
    # login user 1
    response3 = client.post("/login", json={"username": "test_user1", "password": "test_password1"})
    assert response3.status_code == 200
    
    # auth user dan access token_type
    client.headers["authorization"] = f"Bearer {response3.json()['access_token']}"
    
    # create post user 1
    response4 = client.post("/post/", json={"title":initial_post1["title"], "text":initial_post1["text"]})
    assert response4.status_code == 200
    
    # create comment 1
    post_data1 = response4.json()
    post_id = post_data1["id"]
    response5 = client.post("/comment/", json={"post_id": post_id, "text":initial_comment1["text"]})
    assert response5.status_code == 200
    
    # login user 2
    responses6 = client.post("/login", json={"username": "test_user2", "password": "test_password2"})
    assert responses6.status_code == 200
    
    # auth user dan access token_type
    client.headers["authorization"] = f"Bearer {responses6.json()['access_token']}"
    
    #create post 2
    response7 = client.post("/post/", json={"title":initial_post2["title"], "text":initial_post2["text"]})
    assert response7.status_code == 200
    
    # create comment 2
    post_data = response7.json()
    post_id = post_data["id"]
    response8 = client.post("/comment/", json={"post_id": post_id, "text":initial_comment2["text"]})
        
    # show all comment
    response9 = client.get("/comment/")
    assert response9.status_code == 200
    
    comment_data = response9.json()
    assert comment_data[0]["id"] == response5.json()["id"]
    assert comment_data[0]["text"] == initial_comment1["text"]
    
    assert comment_data[1]["id"] == response8.json()["id"]
    assert comment_data[1]["text"] == initial_comment2["text"]
    