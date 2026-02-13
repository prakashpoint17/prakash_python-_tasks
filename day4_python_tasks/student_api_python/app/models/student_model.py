# im memory student storage - simulates database

#Global database - list of dicts (lost on restart)

students: list[dict] = []

def get_all_students() -> list[dict]:
    """Return all students"""
    return students

def get_student_by_id(student_id:int) -> dict|None:
    """Get student by id if not return None"""
    for student in students:
        if student["id"] == student_id:
            return student
        return None
    
def create_student(student_data:dict) -> dict:
    """create new student data as a list"""
    students.append(student_data)
    return student_data

def update_student(student_id:int, update_data:dict) -> dict|None : 
    """update student date if update data is not none using student id"""
    student=get_student_by_id(student_id)
    
    if student:
        for key,value in update_data.items():
            if value is not None:
                student[key]=value
        return student
    return None
            
def delete_student(student_id:int) -> bool:
    '''Delete student by ID, Return True if Deleted'''
    
    global students
    
    initial_len = len(students)
    
    students = [s for s in students if s["id"] != student_id] 
    return len(students)<initial_len
    
