import unittest, datetime
from mod3.person import Person

class TestPerson(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_person = Person('Андрей', 2004, 'Sulimova, 3/3')

    def test_get_age(self):
        test_yob = 2000
        self.test_person.yob = 2000
        self.assertTrue(self.test_person.get_age() == datetime.datetime.now().year - test_yob)

    def test_get_name(self):
        test_name = 'Alex'
        self.test_person.name = test_name
        self.assertTrue(self.test_person.get_name() == test_name)

    def test_set_name(self):
        test_name = 'Oleg'
        self.test_person.set_name(test_name)
        self.assertTrue(self.test_person.name == test_name)

    def test_get_address(self):
        test_address = 'Kosmonavtov St., 31'
        self.test_person.address = test_address
        self.assertTrue(self.test_person.get_address() == test_address)

    def test_set_address(self):
        test_address = 'Lenina St., 52'
        self.test_person.set_address(test_address)
        self.assertTrue(self.test_person.address == test_address)

    def test_is_homeless(self):
        self.test_person.address = None
        self.assertTrue(self.test_person.is_homeless())
        self.test_person.address = 'Lenina St., 52'
        self.assertFalse(self.test_person.is_homeless())