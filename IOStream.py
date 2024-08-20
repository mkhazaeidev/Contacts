import hashlib
from getpass import getpass

from validations import Validations


class IOStream:
    @staticmethod
    def get_name(prompt: str, empty=False) -> str:
        while True:
            name = input(prompt)
            if Validations.is_name(name, empty):
                return name
            else:
                print("Invalid name. Please try again.")

    @staticmethod
    def get_email(prompt: str, empty=False) -> str:
        while True:
            email = input(prompt)
            if Validations.is_email(email, empty):
                return email
            else:
                print("Please enter a valid email.")

    @staticmethod
    def get_cellphone(prompt: str, empty=False, ir=False) -> str:
        while True:
            cellphone = input(prompt)
            if Validations.is_cellphone(cellphone, empty, ir):
                return cellphone
            else:
                print("Please enter a valid cellphone number.")

    @staticmethod
    def get_landline(landline: str, empty=False, ir=False) -> str:
        while True:
            landline = input(landline)
            if Validations.is_landline(landline, empty, ir):
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

    @staticmethod
    def get_address() -> dict:
        address = {
            'street': input("Street: "),
            'city': input("City: "),
            'state': input("State: "),
            'zip_code': input("Zip Code: "),
        }
        return address
