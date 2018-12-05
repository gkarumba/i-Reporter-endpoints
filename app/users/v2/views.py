from flask_restful import Resource
from flask import make_response,jsonify, request
from app.users.v2.models import User

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
     
        new_user = user.add_user(email, password, username, firstname, lastname, phonenumber)
        
        if not new_user:
            return make_response(jsonify({
                'message' : 'Email already exists'
            }), 400)
        return make_response(jsonify({
            'message' : 'Account Registered Successfully',
            'data' : new_user
        }), 201)

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
        
        user_id = queried_user[0]['id']
        valid_password = user.validate_password(password, email)
        if not check_password:
            return make_response(jsonify({
                'message' : 'incorrect login credentials. please enter details again'
            }), 401)
        user_token = user.generate_token(user_id)
        
        if not user_token:
            return make_response(jsonify( {
                'message' : 'token generation failed'
            }), 401)
        
        return make_response(jsonify({
            'message' : 'Successfully logged in',
            'data' : user_token.decode()
        }), 200)
      