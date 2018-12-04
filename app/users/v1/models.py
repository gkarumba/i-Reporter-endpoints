from datetime import datetime,timedelta
import psycopg2
from flask import current_app
import jwt
from werkzeug.security import generate_password_hash, check_password_hash

class MockDb():
    def __init_(self):
        try:
            self.connection = psycopg2.connect(
                os.getenv('DATABASE_URL'))
            self.cursor = self.connection.cursor()
        
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

class User(MockDb):
    def __init__(self,email=None, password=None,
                  firstname=None,lastname=None,
                  phonenumber=None,username=None,isAdmin=False):
        super().__init__()
        self.email = email
        if password:
            self.password = generate_password_hash(password)
        self.firstname = firstname
        self.lastname = lastname
        self.phonenumber = phonenumber
        self.username = username
        self.isAdmin = isAdmin

    def add(self):
        self.cursor.execute(
            '''INSERT INTO users(email, password,firstname,lastname, phonenumber,username,isAdmin) VALUES(%s,%s,%s,%s,%s,%s,%s)''',
            (self.email, self.password, self.firstname,self.lastname,self.phonenumber,self.username,self.isAdmin ))

        self.connection.commit()
        self.cursor.close()

    def get_user_by_email(self,email):
        self.cursor.execute(''' SELECT * FROM users WHERE email=%s''', (email))
        user = self.cursor.fetchone()
        self.connection.commit()
        self.cursor.close()

        if user:
            return self.convert_data(user)
        return None

    def serialize(self):
        return dict (
            id = self.id
            email = self.email
            firstname = self.firstname
            lastname= self.lastname
            phonenumber = self.phonenumber
            username = self.username
            isAdmin = self.isAdmin
        )
    
    def convert_data(self,data):
        self.id = data['0']
        self.email = data['1']
        self.firstname = data['2']
        self.lastname = data['3']
        self.phonenumber = data['4']
        self.username = data['5']
        self.isAdmin = data['6']

        return self



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
