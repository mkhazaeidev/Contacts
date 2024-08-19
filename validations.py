import re


class Validations:
    @staticmethod
    def is_name(name):
        if name.isalpha():
            return True
        return False
