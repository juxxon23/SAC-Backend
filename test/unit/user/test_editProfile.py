import unittest
from app import create_app


class TestEditProfile(unittest.TestCase):

    app = create_app()

    def test_edit_profile(self):
        client = self.app.test_client(self)
        rv = client.put('/signin', json={'document_u': '1094565445', 'name_u': 'juancho', 'lastname_u': 'mosquera', 'phone_u': '3124567',
                                         'city_u': 'Armenia', 'regional_u': 'quindio', 'center_u': 'Comercio y turismo'})
        json_data = rv.get_json()
        print('\n----------------------------------------------------------------------\n-----------------------------JSON CONTENT-----------------------------\n',
              json_data, '\n----------------------------------------------------------------------\n')
        statuscode = rv.status_code
        self.assertEqual(statuscode, 200)

    def test_edit_profile_error(self):
        client = self.app.test_client(self)
        rv = client.put('/signin', json={'document_u': '1094565445', 'name_u': 'ju', 'lastname_u': 'mosquera', 'phone_u': '3124567',
                                         'city_u': 'Armenia', 'regional_u': 'quindio', 'center_u': 'Comercio y turismo'})
        json_data = rv.get_json()
        print('\n----------------------------------------------------------------------\n-----------------------------JSON CONTENT-----------------------------\n',
              json_data, '\n----------------------------------------------------------------------\n')
        statuscode = rv.status_code

        list_keys = []
        for i in json_data['error']:
            list_keys.append(i)

        self.assertEqual(statuscode, 400)
        self.assertEqual(list_keys[0], 'name_u')
