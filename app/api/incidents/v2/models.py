from datetime import datetime
from app.api.users.v1.database import ReportDB

db = ReportDB() 

class ReportIncident:
    """
      Class contains some of the methods used on reports table in the db
    """
    # def __init__(self,createdOn,createdBy,flag_type,location,status,flags):
    #     self.createdOn = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    #     self.username = username
    #     self.flag_type = flag_type
    #     self.location = location
    #     self.status = status
    #     self.comments = comments

    def create_incident(self,createdBy,flag_type,location,comments):
        """
        Method for generating new input to the reports list
        """
        payload ={
            "createdBy" : createdBy,
            "flag_type": flag_type,
            "location":location,
            "comments":comments
        }
        load_query = """INSERT INTO reports (createdBy,flag_type,location,comments) VALUES(%s,%s,%s,%s);"""
        tupl = (createdBy,flag_type,location,comments)
        db.save_to_db(load_query,tupl)
        return payload
        
    def check_if_admin(self):
        check_query = """ SELECT user_id FROM users WHERE user_id=(select min(user_id) from users);"""
        check_admin = db.get_one(check_query)
        if not check_admin:
            return False
        return check_admin
    
    def get_report_id(self):
        get_reportid_query = """SELECT report_id FROM reports WHERE report_id=(select max(report_id) from reports);"""
        response = db.get_one(get_reportid_query)
        if not response:
            return False
        return response

    def incident_list(self):
        """
        Gets all the reports 
        """
        query = """SELECT createdBy,flag_type,createdOn,location,status,comments,report_id FROM reports ORDER BY report_id ASC;"""
        respo = db.get_all(query)
        return respo

    def get_one_incident(self, report_id):
        load_query = """SELECT createdBy,flag_type,createdOn,location,status,comments,report_id FROM reports WHERE report_id={}""".format(report_id)
        respo = db.get_one(load_query)
        if not respo:
            return False
        return respo
        
    def update_location(self,new_location,report_id):
        load_query = """SELECT location FROM reports WHERE report_id={}""".format(report_id)
        respo = db.get_one(load_query)
        if not respo:
            return False
        update_query = """UPDATE reports SET location='{}' WHERE report_id={}""".format(new_location, report_id)
        db.update_table_row(update_query)
        retrieve_query = """SELECT * FROM reports WHERE report_id={}""".format(report_id)
        response = db.get_one(retrieve_query)
        return response

    def update_comment(self,new_comment,report_id):
        load_query = """SELECT comments FROM reports WHERE report_id={}""".format(report_id)
        respo = db.get_one(load_query)
        if not respo:
            return False
        update_query = """UPDATE reports SET comments='{}' WHERE report_id={}""".format(new_comment, report_id)
        db.update_table_row(update_query)
        retrieve_query = """SELECT * FROM reports WHERE report_id={}""".format(report_id)
        response = db.get_one(retrieve_query)
        return response

    def update_flag(self,new_flag,report_id):
        load_query = """SELECT flag_type FROM reports WHERE report_id={}""".format(report_id)
        respo = db.get_one(load_query)
        if not respo:
            return False
        update_query = """UPDATE reports SET flag_type='{}' WHERE report_id={}""".format(new_flag, report_id)
        db.update_table_row(update_query)
        retrieve_query = """SELECT * FROM reports WHERE report_id={}""".format(report_id)
        response = db.get_one(retrieve_query)
        return response
    
    def update_status(self,new_status,report_id):
        load_query = """SELECT status FROM reports WHERE report_id={}""".format(report_id)
        respo = db.get_one(load_query)
        if not respo:
            return False
        update_query = """UPDATE reports SET status='{}' WHERE report_id={}""".format(new_status, report_id)
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
