#Email Validator (Simple)
#Check if email contains @ and .

def email_validate(s:str) -> bool:
    
    if "@" in s and "." in s:
        return True
    else:
        return False
            

email_id = "abc1245@gmail.com"

if email_validate(email_id):
    print(f"{email_id} is a valid email ID")
else:
    print(f"{email_id} is a valid not a email ID , Missing Charecters '@' and '.' ")
