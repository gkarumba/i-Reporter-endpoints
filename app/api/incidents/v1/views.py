from flask_restful import Resource
from flask import jsonify, make_response, request
from .models import Reports, incident,db
from app.utilities.validators import is_valid_username,is_blank,is_image,is_video,is_status,is_location,is_flag

class ReportLists(Resource):
    """
        Class for creating a report and getting all the reports created
    """
    def post(self):
        """
            POST method for creating a new report
        """
        data = request.get_json()
        createdBy = data['username']
        flag = data['flag']
        location = data['location']
        status = data['status']
        image = data['image']
        video = data['video']
        #comment = ['comment']

        
        if not is_valid_username(createdBy):
            return make_response(jsonify({
                'message':'Username takes letters only'
            }), 400)

        if not is_blank(createdBy):
            return make_response(jsonify({
                'message':'Username cannot be empty'
            }), 400)

        if not is_flag(flag):
            return make_response(jsonify({
                'message':'type cannot be empty'
            }), 400)

        if not is_location(location):
            return make_response(jsonify({
                'message':'Use the correct location format'
            }),400)

        if not is_status(status):
            return make_response(jsonify({
                'message':'Use the correct status format'
            }), 400)
        if not is_image(image):
            return make_response(jsonify({
                'message':'wrong image format. Use jpg/png/gif'
            }), 400)
        if not is_video(video):
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
        """
            GET method for getting all the reports created
        """
        return make_response(jsonify({
            "Message":"OK",
            "data": [get_report.serialize() for get_report in incident] 
        }), 200)
    

class SingleReport(Resource,db):
    """
        Class for retrieving one report 
    """
    def __init__(self):
        self.mydb = db()

    def get(self,id):
        """
            GET method for retrieving a single report by its ID
        """
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
    """
        Class for editing a report
    """
    def __init__(self):
        self.mydb = db()

    def put(self, id):
        """
            PUT method for editing a single report
        """
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
    """
        Class for deleting a report
    """
    def __init__(self):
        self.mydb = db()

    def delete(self, id):
        """
            DELETE method for deleting a single report by its ID
        """
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






