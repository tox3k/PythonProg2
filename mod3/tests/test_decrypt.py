import unittest

from mod3.decrypt import decrypt


class TestDecrypt(unittest.TestCase):
    test_cases = {
        'абра-кадабра.': 'абра-кадабра',
        'абраа..-кадабра': 'абра-кадабра',
        'абраа..-.кадабра': 'абра-кадабра',
        'абра--..кадабра': 'абра-кадабра',
        'абрау...-кадабра': 'абра-кадабра',
        'абра........': '',
        'абр......a.': 'a',
        '1..2.3': '23',
        '.': '',
        '1.......................': '',
    }


    def setUp(self):
        self.method = decrypt

    def test_dectypt_less_than_three_dots(self):
        # В случае ошибки, сабтест покажет на каком кол-ве точек провалились
        for k, v in self.test_cases.items():
            with self.subTest(f'Кол-во точек: {k.count(".")}', k=k, v=v):
                self.assertEqual(self.method(k), self.test_cases[k])