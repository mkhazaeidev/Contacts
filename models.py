from IOStream import IOStream


class Name:
    def __init__(self, first: str = "", last: str = "", middle: str = ""):
        if all([first, last, middle]):
            self.first = first.lower()
            self.last = last.lower()
            self.middle = middle.lower()
        else:
            self.set_name()

    def set_name(self):
        self.first = IOStream.get_name(prompt="First Name: ")
        self.last = IOStream.get_name("Last Name: ")
        self.middle = IOStream.get_name("Middle Name: ")

    def get_full_name(self):
        if self.middle:
            full_name = f"{self.first} {self.middle} {self.last}"
        else:
            full_name = f"{self.first} {self.last}"
        return full_name.capitalize()

    def get_name_info(self):
        return f"{self.first},{self.last},{self.middle}"

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

    def __dict__(self):
        return {"first": self.first, "last": self.last, "middle": self.middle}


class Phone:
    def __init__(self, mobile: str, home: str = "", work: str = "", fax: str = ""):
        self.mobile = mobile
        self.home = home
        self.work = work
        self.fax = fax

    def get_phone_info(self):
        return f"{self.mobile},{self.home},{self.work},{self.fax}"

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

    def __dict__(self):
        return {"mobile": self.mobile, "home": self.home, "work": self.work, "fax": self.fax}


class Address:
    def __init__(self, street: str, city: str, state: str, zip_code: str):
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code

    def get_address_info(self):
        return f"{self.street},{self.city},{self.state},{self.zip_code}"

    @staticmethod
    def get_csv_header():
        return f"Street Address,City,State,Zip Code"

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state}, {self.zip_code}"

    def __repr__(self):
        return f"Address('{self.street}, {self.city}, {self.state}, {self.zip_code}')"

    def __dict__(self):
        return {"street": self.street, "city": self.city, "state": self.state, "zip_code": self.zip_code}


class Email:
    def __init__(self, email: str):
        self.email = email

    def get_email_info(self):
        return f"{self.email}"

    @staticmethod
    def get_csv_header():
        return f"Email"

    def __str__(self):
        return f"{self.email}"

    def __repr__(self):
        return f"Email('{self.email}')"

    def __dict__(self):
        return {"email": self.email}


class Contact:
    def __init__(self):
        self.name = Name()
