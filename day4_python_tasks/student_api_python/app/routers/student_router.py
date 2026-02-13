#Student api endpoint
'''Endpoints required:

Method	Endpoint	Description
POST	/students	Create student
GET	/students	List all students
GET	/students/{id}	Get student by id
PUT	/students/{id}	Update student
DELETE	/students/{id}	Delete student'''

from fastapi import APIRouter,HTTPException,Path
from app.services.student_service import(create_student_service,get_all_students_service,get_studeny_service,update_student_service,delete_student_service)
from app.schemas.student_schema import StudentCreate,StudentUpdate,StudentResponse

#Create router with prefix/tags
router = APIRouter(prefix="/students",tags=["students"],responses={404:{"description":"Not found"}})

@router.post("/",response_model=StudentResponse,status_code=201)
async def create(student:StudentCreate):
    try:
        return create_student_service(student)
    except ValueError as e:
        raise HTTPException(400,str(e))

@router.get("/")
async def list():
    return get_all_students_service()

@router.get("/{id}")
async def get(id: int):
    student = get_studeny_service(id)
    if not student:
        raise HTTPException(404,"Not Found")
    return student

@router.put("/{id}")
async def update(id:int,data:StudentUpdate):
    updated=update_student_service(id,data)
    if not updated:
        raise HTTPException(404,"Not Found")
    return updated

@router.delete("/{id}")
async def delete(id:int):
    if not delete_student_service(id):
        raise HTTPException(404,"Not Found")