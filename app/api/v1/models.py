from datetime import datetime

incident = []
class Reports():
   
    def __init__(self, username, flag, location, status):
        self.id = len(incident)+1
        self.createdOn = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.createdBy = username
        self.flag = flag
        self.location = location
        self.status = status

    def add_to_db(self):
        payload = {
            "id": self.id,
            "date_time": self.createdOn,
            "username": self.createdBy,
            "flag": self.flag,
            "location":self.location,
            "status":self.status
            }
        incident.append(payload)
        return payload

class db():     
    
    def get_by_id(self, id):
        for report in incident:
            if report.id == id:
                return report
    
    def serialize(self):
        return {
            "id": self.id,
            "date_time": self.createdOn,
            "username": self.createdBy,
            "flag": self.flag,
            "location":self.location,
            "status":self.status
            }
   
        



