import sqlite3
from files import SQLITE_FILE_PATH

connection = sqlite3.connect(SQLITE_FILE_PATH)

result = connection.execute("SELECT name, rank, gold FROM users;")

# Получаем заголовки для даных
headers = [row[0] for row in result.description]

for user in result.fetchall():
    print(dict(zip(headers, user)))
