import unittest
from freezegun import freeze_time

from mod3.hello_word_with_day import app

class TestHelloWordWithDay(unittest.TestCase):
    weekdays = {
        1: 'понедельника',
        2: 'вторника',
        3: 'среды',
        4: 'четверга',
        5: 'пятницы',
        6: 'субботы',
        7: 'воскресенья',
    }
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_url = '/hello-world/'
    def test_can_get_correct_username_with_weekdate(self):
        username = 'username'
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertTrue(username in response_text)

    def test_cat_get_correct_weekdate(self):
        username = 'Хорошей среды'
        for i in range(1, 8):
            freezer = freeze_time(f'2024-01-{i}')
            freezer.start()
            response = self.app.get(self.base_url + username)
            response_text = response.data.decode().replace(username, '', 1)
            self.assertTrue(self.weekdays[i] in response_text)
            freezer.stop()


