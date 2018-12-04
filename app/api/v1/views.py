from flask_restful import Resource
from flask import jsonify, make_response, request

from .models import Reports, incident

class ReportLists(Resource):
    
    def post(self):
        data = request.get_json(force=True)
        
        createdBy = data['username']
        type = data['flag']
        location = data['location']
        status = data['statusMode']
       
        new_report = Reports(createdBy, type, location, status)
        incident.append(new_report)

        return make_response(jsonify({
            "message": "Report has been created successfully",
            "new report" : new_report.serialize()
        }), 201)

    def get(self):
        return make_response(jsonify({
            "Message":"OK",
            "Report": [get_report.serialize() for get_report in incident] 
        }), 200)
        
class SingleReport(Resource):
    
    def get(self,id):
        report = Reports().get_by_id(id)
        if report:
            return make_response(jsonify({
                "message":"OK",
                "report": report.serialize()
            }), 200)

        else: 
            response = {
                "message":"Invalid ID"
            }
            return make_response(jsonify(response), 400)

class EditReport(Resource, Reports):
    
    def put(self, id):
        report = Reports().get_by_id(id)
        data = request.get_json(force=True)
        if report:
            data = request.get_json()
            report.createdBy = data['username']
            report.type = data['flag']
            report.location = data['location']
            report.status = data['statusMode']
            return make_response(jsonify({
                "message":"Report edited successfully",
                "data": report.serialize()
            }), 201)
        else:
            return make_response(jsonify({
                "message": "ID invalid, no report found"
            }),400)

class DeleteReport(Resource, Reports):
    
    def delete(self, id):
            report = Reports().get_by_id(id)
            if report:
                incident.remove(report)
                return make_response(jsonify({
            "message":"Report has been deleted successfully"
        }), 200)
            else:
                return make_response(jsonify({
                "message":"ID invalid, no report found"
            }), 400)






