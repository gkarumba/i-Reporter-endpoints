import unittest
import json

from app import create_app
from app.users.v1.database import ReportDB as db

class RegistrationTestCase(unittest.TestCase):

    def setUp(self):
        self.test_app = create_app(config_name='testing_config')
        self.app = self.test_app.test_client()
        self.test_app.testing = True

        self.data = {
            'password' : 'Zhunguoren',
            'email' : 'hannibal@ymail.com',
            'username' : 'lector',
            'firstname' : 'hannibal',
            'lastname' : 'psyco',
            'phonenumber' : '0728556699'
        }

        self.data2 = {
            'password' : 'Meiguoren',
            'email' : 'hannibal@ymail.com',
            'username' : 'lector',
            'firstname' : 'hannibal',
            'lastname' : 'psyco',
            'phonenumber' : '0728556699'
        }

    def tearDown(self):
        db.drop_table()

    def test_registration(self):
        response = self.app.post('users/v2/registration',data=json.dumps(self.data),content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('Your account has successfully been registered',str(result))

    def test_already_registered(self):
        response = self.app.post('users/v2/registration',data=json.dumps(self.data),content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        response1 = self.app.post('users/v2/registration',data=json.dumps(self.data2),content_type='application/json')
        result1 = json.loads(response1.data)
        self.assertEqual(response1.status_code, 409)
        self.assertIn('email already exists. Use a different email',str(result))
    
if __name__ == '__main__':
    unittest.main()