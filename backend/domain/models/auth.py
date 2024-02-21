import re

def check_pw_pattern(pw: str):
    """
    Verifies if the password is strenth.

    Args:
        pw (str): The password that will be verified.

    Pattern:
    - At least one lowercase letter
    - At least one uppercase letter
    - At least one number
    - At least one special character (!, #, @, $, % or &)
    - Must have between 8 and 16 characters

    Returns:
        bool: True if matches, if doesn't returns False.
    """
    return (
        re.search(r"(?=.*[a-z])", pw)
        and re.search(r"(?=.*[A-Z])", pw)
        and re.search(r"(?=.*[0-9])", pw)
        and re.search(r"(?=.*[!#@$%&])", pw)
    )