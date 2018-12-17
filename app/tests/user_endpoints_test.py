import json
import unittest

from app import create_app
from app.api.users.v1.database import ReportDB

db = ReportDB()

class EndpointsTestCase(unittest.TestCase):

    def setUp(self):
        self.app_test = create_app(config_name='testing_config')
        self.app = self.app_test.test_client()
        self.app_test.testing = True

        self.post_data = {
            'createdBy' : '1',
            'flag_type' : 'redflag',
            'location' : 'Thika',
            'comments' : 'Power Trip'
        }
        self.edit_data = {
            'flag_type' : 'incident',
            'location' : 'K-west',
            'comments' : 'This is a bad report'
        }

        self.register_data = {
            'password' : 'Zhunguoren',
            'email' : 'hannibal@ymail.com',
            'username' : 'lector',
            'firstname' : 'hannibal',
            'lastname' : 'psyco',
            'phonenumber' : '0728556699'
        }
        
        self.login_data = {
            'password' : 'Zhunguoren',
            'email' : 'hannibal@ymail.com'
        }

        register = self.app.post('/users/v2/registration',data=json.dumps(self.register_data),content_type='application/json')
        log_in = self.app.post('/users/v2/login',data=json.dumps(self.login_data),content_type='application/json')
        response = json.loads(log_in.data)
        #print(log_in.data)
        self.token = json.loads(log_in.data)['token']
        # print(self.token)
        self.Authorization = {'Authorization':'Bearer '+ self.token}
        self.content_type = 'application/json'
        self.headers = {
            'content_type' : 'application/json',
            'Authorization' : self.Authorization,
            'Accept' : 'application/json'
        }
        #print(self.Authorization)

    def test_post(self):
        response = self.app.post('/api/v2/reports',data=json.dumps(self.post_data), headers=self.headers)
        # print(json.loads(self.post_data))
        result = json.loads(response.data)
        # print(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertIn(result['message'],'Incident Created Successfully')

    def test_get(self):
        self.app.post('/api/v2/reports',data=json.dumps(self.post_data),headers=self.headers)
        response = self.app.get('/api/v2/reports',data=json.dumps(self.post_data),headers=self.headers)
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(result['message'],'OK')

    def test_get_one(self):
        self.app.post('/api/v2/reports',data=json.dumps(self.post_data),headers=self.headers)
        response = self.app.get('/api/v2/reports/1',data=json.dumps(self.post_data),headers=self.headers)
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(result['message'],'OK')
        
    def test_edit(self):
        self.app.post('/api/v2/reports',data=json.dumps(self.post_data),headers=self.headers)
        response = self.app.post('/api/v2/reports/1',data=json.dumps(self.edit_data),headers=self.headers)
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertIn(result['message'],'New Incident Updated')

    def test_delete(self):
        self.app.post('/api/v2/reports',data=json.dumps(self.post_data),headers=dict(self.headers))
        response = self.app.delete('/api/v2/reports/1')
        result = json.loads(response.data)
        #import pdb; pdb.set_trace()
        self.assertEqual(response.status_code, 200)
        self.assertIn(result['message'],'Report has been deleted successfully')

    def tearDown(self):
        db.drop_table()
    
if __name__ == '__main__':
    unittest.main()