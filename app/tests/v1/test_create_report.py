from app import create_app
import json
import unittest

class TestReportCreation(unittest.TestCase):

    def setUp(self):
        create_app().testing = True
        self.app  = create_app().test_client()
        self.data = {
            "id": 1,
            "reportedAt": "1500hrs",
            "username": "john",
            "redflags_intervention": "redflag",
            "location": "PAC",
            "statusMode": "resolved"
        }
        self.data1 = {
            "id": 1,
            "reportedAt": "1300hrs",
            "username": "peter",
            "redflags_intervention": "redflag",
            "location": "PAC",
            "statusMode": "resolved"
        } 
        self.data2 = {
            "reportedAt": "1300hrs",
            "username": "peter",
            "redflags_intervention": "redflag",
            "location": "PAC",
            "statusMode": "resolved"
        }
    
    def test_POST_create_report(self):
        response = self.app.post('/api/v1/reports', data=json.dumps(self.data), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('Report has been created successfully', str(result))

    def test_GET_report_list(self):
        self.app.post('/api/v1/reports', data=json.dumps(self.data), content_type='application/json')
        response = self.app.get('/api/v1/reports', data=json.dumps(self.data), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('OK', str(result))

    def test_GET_single_report(self):
        self.app.post('/api/v1/reports', data=json.dumps(self.data), content_type='application/json')
        response = self.app.get('/api/v1/reports/1', data=json.dumps(self.data), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('OK', str(result))

    def test_PUT_edit_report(self):
        self.app.post('/api/v1/reports', data=json.dumps(self.data), content_type='application/json')
        response = self.app.put('api/v1/reports/1/edit', data=json.dumps(self.data1), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('Report editted successfully', str(result))

    #def test_DELETE_remove_report(self):
        #self.app.post('/api/v1/reports', data=json.dumps(self.data), content_type='application/type')
        #response = self.app.delete('/api/v1/reports/1')
        #result = json.loads(response.data)
        #self.assertEqual(response.status_code, 200)
        #self.assertIn('Report has been deleted successfully', str(result))

    

