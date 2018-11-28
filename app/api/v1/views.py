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

    def get(self):
        resp = self.db.get_report_list()
        return make_response(jsonify({
            "Message":"OK",
            "Report": resp 
        }), 200)
        
class SingleReport(Resource, Reports):
    
    def __init__(self):
        self.db = Reports()

    def get(self,id):
        single_report = self.db.get_single_report(id)
        if single_report:
            return make_response(jsonify({
                "message":"OK",
                "report": single_report 
            }), 200)

        else: 
            response = {
                "message":"Invalid ID"
            }
            return make_response(jsonify(response), 400)
