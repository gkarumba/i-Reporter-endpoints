from flask import Blueprint
from flask_restful import Api
from app.api.incidents.v2.views import ReportList,EditLocation,DeleteReport,GetSingleReport,EditComment,Editflag,EditStatus

version_two = Blueprint('api_v2',__name__, url_prefix='/api/v2')

api = Api(version_two)

api.add_resource(ReportList,'/reports')
api.add_resource(EditLocation,'/reports/location/<int:id>')
api.add_resource(DeleteReport,'/reports/<int:id>')
api.add_resource(GetSingleReport,'/reports/<int:id>')
api.add_resource(EditComment,'/reports/comment/<int:id>')
api.add_resource(Editflag,'/reports/flag/<int:id>')
api.add_resource(EditStatus,'/reports/status/<int:id>')