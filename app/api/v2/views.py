from flask_restful import Resource
from flask import make_response, jsonify, request
from app.utilities.validators import isValidUsername,isBlank
from app.api.v2.models import ReportIncident
from app.utilities.tokens import decode_token

report = ReportIncident()

class ReportList(Resource):
    def post(self):
        user_header = request.headers.get('Authorization')
        if not user_header:
            return make_response(jsonify({
                'message':'This is a Protected route. Please add a token to the header'
            }), 400)
        access_token = user_header.split(" ")[1]
        if not access_token:
            return make_response(jsonify({
                'message':'No token. Please put token in the Header'
            }), 400)
        
        user_id = decode_token(access_token)

        if isinstance(user_id, str):
            return make_response(jsonify({
                'message':'Invalid Token'
            }), 400)

        try: 
            data = request.get_json()
            username = data['username']
            flag_type = data['flag_type']
            location = data['location']
            status = data['status']
            comments = data['comments']
        except Exception:
            return make_response(jsonify({
                'message':'Invalid key field'
            }), 400)

        if not isBlank(username) and not isValidUsername(username):
            return make_response(jsonify({
                'message':'Username cannot be empty and takes letters only'
                }),400)
        if not isBlank(flag_type):
            return  make_response(jsonify({
                'message':'Flag_type cannot be blank'
            }), 400)
        if not isBlank(location):
            return  make_response(jsonify({
                'message':'Location cannot be blank'
            }), 400)
        if not isBlank(status):
            return  make_response(jsonify({
                'message':'Status cannot be blank'
            }), 400)
        if not isBlank(comments):
            return make_response(jsonify({
                'message':'Comments cannot be blank'
            }), 400)

        response = report.create_incident(username,flag_type,location,status,comments)

        return make_response(jsonify({
                'message':'Incident Created Successfully',
                'data': response
            }), 201)

    def get(self):
        user_header = request.headers.get('Authorization')
        if not user_header:
            return make_response(jsonify({
                'message':'This is a Protected route. Please add a token to the header'
            }), 400)
        access_token = user_header.split(" ")[1]
        if not access_token:
            return make_response(jsonify({
                'message':'No token. Please put token in the Header'
            }), 400)
        
        user_id = decode_token(access_token)

        if isinstance(user_id, str):
            return make_response(jsonify({
                'message':'Invalid Token'
            }), 400)

        resp = report.incident_list()
        if resp: 
            return make_response(jsonify({
                'message':'OK',
                'data': resp
            }), 200)
        return make_response(jsonify({
                'message':'No incident available'
            }), 400)

class EditReport(Resource):
    def put(self, id):
        user_header = request.headers.get('Authorization')
        if not user_header:
            return make_response(jsonify({
                'message':'This is a Protected route. Please add a token to the header'
            }), 400)
        access_token = user_header.split(" ")[1]
        if not access_token:
            return make_response(jsonify({
                'message':'No token. Please put token in the Header'
            }), 400)

        user_id = decode_token(access_token)

        if isinstance(user_id, str):
            return make_response(jsonify({
                'message':'Invalid Token'
            }), 400)

        new_incident = request.get_json()
        updated_location = new_incident['new_location']
        updated_status = new_incident['new_status']
        updated_comments = new_incident['new_comments']

        if not isBlank(updated_location):
            return  make_response(jsonify({
                'message':'New_Location cannot be blank'
            }), 400)
        if not isBlank(updated_status):
            return  make_response(jsonify({
                'message':'New_Status cannot be blank'
            }), 400)
        if not isBlank(updated_comments):
            return make_response(jsonify({
                'message':'New_Comments cannot be blank'
            }), 400)

        new_report = report.update_incident(updated_location,updated_status,updated_comments,id)
        if new_report:
            return make_response(jsonify({
                'message':'New Incident Updated',
                'data': new_report
            }), 201)
        else:
            return make_response(jsonify({
                'message':'New Incident failed to update. Invalid ID'
            }), 400)

class DeleteReport(Resource):
    def delete(self,id):
        user_header = request.headers.get('Authorization')
        if not user_header:
            return make_response(jsonify({
                'message':'This is a Protected route. Please add a token to the header'
            }), 400)
        access_token = user_header.split(" ")[1]
        if not access_token:
            return make_response(jsonify({
                'message':'No token. Please put token in the Header'
            }), 400)

        user_id = decode_token(access_token)

        if isinstance(user_id, str):
            return make_response(jsonify({
                'message':'Invalid Token'
            }), 400)

        del_report = report.delete_incident(id)
        if not del_report:
            return make_response(jsonify({
                'message':'Report has been deleted successfully'
            }), 200)
        else:
            return make_response(jsonify({
                'message':'ID invalid, no report found'
            }), 400)
