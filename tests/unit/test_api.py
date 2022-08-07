import requests
import json
import unittest


def check_response(url_base):
    response = requests.get(url=url_base)
    return response.status_code


def check_api(ulr_base, data):
    # we're passing post json object
    # json.dumps() - convert python object into json string

    j_data = json.dumps(data)
    headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
    r = requests.get(url=ulr_base, data=j_data, headers=headers)
    return r.json()


class TestApi(unittest.TestCase):

    def setUp(self):
        self.url_base = 'http://127.0.0.1:5000/'
        self.url_api = 'http://127.0.0.1:5000/api/'
        self.data_1 = [100, 200, 1000, 1000, 1430, 0.5]
        self.data_0 = [2, 5, 30, 50, 90, 0.2]
        self.data_short = [2, 32, 5, 46, 76]

    def tearDown(self):
        self.url_base = ''
        self.data = []

    def test_connection(self):
        response = check_response(self.url_base)
        self.assertEqual(response, 200)

    def test_api_1(self):
        response = check_api(self.url_api, self.data_1)
        self.assertEqual(response, '1')

    def test_api_2(self):
        response = check_api(self.url_api, self.data_0)
        self.assertIsNot(response, '0')


