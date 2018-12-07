import re

def isValidEmail(email):
    """
        Validates the email format
    """
    if len(email) > 7:
        if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9.]*\.*[com|org|edu]{3}$)", email) != None:
            return True
        return False

def isValidUsername(u_name):
    """
        Validates the name format 
    """
    if not re.match(r"^[A-Za-z\.\+_-]*$", u_name) != None:
        return False
    return True

def isValidPassword(password):
    """
        Validates the password format
    """
    if re.match(r"[A-Za-z0-9@#$%^&+=]{8,}", password) != None:
        return True
    else:
        return False

def isValidSpace(input_data):
    """
        Checks for whitespaces
    """
    if input_data != input_data.strip():
        return False
    return True
    
def isBlank(input_data):
    """
        Checks for blank inputs
    """
    if input_data and input_data.strip():
        return True
    return False

def isNumber(number):
    """
        Checks if input is integers
    """
    if not re.match("^[0-9 \-]+$", number):
        return False
    return True

def isFlag(check_str):
    """
        Checks the flag type
    """
    if re.search(r'\bredflag\b|\bintervention\b', check_str):
        return False
    return True

def isImage(img):
    if re.match(r".*\.(jpg|png|gif)$", img):
        return True
    return False

def isVideo(video):
    if re.match(r".*\.(mp4|mkv|3gp)$", video):
        return True
    return False

