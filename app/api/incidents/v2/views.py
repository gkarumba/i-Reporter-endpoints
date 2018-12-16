from flask_restful import Resource
from flask import make_response, jsonify, request
from app.utilities.validators import is_valid_username,is_blank,is_status,is_location
from app.api.incidents.v2.models import ReportIncident
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
            }),400)

        try: 
            data = request.get_json()
            flag_type = data['flag_type']
            location = data['location']
            comments = data['comments']
        except Exception:
            return make_response(jsonify({
                'message':'Invalid key field'
            }),400)

        if not is_blank(flag_type):
            return  make_response(jsonify({
                'message':'Flag_type cannot be _blank'
            }),400)
        if not is_blank(location) or not is_location(location):
            return  make_response(jsonify({
                'message':'Location cannot be _blank.Use valid location format(lat,long)'
            }),400)
        if not is_blank(comments):
            return make_response(jsonify({
                'message':'Comments cannot be _blank'
            }),400)
 
        if user_id != 1:
            createdBy = user_id
            response = report.create_incident(createdBy,flag_type,location,comments)
            report_id = report.get_report_id()
            if response:
                return make_response(jsonify({
                    'message':'Incident Created Successfully',
                    'CreatedBy': createdBy,
                    'report_id' : report_id['report_id']
                    }),201)
            else:
                return make_response(jsonify({
                    'message':'Invalid report ID, no report found'
                }),404)
        return make_response(jsonify({
            'message':'Admin cannot post',
        }), 400)

    def get(self):
        user_header = request.headers.get('Authorization')
        if not user_header:
            return make_response(jsonify({
                'message':'This is a Protected route. Please add a token to the header'
            }),400)
        access_token = user_header.split(" ")[1]
        if not access_token:
            return make_response(jsonify({
                'message':'No token. Please put token in the Header'
            }),400)
        
        user_id = decode_token(access_token)

        if isinstance(user_id, str):
            return make_response(jsonify({
                'message':'Invalid Token'
            }),400)
        
        resp = report.incident_list()
        if resp: 
            return make_response(jsonify({
                'message':'OK',
                'data': resp
            }),200)
        else:
            return make_response(jsonify({
                'message':'Invalid report ID, no report found'
            }),404)

class GetSingleReport(Resource):
    def get(self,id):
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

        response  = report.get_one_incident(id)
        if response:
            return make_response(jsonify({
                'message':'OK',
                'data': response
            }),200)
        else:
            return make_response(jsonify({
                'message':'Invalid report ID, no report found'
            }),404)
    
class EditLocation(Resource):
    def patch(self,id):
        user_header = request.headers.get('Authorization')
        if not user_header:
            return make_response(jsonify({
                'message':'This is a Protected route. Please add a token to the header'
            }),400)
        access_token = user_header.split(" ")[1]
        if not access_token:
            return make_response(jsonify({
                'message':'No token. Please put token in the Header'
            }),400)

        user_id = decode_token(access_token)

        if isinstance(user_id, str):
            return make_response(jsonify({
                'message':'Invalid Token'
            }),400)

        try:
            data = request.get_json()
            updated_location = data['new_location']
        except Exception:
            return make_response(jsonify({
                'message':'Invalid Key Field'
            }),400)
        if not is_blank(updated_location):
            return make_response(jsonify({
                'message':'new_location cannot be empty'
            }),400)

        if user_id != 1:
            new_report = report.update_location(updated_location,id)
            if new_report:
                return make_response(jsonify({
                        'message':'Report has been edited successfully',
                        'report': new_report
                    }),200)
            else:
                return make_response(jsonify({
                    'message':'Invalid report ID, no report found'
                }),404)
        return make_response(jsonify({
            'message':'Admin can only edit the status'
        }),400)

