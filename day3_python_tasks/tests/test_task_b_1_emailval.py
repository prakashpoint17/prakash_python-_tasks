from validations.task_b_1_emailval import validate_email

'''email_id = "abc1245@gmail.com"

if validate_email(email_id):
    print(f"{email_id} is a valid email ID")
else:
    print(f"{email_id} is a valid not a email ID , Missing Charecters '@' and '.' ")'''

def test_valid_email():
    assert validate_email("test@gmail.com") == True
    
def test_invalid_email_no_at():
    assert validate_email("testgmail.com") == False
    
def test_invalid_email_no_dot():
    assert validate_email("testgmailcom") == False
