import os
from datetime import datetime, timedelta
import json
import jwt
from werkzeug.security import generate_password_hash, check_password_hash
#local import
from app.database.database import ReportDB


db = ReportDB()

class User():
    """
        Class for the method of adding a new user to the users table
    """
    def add_user(self,email,password,username,firstname,lastname,phonenumber):
        """
            Method for adding a new user to the users table
        """
        hash_password = generate_password_hash(password)
        username_query = """SELECT * FROM users WHERE username = '{}'""".format(username)
        email_query = """SELECT * FROM users WHERE email = '{}'""".format(email)
        retrieved_username = db.get_all(username_query)
        retrieved_email = db.get_all(email_query)
        
        if retrieved_username or retrieved_email:
            return False
        user_query = """INSERT INTO users (email,password,username,firstname,lastname,phonenumber) VALUES (%s,%s,%s,%s,%s,%s) RETURNING user_id"""
        tupl = (email,hash_password,username,firstname,lastname,phonenumber)
        repo = db.add_to_db(user_query,tupl)
        user_id_query = """SELECT * FROM users WHERE user_id = '{}' """.format(1)
        retrieve_user_id = db.get_one(user_id_query)
        if retrieve_user_id:
            admin_query = """UPDATE users SET isAdmin='{}' WHERE user_id={}""".format(True, 1)
            add_admin = db.update_table_row(admin_query)
        payload = repo
        return payload
 
    def get_user_by_email(self, email):
        """
            Method of retrieving a user by their email
        """
        email_query = """SELECT * FROM users WHERE email = '{}'""".format(email)
        repo = db.get_all(email_query)
        # print(repo)
        if not repo:
            return False
        return repo

    def get_user_by_username(self, username):
        """
            Method for retrieving a user by their username
        """
        username_query = """SELECT * FROM users WHERE username = '{}'""".format(username)
        repo = db.get_all(username_query)
        if not repo:
            return False
        return repo

    def validate_password(self, password, email):
        """
            Method for validating the password
        """
        query = """SELECT password FROM users WHERE email='{}'""".format(email)
        result = db.get_one(query)

        if not check_password_hash(result['password'], password):
            return False
        return True

    def generate_token(self, id):
        """
            Method for generating new tokens
        """
        try:
            payload = {
                'exp' : datetime.utcnow()+timedelta(minutes=60),
                'iat' : datetime.utcnow(),
                'id' : id
            }
            token = jwt.encode(
                payload,
                os.environ.get('SECRET_KEY'),
                algorithm='HS256'
            )
            valid_token = token.decode('utf-8')
            return valid_token
        except Exception as err:
            return str(err)

class Object:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
            