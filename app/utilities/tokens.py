import os
import jwt

def decode_token(token):
    try:
        payload = jwt.decode(token, os.environ.get('SECRET_KEY'))
        return payload['id']
    except jwt.ExpiredSignatureError:
        return 'Token has already Expired, Please login again'
    except jwt.InvalidTokenError:
        return 'Invalid token, please login again'
