from app.users.v1.database import ReportDB

class ReportIncident:
    """
      Class contains some of the methods used on reports table in the db
    """
    def create_incident(self,createdby,flag,location,status,comments):
        """
        Method for generating new input to the reports list
        """
        payload ={
            "username": createdby,
            "flag_type": flag,
            "location":location,
            "status":status,
            "comments":comments
        }
        load_query = """INSERT INTO reports (username,flag_type,location,status,comments) VALUES(%s,%s,%s,%s);"""
        tupl = (username,flag_type,location,status,comments)
        ReportDB.save_to_db(load_query,tupl)

        return payload

    def report_list(self):
        """
        Gets all the reports 
        """
        query = """SELECT username,flag_type,location,status,report_id FROM reports ORDER BY report_id ASC;"""
        respo = ReportDB.get_all(query)
        return respo


    