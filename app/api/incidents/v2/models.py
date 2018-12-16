from datetime import datetime
#local import
from app.database.database import ReportDB

db = ReportDB() 

class ReportIncident:
    """
        Class contains some of the methods used on reports table in the db
    """

    def create_incident(self,createdBy,flag_type,location,comments):
        """
            Method for adding a new report to the reports table
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
        
    def check_user_id(self,report_id):
        """
            Method for checking whether the logged in user_id matches the createdby in a report
        """
        check_query = """SELECT createdBy FROM reports WHERE report_id ='{}'""".format(report_id)
        response = db.get_one(check_query)
        if not response:
            return False
        return response

    def check_if_admin(self):
        """
            Method for checking if a user is an Admin
        """
        check_query = """ SELECT user_id FROM users WHERE user_id=(select min(user_id) from users);"""
        check_admin = db.get_one(check_query)
        if not check_admin:
            return False
        return check_admin
    
    def get_report_id(self):
        """
            Method for retrieving the report_id for the latest created report
        """
        get_reportid_query = """SELECT report_id FROM reports WHERE report_id=(select max(report_id) from reports);"""
        response = db.get_one(get_reportid_query)
        if not response:
            return False
        return response

    def incident_list(self,user_id):
        """
            Method for retrieving all the reports 
        """
        query = """SELECT createdBy,flag_type,createdOn,location,status,comments,report_id FROM reports WHERE createdby ='{}' ORDER BY report_id ASC;""".format(user_id)
        respo = db.get_all(query)
        return respo

    def get_one_incident(self, report_id):
        """
            Method for retrieving a specific report
        """
        load_query = """SELECT createdBy,flag_type,createdOn,location,status,comments,report_id FROM reports WHERE report_id={}""".format(report_id)
        respo = db.get_one(load_query)
        if not respo:
            return False
        return respo
        
    def update_location(self,new_location,report_id):
        """
            Method for updating the location
        """
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
        """
            Method for updating the comments
        """
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
        """
            Method for updating the flag_type
        """
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
        """
            Method for updating the status
        """
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
        """
            Method for deleting a specific report
        """
        load_query = """DELETE FROM reports WHERE report_id={}""".format(report_id)
        response = db.delete(load_query)
        retrieve_query = """SELECT * FROM reports WHERE report_id={}""".format(report_id)
        response = db.get_one(retrieve_query)
        return response
