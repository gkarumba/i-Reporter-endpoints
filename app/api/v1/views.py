from flask_restful import Resource
from flask import jsonify, make_response, request
from .models import Reports, db, incident
from app.utilities.validators import isValidUsername,isBlank,isImage,isVideo

class ReportLists(Resource):
    
    def post(self):
        data = request.get_json()
        createdBy = data['username']
        flag = data['flag']
        location = data['location']
        status = data['status']
        image = data['image']
        video = data['video']
        #comment = ['comment']
        
        if not isValidUsername(createdBy):
            return make_response(jsonify({
                'message':'Username takes letters only'
            }), 400)

        if not isBlank(createdBy):
            return make_response(jsonify({
                'message':'Username cannot be empty'
            }), 400)

        if not isBlank(flag):
            return make_response(jsonify({
                'message':'type cannot be empty'
            }), 400)

        if not isBlank(location):
            return make_response(jsonify({
                'message':'location cannot be empty'
            }),400)

        if not isBlank(status):
            return make_response(jsonify({
                'message':'status cannot be empty'
            }), 400)
        if not isImage(image):
            return make_response(jsonify({
                'message':'wrong image format. Use jpg/png/gif'
            }), 400)
        if not isVideo(video):
            return make_response(jsonify({
                'message':'wrong video format. Use mp4/mkv/3gp'
            }))

        new_report = Reports(createdBy, flag, location, status, image, video)
        incident.append(new_report)
        payload = new_report.serialize()
        return make_response(jsonify({
            "message": "Report has been created successfully",
            "data" : payload
        }), 201)

    def get(self):
        return make_response(jsonify({
            "Message":"OK",
            "data": [get_report.serialize() for get_report in incident] 
        }), 200)
    

class SingleReport(Resource,db):
    def __init__(self):
        self.mydb = db()

    def get(self,id):
        report = self.mydb.get_by_id(id)
        if report:
            return make_response(jsonify({
                "message":"OK",
                "data": report.serialize()
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
            report.status = data['status']
            report.image = data['image']
            report.video = data['video']
            report.comment = ['comment']
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






