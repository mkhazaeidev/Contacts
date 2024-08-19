class Name:
    def __init__(self, first: str, last: str, middle: str = ""):
        self.first = first.lower()
        self.last = last.lower()
        self.middle = middle.lower()

    def get_full_name(self):
        if self.middle:
            full_name = f"{self.first} {self.middle} {self.last}"
        else:
            full_name = f"{self.first} {self.last}"
        return full_name.capitalize()

    def get_csv_info(self):
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
