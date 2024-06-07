"""
Для каждого поля и валидатора в эндпоинте /registration напишите юнит-тест,
который проверит корректность работы валидатора. Таким образом, нужно проверить, что существуют наборы данных,
которые проходят валидацию, и такие, которые валидацию не проходят.
"""

import unittest
from hw1_registration import app
import requests

class TestRegistration(unittest.TestCase):

    def test_null_fields(self):
        response = requests.post('http://localhost:5000/registration', data={})
        self.assertEqual(response.status_code , 400)
    
    def test_correct_fields(self):
        data = {
            'name': 'Andrey Kolchin',
            'email': 'an.kolchin.16@yandex.ru',
            'phone': 9826201196,
            'address': 'Sulimova 3/3, 174',
            'index': 620066
        }
        response = requests.post('http://localhost:5000/registration', data=data)
        self.assertEqual(response.status_code, 200)

    def test_name(self):
        names = [None, 'Andrew']
        for name in names:
            data = {
                'name': name,
                'email': 'an.kolchin.16@yandex.ru',
                'phone': 9826201196,
                'address': 'Sulimova 3/3, 174',
                'index': 620066
            }
            response = requests.post('http://localhost:5000/registration', data=data)

            with self.subTest():
                if not isinstance(name, str):
                    self.assertEqual(response.status_code, 400)
                else:
                    self.assertEqual(response.status_code, 200)
    
    def test_email(self):
        emails = ['aaaa', 'an.kolchin.16@yandex.ru']
        for i in range(len(emails)):
            data = {
                'name': 'Andrew',
                'email': emails[i],
                'phone': 9826201196,
                'address': 'Sulimova 3/3, 174',
                'index': 620066
            }
            response = requests.post('http://localhost:5000/registration', data=data)

            with self.subTest():
                if i == 0:
                    self.assertEqual(response.status_code, 400)
                else:
                    self.assertEqual(response.status_code, 200)

    def test_phone(self):
        phones = [123213, 9826201196]
        for i in range(len(phones)):
            data = {
                'name': 'Andrew',
                'email': 'an.kolchin.16@yandex.ru',
                'phone': phones[i],
                'address': 'Sulimova 3/3, 174',
                'index': 620066
            }
            response = requests.post('http://localhost:5000/registration', data=data)

            with self.subTest():
                if i == 0:
                    self.assertEqual(response.status_code, 400)
                else:
                    self.assertEqual(response.status_code, 200)

    def test_address(self):
        addresses = [None, 'Sulimova 3/3']
        for i in range(len(addresses)):
            data = {
                'name': 'Andrew',
                'email': 'an.kolchin.16@yandex.ru',
                'phone': 9826201196,
                'address': addresses[i],
                'index': 620066
            }
            response = requests.post('http://localhost:5000/registration', data=data)

            with self.subTest():
                if i == 0:
                    self.assertEqual(response.status_code, 400)
                else:
                    self.assertEqual(response.status_code, 200)

    def test_index(self):
        indexes = [1, 620066]
        for i in range(len(indexes)):
            data = {
                'name': 'Andrew',
                'email': 'an.kolchin.16@yandex.ru',
                'phone': 9826201196,
                'address': 'Sulimova 3/3, 174',
                'index': indexes[i]
            }
            response = requests.post('http://localhost:5000/registration', data=data)

            with self.subTest():
                if i == 0:
                    self.assertEqual(response.status_code, 400)
                else:
                    self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
