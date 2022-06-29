def test_post_create(client, embedded_db):
    # this test is to test the post creation
    initial_user_data1 = {
        "username": "test_user1",
        "email": "test_email1",
        "password": "test_password1"}
    initial_post1 = {
        "title": "test_title1",
        "text": "test_text1"}
    # membuat User 1
    response = client.post("/user/", json=initial_user_data1)
    assert response.status_code == 200

    # inisialisasi data login
    user_data_login = response.json()
    assert user_data_login["username"] == initial_user_data1["username"]
    assert user_data_login["email"] == initial_user_data1["email"]
    assert response.status_code == 200

    # login dengan data user
    response3 = client.post("/login", json={"username": "test_user1", "password": "test_password1"})
    assert response3.status_code == 200

    # authentikasi data pada user
    client.headers["authorization"] = f"Bearer {response3.json()['access_token']}"
    assert response3.status_code == 200

    # posted post-1
    response4 = client.post("/post/", json=initial_post1)
    assert response4.status_code == 200    

    # assert data post1
    user_data_post1 = response4.json()
    assert user_data_post1["title"] == initial_post1["title"]
    assert user_data_post1["text"] == initial_post1["text"]


def test_get_all_posts(client, embedded_db):
    # this test is to test get all posts
    initial_user_data1 = {
        "username": "test_user1",
        "email": "test_email1",
        "password": "test_password1"}
    initial_post1 = {
        "title": "test_title1",
        "text": "test_text1"}
    # create user 1
    response = client.post("/user/", json=initial_user_data1)
    assert response.status_code == 200


    user_data1 = response.json()
    assert user_data1["username"] == initial_user_data1["username"]
    assert user_data1["email"] == initial_user_data1["email"]
    assert response.status_code == 200

    # login user yang sudah di create
    response3 = client.post("/login", json={"username": "test_user1", "password": "test_password1"})
    assert response3.status_code == 200

    # auth dikasih ke user 1
    client.headers["authorization"] = f"Bearer {response3.json()['access_token']}"

    # posted post-1
    response4 = client.post("/post/", json=initial_post1)
    assert response4.status_code == 200

    # get post-1
    response6 = client.get("/post/alltab")
    assert response6.status_code == 200


def test_get_post_by_id(client, embedded_db):
    # this test is to test get post by id
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

    # create user data 1
    response = client.post("/user/", json=initial_user_data1)
    assert response.status_code == 200

    # create user data 2
    response2 = client.post("/user/", json=initial_user_data2)
    assert response2.status_code == 200

    # inisialisasi data user
    user_data1 = response.json()
    assert user_data1["username"] == initial_user_data1["username"]
    assert user_data1["email"] == initial_user_data1["email"]

    # login user yang sudah di created 1
    response3 = client.post("/login", json={"username": "test_user1", "password": "test_password1"})
    assert response3.status_code == 200

    # authentication pada user 1
    client.headers["authorization"] = f"Bearer {response3.json()['access_token']}"

    # posted post data 1
    response5 = client.post("/post/", json=initial_post1)
    assert response5.status_code == 200

    # inisialisasi data user ke 2
    user_data2 = response.json()
    assert user_data2["username"] == initial_user_data1["username"]
    assert user_data2["email"] == initial_user_data1["email"]

    # login user has been created 2
    response6 = client.post("/login", json={"username": "test_user2", "password": "test_password2"})
    assert response6.status_code == 200

    # authentication token user 2
    client.headers["authorization"] = f"Bearer {response3.json()['access_token']}"
    
    # posted post data 2
    response7 = client.post("/post/", json=initial_post2)
    assert response7.status_code == 200

    # get post by id
    post_data = response7.json()
    post_id = post_data["id"]
    response8 = client.get(f"/post/{post_id}")
    assert response8.status_code == 200

    post_data2 = response8.json()
    post_data1 = response5.json()
    assert post_data1["text"] == initial_post1["text"]
    assert post_data1["title"] == initial_post1["title"]
    assert post_data2["text"] == initial_post2["text"]
    assert post_data2["title"] == initial_post2["title"]


def test_delete_post_by_id(client, embedded_db):
    # this test is to test delete post by id
    initial_user_data1 = {
        "username": "test_user1",
        "email": "test_email1",
        "password": "test_password1"}
    initial_user_data2 = {
        "username": "test_user2",
        "email": "test_email2",
        "password": "test_password2"}
    initial_post_user_data1 = {
        "title": "test_title1",
        "text": "test_text1"}
    initial_post_user_data2 = {
        "title": "test_title2",
        "text": "test_text2"}
    # create user 1
    response = client.post("/user/", json=initial_user_data1)
    assert response.status_code == 200
    # create user 2
    response2 = client.post("/user/", json=initial_user_data2)
    assert response2.status_code == 200
    # assert user data
    user_data = response.json()
    assert user_data["username"] == initial_user_data1["username"]
    assert user_data["email"] == initial_user_data1["email"]
    assert response.status_code == 200
    # login user
    response3 = client.post("/login", json={"username": "test_user1", "password": "test_password1"})
    assert response3.status_code == 200
    # auth user
    client.headers["authorization"] = f"Bearer {response3.json()['access_token']}"
    # create post 1
    response4 = client.post("/post/", json=initial_post_user_data1)
    assert response4.status_code == 200
    # create post 2
    response5 = client.post("/post/", json=initial_post_user_data2)
    assert response5.status_code == 200
    # delete post
    post_data = response5.json()
    post_id = post_data["id"]
    response6 = client.delete(f"/post/{post_id}")
    assert response6.status_code == 200


def test_update_post_by_id(client, embedded_db):
    # this test is to test update post by id
    initial_user_data1 = {
        "username": "test_user1",
        "email": "test_email1",
        "password": "test_password1"}
    initial_post_user_data1 = {
        "title": "test_title1",
        "text": "test_text1"}
    initial_post_user_data_update = {
        "title": "test_title_update",
        "text": "test_text_update"}
    # create user
    response = client.post("/user/", json=initial_user_data1)
    assert response.status_code == 200
    # assert user data
    user_data = response.json()
    assert user_data["username"] == initial_user_data1["username"]
    assert user_data["email"] == initial_user_data1["email"]
    assert response.status_code == 200
    # login user
    response3 = client.post("/login", json={"username": "test_user1", "password": "test_password1"})
    assert response3.status_code == 200
    # auth user
    client.headers["authorization"] = f"Bearer {response3.json()['access_token']}"
    # create post 1
    response4 = client.post("/post/", json=initial_post_user_data1)
    assert response4.status_code == 200

    post_data1 = response4.json()
    post_id1 = post_data1["id"]

    response6 = client.put(f"/post/{post_id1}", json=initial_post_user_data_update)
    assert response6.status_code == 200

    # get post by id
    response7 = client.get(f"/post/{post_id1}")
    assert response7.status_code == 200

    post_data1 = response7.json()
    assert post_data1["text"] == initial_post_user_data_update["text"]
    assert post_data1["title"] == initial_post_user_data_update["title"]