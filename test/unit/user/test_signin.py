import unittest
from app import create_app


class TestSignin(unittest.TestCase):
    app = create_app()

    # Successfully registered 
    def test_signin_successfully(self):
        client = self.app.test_client(self)
        rv = client.post('/signin', json={'document_u': '10945654468',
                                         'email_inst': 'pedro@misena.edu.co', 'password_u': '1234567890'})
        json_data = rv.get_json()
        print('\n----------------------------------------------------------------------\n-----------------------------JSON CONTENT-----------------------------\n',
              json_data, '\n----------------------------------------------------------------------\n')
        statuscode = rv.status_code
        self.assertEqual(statuscode, 200)

    # sign up failed
    def test_signin_error(self):
        client = self.app.test_client(self)
        rv = client.post ('/signin', json={'document_u': '1091094565446',
                                         'email_inst': 'pe@gmail.com', 'password_u': '1234567890'})
        json_data = rv.get_json()
        print ('\n----------------------------------------------------------------------\n-----------------------------JSON CONTENT-----------------------------\n',
              json_data, '\n----------------------------------------------------------------------\n')
        statuscode = rv.status_code
        list_keys = []
        for i in json_data['error'].keys():
            list_keys.append(i)
        self.assertEqual(statuscode, 400)
        self.assertEqual(list_keys[0], 'email_inst')