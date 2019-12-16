from app import app
import requests
import unittest


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_count_recipes(self):
        expected = {'response': {'Салат «Русский»': 1}}
        req = requests.post('http://localhost:5000/recipes', json={"огурец": 3, 'мясо': 500})
        assert req.json() == expected

    def test_count_recipes1(self):
        expected = {'response': {'Салат «Ленинградский»': 1, 'Салат «Русский»': 2}}
        req = requests.post('http://localhost:5000/recipes', json={"огурец": 12,
                                                                   'мясо': 500,
                                                                   'картофель': 30})
        assert req.json() == expected

    def test_count_recipes2(self):
        expected = {'response': {'Салат «Ленинградский»': 1, 'Салат «Русский»': 2, 'Салат с рыбой и овощами': 2}}
        req = requests.post('http://localhost:5000/recipes', json={"огурец": 12,
                                                                   'мясо': 500,
                                                                   'картофель': 30,
                                                                   'рыба': 1000,
                                                                   'яйцо': 20})
        assert req.json() == expected

    def test_count_recipes3(self):
        expected = {'response': {}}
        req = requests.post('http://localhost:5000/recipes', json={"картофель": 6, 'мясо': 400})
        assert req.json() == expected


if __name__ == '__main__':
    unittest.main()
