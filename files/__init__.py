import os.path

FILES_DIR = os.path.dirname(__file__)


def get_path(filename: str):
    return os.path.join(FILES_DIR, filename)


TXT_FILE_PATH = get_path(filename="example.txt")
CSV_FILE_PATH = get_path(filename="users.csv")
JSON_FILE_PATH = get_path(filename="example.json")
SQLITE_FILE_PATH = get_path(filename="data.sqlite")
