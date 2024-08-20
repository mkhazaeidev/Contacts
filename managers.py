import csv

from database import DBConnection


class ContactManager:
    def __init__(self, headers: str):
        self.headers = headers

    def all(self, file_name):
        db = DBConnection(file_name, self.headers)
        contacts = []
        with db as file:
            for contact in csv.reader(file):
                contacts.append(contact)
        return contacts

    def save(self):
        pass

    def delete(self):
        pass

    def update(self):
        pass

    def create(self):
        pass

    def search(self):
        pass
