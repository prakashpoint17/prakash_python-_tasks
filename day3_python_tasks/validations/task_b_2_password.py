'''Password Strength Checker
Length ≥ 8
Contains upper, lower, number'''

class WeakPasswordError(Exception):
    """Custom exception for weak passwords."""
    pass


def password_strength_check(s: str) -> str:
    """
    Password rules:
    - Minimum 8 characters
    - At least one uppercase
    - At least one lowercase
    - At least one digit
    """

    if len(s) < 8:
        raise WeakPasswordError("Password must contain at least 8 characters.")

    if not any(char.islower() for char in s):
        raise WeakPasswordError("Password must contain at least one lowercase letter.")

    if not any(char.isupper() for char in s):
        raise WeakPasswordError("Password must contain at least one uppercase letter.")

    if not any(char.isdigit() for char in s):
        raise WeakPasswordError("Password must contain at least one digit.")

    return "It's a valid password"
