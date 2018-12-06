from datetime import datetime

incident = []
class Reports():
   
    def __init__(self,id=None,createdOn=None,username=None,type=None,location=None,status=None):
        self.id = len(incident)+1
        self.createdOn = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.createdBy = username
        self.type = type
        self.location = location
        self.status = status
    
    def serialize(self):
        return {
            "id": self.id,
            "date_time": self.createdOn,
            "username": self.createdBy,
            "type": self.type,
            "location":self.location,
            "status":self.status
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
            "type": self.type,
            "location":self.location,
            "status":self.status
        }
   
        



