from flask_restful import Resource
from flask import make_response,jsonify, request
from app.api.users.v2.models import User
from app.utilities.validators import is_blank,is_number,is_valid_email,is_valid_password,is_valid_space,is_valid_username,is_status

user = User()

class Registration(Resource):
    
    def post(self):
        try:
            data = request.get_json()
            password = data['password']
            email = data['email']
            username = data['username']
            firstname = data['firstname']
            lastname = data['lastname']
            phonenumber = data['phonenumber']
        except Exception:
            return make_response(jsonify({
                'message' : 'Invalid key field'
            }), 400)
        
        if not is_valid_email(email):
            return make_response(jsonify({
                'message':'Invalid email format'
                }), 400)
        if not is_valid_password(password):
            return make_response(jsonify({
                'message':'Password is a max of 8 characters and cannot be empty'
                }), 400)
        if not is_valid_username(firstname) or not is_blank(firstname):
            return make_response(jsonify({
                'message':'Firstname cannot be empty and takes letters only'
                }), 400)  
        if not is_valid_username(lastname)or not is_blank(lastname): 
            return make_response(jsonify({
                'message':'Lastname cannot be empty and takes letters only'
                }), 400)
        if not is_valid_username(username) or not is_blank(username):
            return make_response(jsonify({
                'message':'Username cannot be empty and takes letters only'
                }),400)
        if not is_number(phonenumber) or not is_blank(phonenumber):
            return make_response(jsonify({
                'message':'Phonenumber cannot be empty and should be in numerals'
                }),400)
         
        new_user = user.add_user(email,password,username,firstname,lastname,phonenumber)

        if new_user:
            return make_response(jsonify({
              'message':'Your account has successfully been registered',
              'data': new_user
            }), 201)       
        else:
            return make_response(jsonify({
            'message':'email already exists. Use a different email'
            }), 409)

class LogIn(Resource):
    def post(self):
        try:
            data = request.get_json()
            email = data['email']
            password = data['password']
        except Exception:
            return make_response(jsonify({
                'message' : 'Invalid data, try again'
            }), 400)

        user_login = user.get_user_by_email(email)
        if not user_login:
            return make_response(jsonify( {
                'message' : 'incorrect login credentials. please enter details again'
            }), 401)
        
        valid_password = user.validate_password(password, email)
        if not valid_password:
            return make_response(jsonify({
                'message' : 'incorrect login credentials. please enter details again'
            }), 401)
        login_id = user_login[0]['user_id']
        user_token = user.generate_token(login_id)
        
        if not user_token:
            return make_response(jsonify( {
                'message' : 'token generation failed'
            }), 401)
        
        return make_response(jsonify({
            'message' : 'Successfully logged in',
            'user_id' : login_id,
            'token' : user_token
        }), 200)
      



