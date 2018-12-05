from flask import Blueprint
from flask_restful import Api

from app.users.v2.views import Registration, LogIn

users2 = Blueprint('users2', __name__, url_prefix="/users/v2")

api = Api(user2)

api.add_resource(SignUp, '/Registration')
api.add_resource(SignIn, '/LogIn')