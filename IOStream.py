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
