#Email Validator (Simple)
#Check if email contains @ and .

def validate_email(s:str) -> bool:
    
    if "@" in s and "." in s:
        return True
    else:
        return False
            
