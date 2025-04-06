import unittest
from app import app

class WebTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_task_post(self):
        response = self.client.post('/task', json={'message': 'test'})
        self.assertEqual(response.status_code, 202)

if __name__ == '__main__':
    unittest.main()
