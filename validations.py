import re


class Validations:
    @staticmethod
    def is_name(name, empty=False):
        pattern = r'^[A-Za-z ]+$'
        if not name and empty:
            return True
        elif re.match(pattern, name):
            return True
        return False

    @staticmethod
    def is_email(email, empty=False):
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not email and empty:
            return True
        elif re.match(pattern, email):
            return True
        return False

    @staticmethod
    def is_cellphone(cellphone, empty=False, ir=False):
        if ir:
            pattern = r"^09\d{9}$"
        else:
            pattern = r"^\+?\d{1,3}?[-.\s]?\(?\d{1,3}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}$"
        if not cellphone and empty:
            return True
        elif re.match(pattern, cellphone):
            return True
        return False

    @staticmethod
    def is_landline(landline, empty=False, ir=False):
        if ir:
            pattern = r"^0\d{2,3}-?\d{7,8}$"
        else:
            pattern = r"^\(?(0\d{2,3}[ -]?\d{3,4}[ -]?\d{3,4}|\(0\d{2,3}\) \d{3,4}[ -]?\d{3,4})$"
        if not landline and empty:
            return True
        elif re.match(pattern, landline):
            return True
        return False

    @staticmethod
    def is_password(password):
        pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
        if re.match(pattern, password):
            return True
        return False
