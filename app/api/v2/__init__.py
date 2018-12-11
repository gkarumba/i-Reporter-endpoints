from flask import Blueprint
from flask_restful import Api
from app.api.v2.views import ReportList

version_two = Blueprint('api_v2',__name__, url_prefix='/api/v2')

api = Api(version_two)

api.add_resource(ReportList, '/reports')