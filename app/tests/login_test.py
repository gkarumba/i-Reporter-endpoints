import unittest
import json
#local imports
from app import create_app
from app.database.database import ReportDB

db = ReportDB()

class LoginTestCase(unittest.TestCase):
    """
        Class for the methods used in testing
    """
    def setUp(self):
    """
        Method for setting up the tests
    """
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

    
    def test_registered_login(self):
    """
        Method for testing whether a user is registered before login
    """
        response = self.app.post('/users/v2/registration',data=json.dumps(self.register_data),content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        response1 = self.app.post('/users/v2/login',data=json.dumps(self.login_data),content_type='application/json')
        result1 = json.loads(response1.data)
        # import pdb; pdb.set_trace()
        self.assertEqual(response1.status_code,200)
        self.assertIn(result1['message'],'Successfully logged in')

    def test_unregistered_login(self):
    """
        Method for testing whether a user is not registered before login
    """
        # response = self.app.post('/users/v2/registration',data=json.dumps(self.register_data),content_type='application/json')
        # result = json.loads(response.data)
        # self.assertEqual(response.status_code, 201)
        response = self.app.post('/users/v2/login',data=json.dumps(self.unregistered_data),content_type='application/json')
        # import pdb; pdb.set_trace()
        result = json.loads(response.data)
        # import pdb; pdb.set_trace()
        self.assertEqual(response.status_code,401)
        self.assertIn('incorrect login credentials. please enter details again', str(result))


    def test_invalid_data(self):
    """
        Method for checking the data passed during login
    """
        response = self.app.post('/users/v2/registration',data=json.dumps(self.register_data),content_type='application/json')
        result = json.loads(response.data)
        # import pdb; pdb.set_trace()
        self.assertEqual(response.status_code, 201)
        response1 = self.app.post('/users/v2/login',data=json.dumps(self.invalid_data),content_type='application/json')
        result1 = json.loads(response1.data)
        #import pdb; pdb.set_trace()
        self.assertEqual(response1.status_code, 400)
        self.assertIn(result1['message'], 'Invalid data, try again')

    def tearDown(self):
    """
        Method for destroying the tables after all tests have run
    """
        db.drop_table()
        
if __name__ == '__main__':
    unittest.main()
    