from datetime import datetime
from app.users.v1.database import ReportDB

db = ReportDB() 

class ReportIncident:
    """
      Class contains some of the methods used on reports table in the db
    """
    # def __init__(self,createdOn,username,flag_type,location,status,comments):
    #     self.createdOn = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    #     self.username = username
    #     self.flag_type = flag_type
    #     self.location = location
    #     self.status = status
    #     self.comments = comments

    def create_incident(self,username,flag_type,location,status,comments):
        """
        Method for generating new input to the reports list
        """
        payload ={
            "username": username,
            "flag_type": flag_type,
            "location":location,
            "status":status,
            "comments":comments
        }
        load_query = """INSERT INTO reports (username,flag_type,location,status,comments) VALUES(%s,%s,%s,%s,%s);"""
        tupl = (username,flag_type,location,status,comments)
        db.save_to_db(load_query,tupl)

        return payload

    def incident_list(self):
        """
        Gets all the reports 
        """
        query = """SELECT username,flag_type,location,status,comments,report_id FROM reports ORDER BY report_id ASC;"""
        respo = db.get_all(query)
        return respo

    def get_one_incident(self, report_id):
        load_query = """SELECT username,flag_type,location,status,comments,report_id FROM reports WHERE report_id={}""".format(report_id)
        respo = db.get_one(load_query)
        if not respo:
            return False
        return respo
        
    def update_incident(self,new_location,new_status,new_comments,report_id):
        payload = {
            'updated_location': new_location,
            'updated_status': new_status,
            'updated_comments': new_comments
        }
        load_query = """SELECT location,status,comments FROM reports WHERE report_id={}""".format(report_id)
        respo = db.get_one(load_query)
        if not respo:
            return False
        update_query = """UPDATE reports SET location='{}', status='{}', comments='{}' WHERE report_id={}""".format(new_location,new_status,new_comments, report_id)
        db.update_table_row(update_query)
        retrieve_query = """SELECT * FROM reports WHERE report_id={}""".format(report_id)
        response = db.get_one(retrieve_query)
        return response

    def delete_incident(self,report_id):
        load_query = """DELETE FROM reports WHERE report_id={}""".format(report_id)
        response = db.delete(load_query)
        retrieve_query = """SELECT * FROM reports WHERE report_id={}""".format(report_id)
        response = db.get_one(retrieve_query)
        return response
