from datetime import datetime,timedelta
from flask import current_app
import jwt
from werkzeug.security import generate_password_hash, check_password_hash

class MockDb():
    def __init__(self):
        self.users = {}
        self.reports = {}
        
    def drop(self):
        self.__init__()

db = MockDb()

class Parent():
    def update(self, data):
        for key in data:
            setattr(self, key, data[key])
        setattr(self, 'last_updated', datetime.utcnow().isoformat())
        return self.lookup()

class User(Parent):
    def __init__(self,id,email=None, password=None,firstname=None,lastname=None,phonenumber=None,username=None):
        self.id = None
        self.email = email
        self.password = generate_password_hash(password)
        self.firstname = firstname
        self.lastname = lastname
        self.phonenumber = phonenumber
        self.username = username
        

    def add_user(self):
        setattr(self, 'id', db.user_no + 1)
        db.users.update({self.id: self})
        db.user_no += 1
        db.orders.update({self.id: {}})
        return self.lookup()

    def validate_password(self, password):
        if check_password_hash(self.password, password):
            return True
        return False
    
    def lookup(self):
        keys = ['email', 'id']
        return {key: getattr(self, key) for key in keys}

    def generate_user_token(self, userID):  
        try:
            payload = {
                'exp': datetime.utcnow()+timedelta(minutes=10),
                'iat' :datetime.utcnow(),
                'id': userID
            }
            token = jwt.encode(
                payload,
                current_app.config.get('SECRET_KEY'),
                algorithm='HS256'
            )
            return token
        except Exception as err:
                return str(err)
    
    @classmethod
    def get_user_by_email(cls,email):
        for user_id in db.users:
            user = db.users.get(user_id)
            if user.email == email:
                return user
            return None
