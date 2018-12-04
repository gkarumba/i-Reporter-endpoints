from flask_restful import Resource
from flask import make_response, jsonify, request
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


