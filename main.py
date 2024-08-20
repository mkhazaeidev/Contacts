from database import DBConnection
from models import Contact


class Main:
    def __init__(self):
        self.db = DBConnection("Contacts.csv", Contact.get_csv_header())


if __name__ == "__main__":
    main = Main()
