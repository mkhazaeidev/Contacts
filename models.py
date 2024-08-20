import uuid

from managers import ContactManager
from IOStream import IOStream


class Name:
    def __init__(self, first: str = "", last: str = "", middle: str = ""):
        if all([first, last, middle]):
            self.first = first.lower()
            self.last = last.lower()
            self.middle = middle.lower()
        else:
            self.set_names()

    def set_names(self):
        self.first = IOStream.get_name("First Name: ")
        self.last = IOStream.get_name("Last Name: ")
        self.middle = IOStream.get_name("Middle Name: ", empty=True)

    def get_full_name(self):
        if self.middle:
            full_name = f"{self.first} {self.middle} {self.last}"
        else:
            full_name = f"{self.first} {self.last}"
        return full_name.capitalize()

    def get_name_info(self):
        return f"{self.first},{self.last},{self.middle}"

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def get_csv_header():
        return f"First Name,Last Name,Middle Name"

    def __str__(self):
        if self.middle:
            full_name = f"{self.first} {self.middle[0]}. {self.last}"
        else:
            full_name = f"{self.first} {self.last}"
        return full_name.capitalize()

    def __repr__(self):
        return f"Name('{self.first}', '{self.last}', {self.middle})"


class Phone:
    def __init__(self, mobile: str = "", home: str = "", work: str = "", fax: str = ""):
        if any([mobile, home, work, fax]):
            self.mobile = mobile
            self.home = home
            self.work = work
            self.fax = fax
        else:
            self.set_phones()

    def set_phones(self):
        self.mobile = IOStream.get_cellphone("Mobile Number: ", ir=True)
        self.home = IOStream.get_landline("Home Number: ", empty=True, ir=True)
        self.work = IOStream.get_landline("Home Number: ", empty=True, ir=True)
        self.fax = IOStream.get_landline("Home Number: ", empty=True, ir=True)

    def get_phone_info(self):
        return f"{self.mobile},{self.home},{self.work},{self.fax}"

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def get_csv_header():
        return f"Mobile,Home,Work,Fax"

    def __str__(self):
        phones = [self.mobile, self.home, self.work, self.fax]
        phones = list(
            map(lambda item: item if item else "NotSet", phones)
        )
        phones = ",".join(phones)
        return phones

    def __repr__(self):
        return f"Phone('{self.mobile}', '{self.home}', '{self.work}', '{self.fax}')"


class Address:
    def __init__(self, street: str = "", city: str = "", state: str = "", zip_code: str = ""):
        if any([street, city, state, zip_code]):
            self.street = street
            self.city = city
            self.state = state
            self.zip_code = zip_code
        else:
            self.set_address()

    def set_address(self) -> None:
        address = IOStream.get_address()
        self.street = address["street"]
        self.city = address["city"]
        self.state = address["state"]
        self.zip_code = address["zip_code"]

    def get_address_info(self):
        return f"{self.street},{self.city},{self.state},{self.zip_code}"

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def get_csv_header():
        return f"Street Address,City,State,Zip Code"

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state}, {self.zip_code}"

    def __repr__(self):
        return f"Address('{self.street}, {self.city}, {self.state}, {self.zip_code}')"


class Email:
    def __init__(self, email: str = ""):
        if email:
            self.email = email
        else:
            self.set_email()

    def set_email(self):
        self.email = IOStream.get_email("Email Address: ", empty=True)

    def get_email_info(self):
        return f"{self.email}"

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def get_csv_header():
        return f"Email"

    def __str__(self):
        return f"{self.email}"

    def __repr__(self):
        return f"Email('{self.email}')"


def get_contacts_csv_header():
    headers = (
        Name.get_csv_header(),
        Phone.get_csv_header(),
        Email.get_csv_header(),
        Address.get_csv_header()
    )
    return f"ID,{','.join(headers)}"


class Contact:
    objects = ContactManager(get_contacts_csv_header())

    def __init__(self):
        self._id = uuid.uuid4()
        self.name = Name()
        self.phone = Phone()
        self.email = Email()
        self.address = Address()

    @property
    def id(self):
        return self._id.int

    def get_contact_info(self):
        info = (
            self.id,
            self.name.get_name_info(),
            self.phone.get_phone_info(),
            self.email.get_email_info(),
            self.address.get_address_info()
        )
        return f"{','.join(info)}"

    def to_dict(self):
        return {
            "id": self._id,
            "name": self.name.to_dict(),
            "phone": self.phone.to_dict(),
            "email": self.email.to_dict(),
            "address": self.address.to_dict(),
        }

    def __str__(self):
        return f"{self._id}, {str(self.name)}, {str(self.phone)}, {str(self.email)}, {str(self.address)}"

    def __iter__(self):
        return self
