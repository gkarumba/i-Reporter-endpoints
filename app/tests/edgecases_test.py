import unittest
import json
#local imports
from app import create_app
# from app.users.v1.database import ReportDB as db

class TestEdgeCases(unittest.TestCase):
    """
        Class for the methods used in testing
    """
    def setUp(self):
        """
            Method for setting up the tests
        """
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
        self.check_status = {
            "username": "peter",
            "flag": "redflag",
            "location": "12.786,89.098",
            "status": "draft",
            "image": "image.png",
            "video": "video.mkv"
        }
        self.check_location = {
            "username": "peter",
            "flag": "redflag",
            "location": "PAC",
            "status": "resolved",
            "image": "image.png",
            "video": "video.mkv"
        }
        self.check_username = {
            "username": "12345",
            "flag": "redflag",
            "location": "12.786,89.098",
            "status": "resolved",
            "image": "image.png",
            "video": "video.mkv"
        }
        self.check_image = {
            "username": "Peter",
            "flag": "redflag",
            "location": "12.786,89.098",
            "status": "resolved",
            "image": "image",
            "video": "video.mkv"
        }
        self.check_video = {
            "username": "John",
            "flag": "redflag",
            "location": "12.786,89.098",
            "status": "resolved",
            "image": "image.png",
            "video": " "
        }

    
    # def tearDown(self):
        # db.drop_all()

    def test_invalid_email(self):
        """
            Method for testing the data passed on the email
        """
        response = self.app.post('users/v1/register',data=json.dumps(self.invalid_email),content_type='application/json')
        result = json.loads(response.data)
        print(result)
        self.assertEqual(response.status_code,400)
        self.assertIn('Invalid email format', str(result))

    def test_invalid_password(self):
        """
            Method for testing the data passed on the password
        """
        response = self.app.post('users/v1/register',data=json.dumps(self.invalid_password),content_type='application/json')
        result = json.loads(response.data)
        # import pdb; pdb.set_trace()
        self.assertEqual(response.status_code, 400)
        self.assertIn('Password is a max of 8 characters and cannot be empty',str(result))

    def test_blank_space(self):
        """
            Method for testing the emptiness of a key field
        """
        response = self.app.post('users/v1/register',data=json.dumps(self.blank_space),content_type='application/json')
        result = json.loads(response.data)
        # import pdb; pdb.set_trace()
        self.assertEqual(response.status_code,400)
        self.assertIn('Firstname cannot be empty and takes letters only',str(result))

    def test_check_integer(self):
        """
            Method for testing whether an element is an integer
        """
        response = self.app.post('users/v1/register',data=json.dumps(self.check_integer),content_type='application/json')
        result = json.loads(response.data)
        # import pdb; pdb.set_trace()
        self.assertEqual(response.status_code,400)
        self.assertIn('Phonenumber should be in numerals',str(result))
    
    def test_check_status(self):
        """Method to test the status format"""
        response = self.app.post('/api/v1/reports',data=json.dumps(self.check_status),content_type='application/json')
        result = json.loads(response.data)
        # import pdb; pdb.set_trace()
        self.assertEqual(response.status_code,400)
        self.assertIn('Use the correct status format',str(result))
    
    def test_check_username(self):
        """Method to test the username format"""
        response = self.app.post('/api/v1/reports',data=json.dumps(self.check_username),content_type='application/json')
        result = json.loads(response.data)
        # import pdb; pdb.set_trace()
        self.assertEqual(response.status_code,400)
        self.assertIn('Username takes letters only',str(result))

    def test_check_location(self):
        """Method to test the location format"""
        response = self.app.post('/api/v1/reports',data=json.dumps(self.check_location),content_type='application/json')
        result = json.loads(response.data)
        # import pdb; pdb.set_trace()
        self.assertEqual(response.status_code,400)
        self.assertIn('Use the correct location format',str(result))

    def test_check_image(self):
        """Method to test the image format"""
        response = self.app.post('/api/v1/reports',data=json.dumps(self.check_image),content_type='application/json')
        result = json.loads(response.data)
        # import pdb; pdb.set_trace()
        self.assertEqual(response.status_code,400)
        self.assertIn('wrong image format. Use jpg/png/gif',str(result))

    # def test_check_video(self):
    #     """Method to test the video format"""
    #     response = self.app.post('/api/v1/reports',data=json.dumps(self.check_video),content_type='application/json')
    #     result = json.loads(response.data)
    #     # import pdb; pdb.set_trace()
    #     self.assertEqual(response.status_code,400)
    #     self.assertIn('wrong video format. Use mp4/mkv/3gp',str(result))    


    

    # def tearDown(self):
    #     db.drop_all()

if __name__ == '__main__':
    unittest.main()