import hashlib
from getpass import getpass

from validations import Validations


class IOStream:
    @staticmethod
    def get_name(prompt: str) -> str:
        while True:
            name = input(prompt)
            if Validations.is_name(name):
                return name
            else:
                print("Please enter a valid name.")

    @staticmethod
    def get_email(prompt: str) -> str:
        while True:
            email = input(prompt)
            if Validations.is_email(email):
                return email
            else:
                print("Please enter a valid email.")

    @staticmethod
    def get_cellphone(prompt: str) -> str:
        while True:
            cellphone = input(prompt)
            if Validations.is_cellphone(cellphone):
                return cellphone
            else:
                print("Please enter a valid cellphone number.")

    @staticmethod
    def get_landline(landline: str) -> str:
        while True:
            landline = input(landline)
            if Validations.is_landline(landline):
                return landline
            else:
                print("Please enter a valid landline number.")

    @staticmethod
    def hash_password(password: str) -> str:
        return hashlib.sha256(password.encode("UTF-8")).hexdigest()

    @staticmethod
    def get_password(prompt: str) -> str:
        while True:
            password = getpass(prompt)
            if Validations.is_password(password):
                return IOStream.hash_password(password)
            else:
                print("Please enter a valid password.")

