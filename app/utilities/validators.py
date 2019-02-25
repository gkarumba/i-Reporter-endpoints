import re
import json

def is_valid_email(email):
    """
        Method that Validates the email format
    """
    if len(email) > 7:
        if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9.]*\.*[com|org|edu]{3}$)", email) != None:
            return True
        return False

def is_valid_username(u_name):
    """
       Method that Validates the name format 
    """
    if not re.match(r"^[A-Za-z\.\+_-]*$", u_name) != None:
        return False
    return True

def is_valid_password(password):
    """
        Method that Validates the password format
    """
    if re.match(r"[A-Za-z0-9@#$%^&+=]{8,}", password) != None:
        return True
    else:
        return False

def is_valid_space(input_data):
    """
        Method that Checks for whitespaces
    """
    if input_data != input_data.strip():
        return False
    return True
    
def is_blank(input_data):
    """
        Method that Checks for blank inputs
    """
    if input_data and input_data.strip():
        return True
    return False

def is_number(number):
    """
        Method that Checks if input is integers
    """
    if not re.match("^[0-9 \-]+$", number):
        return False
    return True

def is_flag(check_flag):
    """
        Method that Checks the flag type match the two defaults
    """
    flag_list = ['redflag','intervention']
    if check_flag in flag_list:
        return True
    return False

def is_status(check_stt):
    """
       Method that Checks if the status is the correct format
    """
    status_list = ['rejected','resolved','under investigation']
    if check_stt in status_list:
        return True
    return False
    
def is_location(location):
    """ 
       Method that Checks if the location is in the format long/lat
    """
    coords = []
    loc = json.dumps(location)
    check_loc = re.split(',|"',loc)
    coords.append(check_loc)
    check_long = re.search("^(\+|-)?(?:180(?:(?:\.0{1,6})?)|(?:[0-9]|[1-9][0-9]|1[0-7][0-9])(?:(?:\.[0-9]{1,6})?))$", coords[0][1])
    check_lat = re.search("^(\+|-)?(?:90(?:(?:\.0{1,6})?)|(?:[0-9]|[1-8][0-9])(?:(?:\.[0-9]{1,6})?))$", coords[0][1])
    if check_lat:
        return True
    return False

def is_image(img):
    """
        Method that checks for the correct image format
    """
    if re.match(r".*\.(jpg|png|gif)$", img):
        return True
    return False

def is_video(vid):
    """
        Method that checks for the correct video format
    """
    if re.match(r".*\.(mp4|mkv|3gp)$", vid):
        return True
    return False

