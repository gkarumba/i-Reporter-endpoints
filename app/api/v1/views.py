from flask_restful import Resource
from flask import jsonify, make_response, request

from .models import Reports, incident

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

class EditReport(Resource, Reports):
    
    def __init__(self):
        self.db = Reports()

    def put(self, id):
        report_edit = self.db.get_by_id(id)
        if report_edit:
            data = request.get_json()
            new_createdOn = data['reportedAt']
            new_createdBy = data['username']
            new_type = data['redflags_intervention']
            new_location = data['location']
            new_status = data['statusMode']

            updated_report = self.db.edit_single_report(id, new_createdOn, new_createdBy,new_type, new_location, new_status)
            
            return make_response(jsonify({
                "message":"Report editted successfully",
                "data": updated_report
            }), 201)

class DeleteReport(Resource, Reports):
    
    def __init__(self):
        self.db = Reports()
    
    def delete(self, id):
            repo = self.db.get_single_report(id)
            if repo:
                incident.remove(repo[0])
                return make_response(jsonify({
            "message":"Report has been deleted successfully"
        }), 200)
            else:
                return make_response(jsonify({
                "message":"ID invalid, no report found"
            }), 400)






