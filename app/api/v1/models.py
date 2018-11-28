incident = []

class Reports:
    
    def __init__(self):
        self.db = incident

    def create_report(self, createdOn, createdBy, type, location, status):
        data = {
            "id": len(self.db)+1,
            "reportedAt": createdOn,
            "userName": createdBy,
            "redflag_intervention": type,
            "locationName": location,
            "statusMode": status
        }
        self.db.append(report)
        return self.db
    
    def get_single_report(self,reportID):
        single_report = [repo for repo in self.db if repo['id'] == reportID]
        if single_report:
            return single_report
        else:
            return False
    