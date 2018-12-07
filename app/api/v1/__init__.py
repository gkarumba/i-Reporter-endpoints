from flask import Blueprint
from flask_restful import Api, Resource
#local imports
from .views import ReportLists, SingleReport, EditReport, DeleteReport

version_one = Blueprint('api_v1', __name__, url_prefix='/api/v1')

api = Api(version_one)

api.add_resource(ReportLists, '/reports')
api.add_resource(SingleReport, '/reports/<int:id>')
api.add_resource(EditReport, '/reports/<int:id>/edit')
api.add_resource(DeleteReport, '/reports/<int:id>')