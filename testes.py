import unittest
from app import app
import werkzeug


if not hasattr(werkzeug, '__version__'):
    werkzeug.__version__ = "mock-version"

class APITestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Criação do cliente de teste
        cls.client = app.test_client()

    def test_post_not_allowed_items(self):
        response = self.client.post('/items')
        self.assertEqual(response.status_code, 405)

    def test_404_route(self):
        response = self.client.get('/rota-que-nao-existe')
        self.assertEqual(response.status_code, 404)

    def test_get_items_content(self):
        response = self.client.get('/items')
        self.assertEqual(response.status_code, 200)
        self.assertIn("item1", response.json["items"])

if __name__ == '__main__':
    unittest.main()