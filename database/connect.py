from pathlib import Path


class DBConnection:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.connection = None

    def __enter__(self):
        path = Path(self.file_path)
        if not path.is_file():
            file = open(str(path), mode='w', encoding='UTF8')
            file.close()

        self.connection = open(str(path), mode='r', encoding='UTF8')
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()
