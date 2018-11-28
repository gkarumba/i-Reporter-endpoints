from views import ReportList

from flask import Blueprint
from flask_restful import Api, Resource

version_one = Blueprint('api_v1', __name__, url_prefix='/api/v1')

api = Api(version_one)

api.add_resource(ReportList, '/reports')