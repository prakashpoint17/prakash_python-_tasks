# Student API Python 🚀

**FastAPI CRUD application** for Python trainee task. Full modular architecture with in-memory storage.

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115.2-green.svg)

## ✨ Features

- ✅ **Full CRUD**: Create, Read, Update, Delete students
- ✅ **Input Validation**: Pydantic schemas (email, age limits)
- ✅ **Auto Documentation**: Swagger UI at `/docs`
- ✅ **Unit Tests**: pytest (100% endpoint coverage)
- ✅ **Modular Architecture**: 5 clean layers
- ✅ **Production Ready**: Error handling, HTTP status codes

## 📁 Project Structure
```
student_api_python/
├── app/ # FastAPI application (main code)
│ ├── init.py # Python package marker
│ ├── main.py # FastAPI app + router mounting
│ ├── schemas/ # 1. Pydantic models (validation)
│ │ └── student_schema.py
| │ └── init.py # Python package marker
│ ├── models/ # 2. Data storage (in-memory list)
│ │ └── student_model.py
| │ └── init.py # Python package marker
│ ├── services/ # 3. Business logic (email unique, ID gen)
│ │ └── student_service.py
| │ └── init.py # Python package marker
│ └── routers/ # 4. HTTP endpoints (REST API)
│ └── student_router.py
| │ └── init.py # Python package marker
├── tests/ # 5. Unit tests (TestClient)
│ └── test_students.py
| │ └── init.py # Python package marker
├── requirements.txt # Dependencies
└── README.md # This file
```

```
**Layered Architecture** (Clean Architecture principle):
HTTP Request → Router → Service → Model → Response
↓ ↓ ↓
Validation Logic Storage
```

## 🚀 Quick Start

# 1. Virtual Environment
```
uv init
uv venv
source .venv/bin/activate  
```

# 3. Install
`uv add -r requirements.txt`

# 4. Run Server
```uvicorn app.main:app --reload --host 0.0.0.0 --port 8000```

🌐 Open Browser: http://localhost:8000/


📋 API Endpoints
---

| Method  | Endpoint         | Description         | Status Code |
|---------|------------------|---------------------|-------------|
| POST    | /students/       | Create student      | 201         |
| GET     | /students/       | List all students   | 200         |
| GET     | /students/{id}   | Get student by ID   | 200 / 404   |
| PUT     | /students/{id}   | Update student      | 200 / 404   |
| DELETE  | /students/{id}   | Delete student      | 204 / 404   |

---

# 📖 Sample Requests

## 1. Create Student

```
curl -X POST "http://localhost:8000/students/" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Priya Sharma",
    "age": 19,
    "email": "priya@college.com",
    "course": "CSE"
  }'
  ```
Response:
```
json
{
  "id": 1,
  "name": "Priya Sharma",
  "age": 19,
  "email": "priya@college.com",
  "course": "CSE"
}
```

## 2. List Students
~~~
curl http://localhost:8000/students/
~~~

Response:

~~~json
[
  {"id": 1, "name": "Priya Sharma", "age": 19, "email": "priya@college.com", "course": "CSE"}
]
~~~

## 3. Update Student

~~~ bash
curl -X PUT "http://localhost:8000/students/1" \
  -H "Content-Type: application/json" \
  -d '{"name": "Priya S.", "age": 20}'
~~~

# 🧪 Testing

# Install test deps
`pip install pytest`

# Run all tests
`pytest tests/ -v`

# Expected: 1 passed in 0.05s

🛠️ Tech Stack

- Framework: FastAPI 0.115.2
- Server:    Uvicorn 0.32.0
- Validation: Pydantic 2.9.2
- Testing:   pytest 8.3.3
- Storage:   In-memory list (Week 3: SQLAlchemy)

---

📈 Layer Flow

~~~
    A[HTTP Request] --> B[Router<br>/students/]
    B --> C[Service<br>Business Logic]
    C --> D[Model<br>In-memory DB]
    D --> C
    C --> B
    B --> E[JSON Response]
~~~
---

## FINAL TEST

**Preview README**:
```bash
cat README.md | head -50
# Or open in VSCode/Markdown viewer
```

Full project COMPLETE ✅

# Run & Show:

~~~bash
uvicorn app.main:app --reload  # Server
~~~

## Open http://localhost:8000/

