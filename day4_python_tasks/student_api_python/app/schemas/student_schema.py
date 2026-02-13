from pydantic import BaseModel,EmailStr,Field
from typing import Optional

# Create Schema for student data (no- id auto generate)
class StudentCreate(BaseModel):
    name:str = Field(...,min_length=1,max_length=100)
    age:int = Field(...,ge=15,le=100)
    email:EmailStr 
    course:str = Field(...,min_length=1,max_length=60)
    
# Update Schema for student data (optional fields - partial updates)
class StudentUpdate(BaseModel):
    name:Optional[str] = Field(None,min_length=1,max_length=100)
    age:Optional[int]= Field(None,ge=15,le=100)
    email:Optional[EmailStr] = None
    course:Optional[str] = Field(None,min_length=1,max_length=60)
    
# Response Schema for student data (includes ID for output)
class StudentResponse(BaseModel):
    id:int
    name:str 
    age:int 
    email:EmailStr 
    course:str 
    
class Config:
    from_attributes = True #Allows creating from dicts (in-memory data)
    
