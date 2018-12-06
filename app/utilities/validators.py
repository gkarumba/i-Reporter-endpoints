import re

def isValidEmail(email):
    if len(email) > 7:
        if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9.]*\.*[com|org|edu]{3}$)", email) != None:
            return True
        return False

def isValidUsername(u_name):
    if not re.match(r"^[A-Za-z\.\+_-]*$", u_name) != None:
        return False
    return True

def isValidPassword(password):
    if re.match(r"[A-Za-z0-9@#$%^&+=]{8,}", password) != None:
        return True
    else:
        return False

def isValidSpace(input_data):
    if input_data != input_data.strip():
        return False
    return True
    
def isBlank(input_data):
    if input_data and input_data.strip():
        return True
    return False

def isNumber(number):
    if not re.match("^[0-9 \-]+$", number):
        return False
    return True

        