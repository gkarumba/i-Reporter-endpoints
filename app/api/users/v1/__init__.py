from flask import Blueprint
from flask_restful import Api
from .views import Registration, LogIn

user = Blueprint('userv1', __name__, url_prefix="/users/v1")

api = Api(user)

api.add_resource(Registration, '/register')
api.add_resource(LogIn,'/login')
