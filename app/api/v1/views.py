from flask_restful import Resource
from flask import jsonify, make_response, request

from models import Reports

class ReportLists(Resource, Reports):
    
    def __init__(self):
        self.db = Reports()

    def post(self):
        data = request.get_json()
        createdOn = data['reportedAt']
        createdBy = data['username']
        type = data['redflags_intervention']
        location = data['location']
        status = data['statusMode']

        resp = self.db.create_report(createdOn, createdBy, type, location, status)
        return make_response(jsonify({
            "message": "Report has been created successfully",
            "new report" : resp
        }), 201)