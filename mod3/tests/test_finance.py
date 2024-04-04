import unittest
from mod2.app2 import app, storage


class TestFinance(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        cls.app = app.test_client()
        cls.storage = storage

    def setUp(self):
        self.storage = storage
        self.storage.clear()

    #Этот метод заполняет storage изначальными данными (года: 2000-2020, все месяцы по 1000 руб.)
    def fill_storage(self):
        for year in range(2000, 2020):
            for month in range(1, 13):
                url = f'/add/{year}-{str(month).zfill(2)}-01/1000'
                self.app.get(url)

    def test_add_correct_money(self):
        for year in range(2000, 2020):
            for month in range(1, 13):
                url = f'/add/{year}-{str(month).zfill(2)}-01/1000'
                self.app.get(url)
                self.assertEqual(self.storage[year][month][1], 1000)
    def test_add_incorrect_date(self):
        url = f'/add/2024-200-01/10'
        with self.assertRaises(ValueError):
            self.app.get(url)

    def test_calculate_year_full_storage(self):
        self.fill_storage()
        for year in range(2000, 2020):
            url = f'/calculate/{year}'
            response_text = self.app.get(url).data.decode()
            self.assertTrue(str(year) in response_text and '12000 руб' in response_text)

    def test_calculate_year_empty_storage(self):
        for year in range(2000, 2020):
            url = f'/calculate/{year}'
            response_text = self.app.get(url).data.decode()
            self.assertTrue(str(year) in response_text and '0 руб' in response_text)

    months = {
        1: 'январь',
        2: 'февраль',
        3: 'март',
        4: 'апрель',
        5: 'май',
        6: 'июнь',
        7: 'июль',
        8: 'август',
        9: 'сентябрь',
        10: 'октябрь',
        11: 'ноябрь',
        12: 'декабрь',
    }
    def test_calculate_year_month_full_storage(self):
        self.fill_storage()
        for year in range(2000, 2020):
            for month in range(1, 13):
                url = f'/calculate/{year}/{month}'
                response_text = self.app.get(url).data.decode()
                self.assertTrue(self.months[month] in response_text and str(year) in response_text and '1000 руб' in response_text)

    def test_calculate_year_month_empty_storage(self):
        for year in range(2000, 2020):
            for month in range(1, 13):
                url = f'/calculate/{year}/{month}'
                response_text = self.app.get(url).data.decode()
                self.assertTrue(
                    self.months[month] in response_text and str(year) in response_text and '0 руб' in response_text)


