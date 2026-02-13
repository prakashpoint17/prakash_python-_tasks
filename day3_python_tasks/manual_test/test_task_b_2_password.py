
from validations.task_b_2_password import password_strength_check, WeakPasswordError

password = "alphaking_17"

try:
    result = password_strength_check(password)
    print(result)

except WeakPasswordError as e:
    print(e)
