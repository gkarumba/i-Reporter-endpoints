import json
import unittest
#local import
from app import create_app

class TestReportCreation(unittest.TestCase):
    """
        Class for Testing the Report endpoints
    """

    def setUp(self):
        """
            Initialize the app and define the 
            variables to be used in the tests 
        """
        create_app().testing = True
        self.app  = create_app().test_client()
        self.data = {
            "username": "john",
            "flag": "redflag",
            "location": "PAC",
            "status": "resolved",
            "image": "image.png",
            "video": "video.mkv"
        }
        self.data1 = {
            "username": "peter",
            "flag": "redflag",
            "location": "PAC",
            "status": "resolved",
            "image": "image.png",
            "video": "video"
        } 
        # self.data2 = {
        #     "username": "peter",
        #     "flag": "redflag",
        #     "location": "PAC",
        #     "status": "resolved"
        #     "image": "image.png",
        #     "video": "video"
        # }
    
    def test_POST_create_report(self):
        """
            Test the API if it can create a report using the POST method
        """
        response = self.app.post('/api/v1/reports', data=json.dumps(self.data), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('Report has been created successfully', str(result))

    def test_GET_report_list(self):
        """
            Test the API if it can retrieve all the reports using the GET method
        """
        self.app.post('/api/v1/reports', data=json.dumps(self.data), content_type='application/json')
        response = self.app.get('/api/v1/reports', data=json.dumps(self.data), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('OK', str(result))

    def test_GET_single_report(self):
        """
            Test the API if it can get a single report using the GET method
        """
        self.app.post('/api/v1/reports', data=json.dumps(self.data), content_type='application/json')
        response = self.app.get('/api/v1/reports/1', data=json.dumps(self.data), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('OK', str(result))

    def test_PUT_edit_report(self):
        """
            Test the API if it can edit a report using the PUT method
        """
        self.app.post('/api/v1/reports', data=json.dumps(self.data), content_type='application/json')
        response = self.app.put('api/v1/reports/1/edit', data=json.dumps(self.data1), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('Report edited successfully', str(result))

    def test_DELETE_report(self):
        """
            Test the API if it can delete a report using the DELETE method
        """
        self.app.post('/api/v1/reports', data=json.dumps(self.data), content_type='application/json')
        response = self.app.delete('/api/v1/reports/1')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Report has been deleted successfully', str(result))

    

