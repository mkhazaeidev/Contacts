import csv
from database import DBConnection


class Main:
    def __init__(self):
        self.db = DBConnection("Contacts.csv")

    def show_contacts(self):
        with self.db as db:
            for contact in csv.reader(db):
                print(contact)


if __name__ == "__main__":
    main = Main()
    main.show_contacts()
