#"Student Marks Processor"

'''
Create a program that:

Accepts student name
Accepts 5 subject marks

Calculates
Total | Average | Grade (A/B/C/Fail)

Store result in a dictionary
Save the dictionary to a JSON file

Read the file again and print results
'''

import json

def subject_data()-> dict:
    
    try:
        name=input("Enter your Name : ")
        subjects_count=int(input("Enter the Number of Subjects : "))

        my_data={"Name":name,"subjects":{}}
        

        for i in range(1,subjects_count+1):
            subject=input("Enter the Subject Name : ")
            marks=int(input(f"Enter the Mark scored in {subject} : "))
            
            my_data["subjects"][subject]=marks

        return my_data,subjects_count
    
    except Exception as e:
        print(e)

def get_grade(mark):
    
    if mark >= 90:
        return "A"
    elif mark >= 70:
        return "B"
    elif mark >= 50:
        return "C"
    else:
        return "Fail"
    

def mark_calculation(data:dict ,subjects) -> dict:
    
    total = 0

    #grade update
    try:
        for sub in list(data["subjects"].keys()):
            mark=data["subjects"][sub]
            data["subjects"][sub]={
                "marks":mark,
                "grade":get_grade(mark)
            }
            total += mark
        
        average = total/subjects
        
        data["total"] = total
        data["average"] = average
        data["total_grade"] = get_grade(average)
        
        return data
    
    except Exception as e:
        print(e)
# ---------------- MAIN ---------------- #

data,subjects = subject_data()
print(data)

updated_data = mark_calculation(data,subjects)

#storeing json data
try:
    with open("student_marks.json","r") as file:
        students = json.load(file)
        
        if isinstance(students, dict):
            students = [students]

except FileNotFoundError:
    students=[]
    
#append New Data
students.append(updated_data)

#write back
with open("student_marks.json","w") as file:
    json.dump(students,file,indent=4)
    
print("saved successfully")

#printing the stores json data
print("The data stored in the json file")

try:
    with open("student_marks.json","r") as file:
        data=json.load(file)
        
    print(data)
    
except FileNotFoundError as e:
    print(e)
