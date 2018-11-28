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
        self.db.append(data)
        return self.db
    
    def get_report_list(self):
        return self.db
    
    def get_single_report(self,reportID):
        single_report = [repo for repo in self.db if repo['id'] == reportID]
        if single_report:
            return single_report
        else:
            return False

    def get_by_id(self, ID):
        get_id = [get_id for get_id in self.db if get_id['id'] == ID]
        if get_id:
            return True
        else: 
            return False

    def edit_single_report(self, reportID, new_createdOn, new_createdBy, new_type, new_location, new_status):
        edit_report = [repo for repo in self.db if repo['id'] == reportID]
        if edit_report:
            edit_report[0]['reportedAt'] = new_createdOn
            edit_report[0]['userName'] = new_createdBy
            edit_report[0]['redflag_intervention'] = new_type
            edit_report[0]['locationName'] = new_location
            edit_report[0]['statusMode'] = new_status
        
            return edit_report[0]
        else:
            return "Error no report found"