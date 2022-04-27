"""This test the homepage"""

def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'href="/login"' in response.data
    assert b'href="/register"' in response.data

def test_auth_pages(client):
    """This makes the index page"""
    response = client.get("/dashboard")
    assert response.status_code == 302
    response = client.get("/register")
    assert response.status_code == 200
    response = client.get("/login")
    assert response.status_code == 200

def test_successful_login(client, auth):
    """Successful login redirects to the dashboard"""
    assert client.get("/login").status_code == 200
    response = auth.login()
    assert response.headers["Location"] == "/dashboard"

def test_successful_registration(client):
    """Successful registration redirects to login page"""
    assert client.get("/register").status_code == 200
    response = client.post("/register", data={"email": "first2@email.com", "password": "tester", "confirm": "tester"})
    assert response.headers["Location"] == "/login"

def test_dashboard_logged_in(client):
    """If user is logged in can access dashboard page"""
    response = client.post("/login", data={"email": "test@email.com", "password": "tester1"})
    response2 = client.get("/dashboard")
    assert b"Welcome: test@email.com" in response2.data
    assert b"Dashboard" in response2.data

def test_dashboard_not_logged_in(client):
    """if user is not logged in can not access dashboard gets sent back to login page"""
    response = client.get("/dashboard")
    assert response.headers["Location"] == "/login?next=%2Fdashboard"

def test_denying_upload(client):
    """if user is not logged in can not access songs page"""
    response = client.post("/songs")
    assert response.headers["Location"] == "/login?next=%2Fsongs"

