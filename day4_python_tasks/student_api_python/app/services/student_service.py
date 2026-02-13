'''Buisness Logic Layer - validate, ID generation, orchestration, clean data before saving'''

from typing import List, Optional
from app.models.student_model import(students,get_all_students,get_student_by_id,create_student,update_student,delete_student)
from app.schemas.student_schema import StudentCreate,StudentUpdate,StudentResponse

import re

def validate_and_clean_email(email:str) -> str:
    '''clean + validate email format'''
    
    cleaned=email.lower().strip()
    
    if not re.match(r"[^@]+@[^@]+.[^@]+",cleaned):
        raise ValueError("Invalid email format")
    return cleaned

def is_email_unique(email:str) -> bool:
    '''check if email already exist in DB'''
    '''for s in students:
        if s["email"]==email:
            return False
        return True'''
        
    return not any(s["email"]==email for s in students)

def create_student_service(student_in:StudentCreate)-> StudentResponse:
    '''Full create flow : validate - generate id - save - return'''
    
    #1.clean validate email
    email=validate_and_clean_email(student_in.email)
    
    #2.Buisness rule unique email
    if not is_email_unique(email):
        raise ValueError("Email already exists")
    
    #3.Auto generate sequential ID
    new_id=max([s["id"] for s in students],default=0) + 1 if students else 1
    
    #4.clean other date
    student_data={
        "id":new_id,
        "name":student_in.name.strip(),
        "age":student_in.age,
        "email":email,
        "course":student_in.course.strip()
    }
    
    #5. save+return typed response
    created = create_student(student_data)
    
    return StudentResponse(**created)

def get_all_students_service() -> list[StudentResponse]:
    """Get all, convert to response model"""
    return [StudentResponse(**s) for s in get_all_students()]

def get_studeny_service(student_id:int) -> Optional[StudentResponse]:
    student = get_student_by_id(student_id)
    return StudentResponse(**student) if student else None

def update_student_service(studen_id:int, student_update:StudentUpdate) -> Optional[StudentResponse]:
    """Partial update flow"""
    
    update_data=student_update.model_dump(exclude_unset=True)
    
    #email special handling
    
    if "email" in update_data:
        new_email = validate_and_clean_email(update_data["email"])
        
        current_student=get_student_by_id(studen_id)
        
        if current_student and new_email != current_student["email"]:
            if not is_email_unique(new_email):
                raise ValueError("Email already exists")
            
        update_data["email"] = new_email
        
    #Update model
    updated = update_student(studen_id,update_data)
    
    return StudentResponse(**updated) if updated else None

def delete_student_service(student_id:int) -> bool:
    '''Delete wrapper'''
    return delete_student(student_id)
