import unittest
from app import create_app

# python -m unittest test.unit.user.test_login
class TestLogin(unittest.TestCase):

    app = create_app()

    # Check for status code
    def test_access(self):
        client = self.app.test_client(self)
        rv = client.post('/login', json={
            'document_u': '1094999999', 'password_u': 'pass1234'
        })
        json_data = rv.get_json()
        print('\n----------------------------------------------------------------------\n-----------------------------JSON CONTENT-----------------------------\n',
              json_data, '\n----------------------------------------------------------------------\n')
        statuscode = rv.status_code
        self.assertEqual(statuscode, 203)



