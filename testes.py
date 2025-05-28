import unittest
from app import app
import werkzeug


if not hasattr(werkzeug, '__version__'):
    werkzeug.__version__ = "mock-version"

class APITestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()

    def test_home_route(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "API is running"})

    def test_items_route(self):
        response = self.client.get('/items')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"items": ["item1", "item2", "item3"]})

    def test_protected_without_token(self):
        response = self.client.get('/protected')
        self.assertEqual(response.status_code, 401)
        self.assertIn("msg", response.json)
        self.assertEqual(response.json["msg"], "Missing Authorization Header")

if __name__ == '__main__':
    unittest.main()
