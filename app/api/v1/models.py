"""
    This model is for the Reports and it 
    defines all the methods to be used on a report
"""
from datetime import datetime

incident = [] #Stores the reports

class Reports():
    """
        Class contains some of the methods used on the Reports resource
    """
    def __init__(self,username,flag,location,status,image,video):
        """
            Method for instatiating the arguments used by a report
        """
        self.id = len(incident)+1
        self.createdOn = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.createdBy = username
        self.flag = flag
        self.location = location
        self.status = status
        self.image = image
        self.video = video

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
            }
        

class db():  
    """
        Contains some of the methods used by a report
    """
    def get_by_id(self, id):
        """
            Gets a report by its ID and returns the report
        """
        for report in incident:
            if report.id == id:
                return report
    
    def serialize(self):
        """
            Takes data and returns it in dictionary format
        """
        return {
            "id": self.id,
            "date_time":self.createdOn,
            "username":self.createdBy,
            "flag":self.flag,
            "location":self.location,
            "status":self.status,
            "image":self.image,
            "video":self.video,
            }
   
        



