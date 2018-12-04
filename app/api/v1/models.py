from datetime import datetime

incident = []
class Reports:
    report_id = 1
    def __init__(self, username=None,flag=None,location=None,status=None):
        self.id = Reports.report_id,
        self.createdOn = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.createdBy = username
        self.type = flag
        self.location = location
        self.status = status

        Reports.report_id += 1
    
    def get_by_id(self, ID):
        for get_id in incident:
            if get_id.id == ID:
                return get_id
        

    def serialize(self):
        return {
            "id": self.id,
            "date_time": self.createdOn,
            "username": self.createdBy,
            "flag": self.type,
            "location":self.location,
            "status": self.status
        }
   
        



