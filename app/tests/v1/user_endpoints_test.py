import json
import unittest

from app import create_app
from app.users.v1.database import ReportDB

db = ReportDB()

class EndpointsTestCase(unittest.TestCase):

    def setUp(self):
        self.app_test = create_app(config_name='testing_config')
        self.app = self.app_test.test_client()
        self.app_test.testing = True

        self.post_data = {
            'username' : 'john',
            'flag_type' : 'incident',
            'location' : 'KANGEMI',
            'status' : 'rejected',
            'comments' : 'This is a good report'
        }
        self.edit_data = {
            'username' : 'peter',
            'flag_type' : 'incident',
            'location' : 'K-west',
            'status' : 'draft',
            'comments' : 'This is a bad report'
        }

    def tearDown(self):
        db.drop_table()
    
    def test_post(self):
        response = self.app.post('api/v2/reports',data=json.dumps(self.post_data),content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('Incident Created Successfully',str(result))

    def test_get(self):
        self.app.post('api/v2/reports',data=json.dumps(self.post_data),content_type='application/json')
        response = self.app.get('api/v2/reports',data=json.dumps(self.post_data),content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('OK',str(result))

    # def test_get_one(self):
    #     self.app.post('api/v2/reports',data=json.dumps(self.post_data),content_type='application/json')
    #     response = self.app.get('api/v2/reports/1',data=json.dumps(self.post_data),content_type='application/json')
    #     result = json.loads(response.data)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertIn('OK',str(result))
        

    def test_edit(self):
        self.app.post('api/v2/reports',data=json.dumps(self.post_data),content_type='application/json')
        response = self.app.post('api/v2/reports/1',data=json.dumps(self.edit_data),content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('New Incident Updated',str(result))

    def test_delete(self):
        self.app.post('api/v2/reports',data=json.dumps(self.post_data),content_type='application/json')
        response = self.app.delete('api/v2/reports/1')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Report has been deleted successfully',str(result))


if __name__ == '__main__':
    unittest.main()