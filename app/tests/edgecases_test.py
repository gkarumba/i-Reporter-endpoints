import unittest
import json
from app import create_app
# from app.users.v1.database import ReportDB as db

class TestEdgeCases(unittest.TestCase):

    def setUp(self):

        create_app().testing = True
        self.app  = create_app().test_client()

        self.invalid_email = {
        'email' : 'gmail.com ',
        'password' : 'novascotia',
        'firstname' : 'Rashid',
        'lastname' : 'Al Khalifa',
        'username' : 'Baghdad',
        'phonenumber' : '0728556699'
        }
        self.invalid_password = {
        'email' : 'iraq@gmail.com',
        'password' : 'nu',
        'firstname' : 'Rashid',
        'lastname' : 'Al Khalifa',
        'username' : 'Baghdad',
        'phonenumber' : '0728556699'
        }
        self.blank_space = {
        'email' : 'iraq@gmail.com',
        'password' : 'novascotia',
        'firstname' : ' ',
        'lastname' : 'Al Khalifa',
        'username' : 'Baghdad',
        'phonenumber' : '0728556699'
        }
        self.check_integer = {
        'email' : 'iraq@gmail.com',
        'password' : 'novascotia',
        'firstname' : 'Rashid',
        'lastname' : 'Al Khalifa',
        'username' : '12345',
        'phonenumber' : 'number'
        }
    
    # def tearDown(self):
        # db.drop_all()

    def test_invalid_email(self):
        response = self.app.post('users/v1/register',data=json.dumps(self.invalid_email),content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(response.status_code,400)
        self.assertIn('Invalid email format', str(result))

    def test_invalid_password(self):
        response = self.app.post('users/v1/register',data=json.dumps(self.invalid_password),content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('Password is a max of 8 characters and cannot be empty',str(result))

    def test_blank_space(self):
        response = self.app.post('users/v1/register',data=json.dumps(self.blank_space),content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(response.status_code,400)
        self.assertIn('Firstname cannot be empty and takes letters only',str(result))

    def test_check_integer(self):
        response = self.app.post('users/v1/register',data=json.dumps(self.check_integer),content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(response.status_code,400)
        self.assertIn('Phonenumber should be in numerals',str(result))

if __name__ == '__main__':
    unittest.main()