from flask_restful import Resource
from flask import make_response,jsonify, request
from app.users.v1.models import User

class Registration(Resource):
    
    def post(self):
        data = request.get_json()
        email = data['email']
        password = data['password']
        firstname = data['firstname']
        lastname = data['lastname']
        username = data['username']
        phonenumber = data['phonenumber']
        
        if not User.get_user_by_email(email):
            new_user = User(email=email, password=password, firstname=firstname, lastname=lastname,username=username,phonenumber=phonenumber)
            new_user.add_user()
        
            return make_response(jsonify({
                'message' : 'Your account has successfully been registered '
            }), 201)
        else:
            response = {
                    'message': ' email already exists. Use a different email'
                    }
            return make_response(jsonify(response), 409)
               

        
class LogIn(Resource):
    
    def post(self):
        data = request.get_json()
        email = data['email']
        password = data['password']
        
        try:
            user = User.get_user_by_email(email)
            user_id = user.id
            if user and user.validate_password(password):
                user_token = user.generate_token(user_id)
                if user_token:
                    response = {
                        'message' : 'Login Successful',
                        'data' : user_token.decode('UTF-8')
                    }
                    return make_response(jsonify(response), 200)
            else:
                response = {
                    'message' : 'Invalid password, please try again'
                }
                return make_response(jsonify(response), 401)
        except Exception:
            response = {
                'message' : 'wrong email address, use a different email'
            }
            return make_response(jsonify(response), 400)