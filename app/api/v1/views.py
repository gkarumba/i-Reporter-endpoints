from flask_restful import Resource
from flask import jsonify, make_response, request
from .models import Reports, incident, db
from app.utilities.validators import isValidUsername,isBlank

class ReportLists(Resource):
    
    def post(self):
        data = request.get_json()
        
        createdBy = data['username']
        type = data['type']
        location = data['location']
        status = data['status']
        
        if isValidUsername(createdBy) and isBlank(createdBy):
            if isBlank(type):
                if isBlank(location):
                    if isBlank(status):
                        new_report = Reports(createdBy, type, location, status)
                        incident.append(new_report)
                        return make_response(jsonify({
                            "message": "Report has been created successfully",
                            "new report" : new_report.serialize()}), 201)
                    else:
                        return make_response(jsonify({
                            'message':'status cannot be empty'}), 400)
                else:
                    return make_response(jsonify({
                        'message':'location cannot be empty'}),400)
            else:
                return make_response(jsonify({
                    'message':'type cannot be empty'}), 400)
        else:
            return make_response(jsonify({
                'message':'Username cannot be empty and takes letters only'}), 400)        
    def get(self):
        return make_response(jsonify({
            "Message":"OK",
            "Report": [get_report.serialize() for get_report in incident] 
        }), 200)
        
class SingleReport(Resource,db):
    def __init__(self):
        self.mydb = db()

    def get(self,id):
        report = self.mydb.get_by_id(id)
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

class EditReport(Resource, db):
    def __init__(self):
        self.mydb = db()

    def put(self, id):
        report = self.mydb.get_by_id(id)
        
        if report:
            data = request.get_json()
            report.createdBy = data['username']
            report.type = data['flag']
            report.location = data['location']
            report.status = data['statusmode']
            return make_response(jsonify({
                "message":"Report edited successfully",
                "data": report.serialize()
            }), 201)
        else:
            return make_response(jsonify({
                "message": "ID invalid, no report found"
            }),400)

class DeleteReport(Resource, db):
    def __init__(self):
        self.mydb = db()

    def delete(self, id):
            report = self.mydb.get_by_id(id)
            if report:
                incident.remove(report)
                return make_response(jsonify({
            "message":"Report has been deleted successfully"
        }), 200)
            else:
                return make_response(jsonify({
                "message":"ID invalid, no report found"
            }), 400)






