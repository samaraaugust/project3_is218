

def test_csv_upload(client):
    response = client.post("/login", data={"email": "test@email.com", "password": "tester1"})
    csv = "tests/test_music.csv"
    csv_data = open(csv, "rb")
    data = {"file": (csv_data, "test_music.csv")}
    response2 = client.post("/songs", data=data)
    print(response2.data)
    assert response2.status_code == 302
    assert response2.headers["Location"] == "/songs_tables"
