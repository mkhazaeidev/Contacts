from models import Contact


class Main:
    def __init__(self, file_name):
        self.file_name = file_name

    def show_contacts(self):
        contacts = Contact.objects.all(self.file_name)
        for contact in contacts:
            print(contact)


if __name__ == "__main__":
    main = Main("Contacts.csv")
    main.show_contacts()
