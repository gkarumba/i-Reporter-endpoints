from flask_restful import Resource
from flask import make_response, jsonify, request
from werkzeug.security import check_password_hash
from .models import User

class Registration(Resource):
    
    def post(self):
        try:
            data = request.get_json()
            email = data['email']
            password = data['password']
            confirm_password = data['password']
            firstname = data['firstName']
            lastname = data['lastName']
            phonenumber = data['phoneNumber']
            username = data['userName']
            registered = data['registered']
            isAdmin = data['isadmin']
        
        if type(data['email']) != str or type(data['password']) != str or type(data['firstName']) or type(data['lastName']) or type(data['phoneNumber']) != int or type(data['userName']) != str:
            return make_response(jsonify({
                "message":"email,password and names should be strings, phonenumber should be integers"
            }))

        if 


        if User.get_user_by_email(email):
            return make_response(jsonify({
                'message' : 'Account with the provided email already exists. Please login '
            }), 400)

        if User.get_user_by username(username):
            return make_response(jsonify({
                'message' : 'Account with the provided username already exists. Please login '
            }), 400)
        
        user = User(email, password,confirm_password,firstname,lastname, phonenumber,username,isAdmin)
        user.add()

        return make_response(jsonify({
                'message' : 'Account created successfully '
            }), 201)

class SignIn(Resource):
    def post(self):
        try: 
            data = request.get_json()
            email = data['email']
            password = data['password']

        except:
            return make_response(jsonify({
                "message": "Data is empty"
            }), 200)
        user = User.get_user_by_email(email)
        if type(data['email']) != str or type(['password'])!= str:
            return make_response(jsonify({
                "message":"email and password should be strings"
            }))
        elif not email:
            return make_response(jsonify({
                "message":"wrong email address"
            }), 404)
        elif not check_password_hash(user.password, password):
            return make_response(jsonify({
                "message": "wrong password"
            }), 400)

        token = create_access_token(identity=(username, user.isAdmin))
        return make_response(jsonify({
            'token': token,
            'message': f'Login was successful{username}',
            'admin':user.isAdmin
            }), 200)

    


