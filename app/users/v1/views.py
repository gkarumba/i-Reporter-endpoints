from flask_restful import Resource
from flask import make_response,jsonify, request
from app.users.v1.models import User
from app.utilities.validators import isValidEmail,isValidPassword,isValidUsername,isValidSpace,isBlank,isNumber

class Registration(Resource):
    
    def post(self):
        data = request.get_json()
        email = data['email']
        password = data['password']
        firstname = data['firstname']
        lastname = data['lastname']
        username = data['username']
        phonenumber = data['phonenumber']
        
        if not isValidEmail(email) and not isValidSpace(email):
            return make_response(jsonify({
                'message':'Invalid email format'
                }), 400)
        if not isValidPassword(password):
            return make_response(jsonify({
                'message':'Password is a max of 8 characters and cannot be empty'
                }), 400)
        if  not isBlank(firstname) and not isValidUsername(firstname):
            return make_response(jsonify({
                'message':'Firstname cannot be empty and takes letters only'
                }), 400)  
        if not isBlank(lastname) and not isValidUsername(lastname): 
            return make_response(jsonify({
                'message':'Lastname cannot be empty and takes letters only'
                }), 400)
        if not isBlank(username) and not isValidUsername(username):
            return make_response(jsonify({
                'message':'Username cannot be empty and takes letters only'
                }),400)
        if not isNumber(phonenumber):
            return make_response(jsonify({
                'message':'Phonenumber should be in numerals'
                }),400)
        if not User.get_user_by_email(email):
            new_user = User(email=email, password=password, firstname=firstname, lastname=lastname,username=username,phonenumber=phonenumber)
            new_user.add_user()
            return make_response(jsonify({
             'message':'Your account has successfully been registered '
             }), 201)       
        else:
            return make_response(jsonify({
            'message':'email already exists. Use a different email'
            }), 409)       
                   
                                
class LogIn(Resource):
    def post(self):
        data = request.get_json()
        email = data['email']
        password = data['password']
        
        
        user = User.get_user_by_email(email)
        if not user:
            response = {
                'message' : 'wrong email address, use a different email'
            }
            return make_response(jsonify(response), 400)
        user_id = user.id
            
        if user and user.validate_password(password):
            user_token = user.generate_user_token(user_id)
            if user_token:
                response = {
                    'message' : 'Login Successful',
                }
                return make_response(jsonify(response), 200)
        else:
            response = {
                'message' : 'Invalid password, please try again'
            }
            return make_response(jsonify(response), 401)
        