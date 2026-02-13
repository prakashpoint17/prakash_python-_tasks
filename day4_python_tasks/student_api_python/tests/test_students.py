from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_CRUD():
    #1.Create
    resp=client.post("/students/",json={
            "name":"Test",
            "age":20,
            "email":"abc123@gmail.com",
            "course":"Test file"
    })
    
    assert resp.status_code == 201
    id = resp.json()["id"]
    
    #2.READ
    assert client.get(f"/students/{id}").status_code == 200
    assert client.get("/students/").status_code==200
    
    #3.Update
    assert client.put(f"/students/{id}",json={"name":"Updated"}).status_code == 200
    
    #4.delete
    assert client.delete(f"/students/{id}").status_code == 200