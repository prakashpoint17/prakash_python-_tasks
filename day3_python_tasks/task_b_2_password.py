'''Password Strength Checker
Length ≥ 8
Contains upper, lower, number'''

class WeakPasswordError(Exception):
    pass

def password_strength_check(s:str):
    
    char_length=False
    has_upper=False
    has_lower=False
    has_digit=False
    
    if len(password) < 8:
        raise WeakPasswordError("Oops ! your password should Contain atleast 8 charecters")
    else:
        char_length=True
    
    if s.isupper():
        raise WeakPasswordError("Oops! there is no lowercase charecter in your password.")
    else:
        has_lower = True
    
    if s.islower():
        raise WeakPasswordError("Oops! there is no Uppercase charecter in your password.")
    else:   
        has_upper = True
    
    if any(char.isdigit() for char in s):
        has_digit=True
    else:
        raise WeakPasswordError("Oops! there is no number in your password.")
    
    if char_length and has_upper and has_lower and has_digit:
        return "It's an Valid password"
        
password = "Alphaking_17"

try: 
    print(password_strength_check(password))
except WeakPasswordError as e:
    print(e)
    
print(password.isdigit())