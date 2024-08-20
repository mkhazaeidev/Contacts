import unittest
from validations import Validations


class TestValidation(unittest.TestCase):
    def setUp(self):
        self.name = "Mohammad Reza"
        self.email = "mkhazaei.dev@gmail.com"
        self.cellphone = "09010902690"

    def test_is_name(self):
        self.assertTrue(Validations.is_name(self.name))

    def test_is_email(self):
        self.assertTrue(Validations.is_email(self.email))

    def test_is_cellphone(self):
        self.assertTrue(Validations.is_cellphone(self.cellphone, ir=True))


if __name__ == '__main__':
    unittest.main(verbosity=2)