class EditComment(Resource):
    def patch(self,id):
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
            }),400)
        try:
            data = request.get_json()
            updated_comment = data['new_comment']
        except Exception:
            return make_response(jsonify({
                'message':'Invalid Key Field'
            }),400)
        
        if not is_blank(updated_comment):
            return make_response(jsonify({
                'message':'new_comment cannot be empty'
            }),400)

        if user_id != 1:
            new_report = report.update_comment(updated_comment,id)
            if new_report:
                return make_response(jsonify({
                    'message':'Report has been edited successfully',
                    'report': new_report
                }),200) 
            else:
                return make_response(jsonify({
                    'message':'Invalid report ID, no report found'
                }),404)
        return make_response(jsonify({
            'message':'Admin can only edit the status'
        }),400)     
           
class Editflag(Resource):
    def patch(self,id):
        user_header = request.headers.get('Authorization')
        if not user_header:
            return make_response(jsonify({
                'message':'This is a Protected route. Please add a token to the header'
            }),400)
        access_token = user_header.split(" ")[1]
        if not access_token:
            return make_response(jsonify({
                'message':'No token. Please put token in the Header'
            }),400)

        user_id = decode_token(access_token)

        if isinstance(user_id, str):
            return make_response(jsonify({
                'message':'Invalid Token'
            }),400)
        try:
            data = request.get_json()
            updated_flag = data['new_flag']
        except Exception:
            return make_response(jsonify({
                'message':'Invalid Key Field'
            }),400)
        if not is_blank(updated_flag):
            return make_response(jsonify({
                'message':'new_flag cannot be empty'
            }),400)
        check_user = report.check_if_admin()
        if user_id != 1:
            new_report = report.update_flag(updated_flag,id)
            if new_report:
                return make_response(jsonify({
                        'message':'Report has been edited successfully',
                        'report': new_report
                    }),200)
            else:
                return make_response(jsonify({
                    'message':'Invalid report ID, no report found'
                }),404)
        return make_response(jsonify({
            'message':'Admin can only edit the status'
        }),400)


class DeleteReport(Resource):
    def delete(self,id):
        user_header = request.headers.get('Authorization')
        if not user_header:
            return make_response(jsonify({
                'message':'This is a Protected route. Please add a token to the header'
            }),400)
        access_token = user_header.split(" ")[1]
        if not access_token:
            return make_response(jsonify({
                'message':'No token. Please put token in the Header'
            }),400)

        user_id = decode_token(access_token)

        if isinstance(user_id, str):
            return make_response(jsonify({
                'message':'Invalid Token'
            }),400)

        if user_id != 1:
            del_report = report.delete_incident(id)
            if not del_report:
                return make_response(jsonify({
                    'message':'Report has been deleted successfully'
                }),200)
            else:
                return make_response(jsonify({
                    'message':'Invalid report ID, no report found'
                }),404)
        return make_response(jsonify({
            'message':'Admin can only edit the status'
        }),400)
            
class EditStatus(Resource):
    def patch(self,id):
        user_header = request.headers.get('Authorization')
        if not user_header:
            return make_response(jsonify({
                'message':'This is a Protected route. Please add a token to the header'
            }),400)
        access_token = user_header.split(" ")[1]
        if not access_token:
            return make_response(jsonify({
                'message':'No token. Please put token in the Header'
            }),400)

        user_id = decode_token(access_token)

        if isinstance(user_id, str):
            return make_response(jsonify({
                'message':'Invalid Token'
            }),400)
        
        if user_id == 1:
            try:
                data = request.get_json()
                updated_status = data['new_status']
            except Exception:
                return make_response(jsonify({
                'message':'Invalid Key Field'
            }), 400)
            if not is_blank(updated_status) or not is_status(updated_status):
                return make_response(jsonify({
                    'message':'new_status cannot be empty,use the valid status'
                }),400)
            new_status = report.update_status(updated_status,id)
            if new_status:
                return make_response(jsonify({
                    'message':'Status change successful',
                    'report': new_status
                }),200)
            return make_response(jsonify({
                'message':'Invalid report ID, no report found'
            }),404)
            
        return make_response(jsonify({
            'message':'user is not allowed to edit status'
        }),400)
