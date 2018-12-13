import unittest
import json

from app.users.v1.database import ReportDB

db = ReportDB()

class LoginTestCase(unittest.TestCase):
    
    def setUp(self):
        self.test_app = create_app(config_name='testing_config')
        self.app = self.test_app.test_client()
        self.test_app.testing = True

        self.login_data = {
            'email' : 'hannibal@ymail.com',
            'password' : 'Zhunguoren'
        }
        self.register_data = {
            'password' : 'Zhunguoren',
            'email' : 'hannibal@ymail.com',
            'username' : 'lector',
            'firstname' : 'hannibal',
            'lastname' : 'psyco',
            'phonenumber' : '0728556699'
        }
        self.unregistered_data = {
            'email' : 'Duffy@ymail.com',
            'password' : 'Zhunguoren'
        }
        self.invalid_data = {
            'username' : 'lector',
            'password' : 'Zhunguoren'
        }

    def tearDown(self):
        db.drop_table()
    
    def test_registered_login(self):
        response = self.app.post('user/v2/register',data=json.dumps(self.register_data),content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        response1 = self.app.post('user/v2/login',data=json.dumps(self.data),content_type='application/json')
        result1 = json.loads(response1.data)
        self.assertEqual(response1.status_code,200)
        self.assertIn('Successfully logged in', str(result))

    def test_unregistered_login(self):
        response = self.app.post('user/v2/register',data=json.dumps(self.register_data),content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        response1 = self.app.post('user/v2/login',data=json.dumps(self.unregistered_data),content_type='application/json')
        result1 = json.loads(response1.data)
        self.assertEqual(response1.status_code,401)
        self.assertIn('incorrect login credentials. please enter details again', str(result))

    def test_invalid_data(self):
        response = self.app.post('user/v2/register',data=json.dumps(self.register_data),content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        response1 = self.app.post('user/v2/login',data=json.dumps(self.invalid_data),content_type='application/json')
        result1 = json.loads(response1.data)
        self.assertEqual(response1.status_code,400)
        self.assertIn('Invalid data, try again', str(result))

if __name__ == '__main__':
    unittest.main()
    