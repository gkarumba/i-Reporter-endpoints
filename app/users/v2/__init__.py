from flask import Blueprint
from flask_restful import Api

from app.users.v2.views import Registration, LogIn

users2 = Blueprint('users2', __name__, url_prefix="/users/v2")

api = Api(users2)

api.add_resource(Registration, '/registration')
api.add_resource(LogIn, '/login')