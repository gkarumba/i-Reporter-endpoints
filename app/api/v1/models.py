from datetime import datetime

incident = []
class Reports():
   
    def __init__(self, username, flag, location, status, image, video, comment):
        self.id = len(incident)+1
        self.createdOn = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.createdBy = username
        self.flag = flag
        self.location = location
        self.status = status
        self.image = image
        self.video = video
        self.comment = comment

    def serialize(self):
        return {
            "id": self.id,
            "date_time":self.createdOn,
            "username":self.createdBy,
            "flag":self.flag,
            "location":self.location,
            "status":self.status,
            "image":self.image,
            "video":self.video,
            "comment":self.comment
            }
        

class db():     
    
    def get_by_id(self, id):
        for report in incident:
            if report.id == id:
                return report
    
    def serialize(self):
        return {
            "id": self.id,
            "date_time":self.createdOn,
            "username":self.createdBy,
            "flag":self.flag,
            "location":self.location,
            "status":self.status,
            "image":self.image,
            "video":self.video,
            "comment":self.comment
            }
   
        



