from datetime import datetime

incident = []
class Reports():
   
    def __init__(self,id,createdOn, username=None,flag=None,location=None,statusmode=None):
        self.id = len(incident)+1
        self.createdOn = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.createdBy = username
        self.type = flag
        self.location = location
        self.status = statusmode
    def serialize(self):
        return {
            "id": self.id,
            "date_time": self.createdOn,
            "username": self.createdBy,
            "flag": self.type,
            "location":self.location,
            "statusmode":self.status
        }

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
            "flag": self.type,
            "location":self.location,
            "statusmode":self.status
        }
   
        



