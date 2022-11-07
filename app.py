import json
import csv
from csv import DictReader

books = []
result = []

with open('./hw_files/books.csv', newline='') as f:
    rows = DictReader(f)
    for row in rows:
        books.append(dict(row))

with open('./hw_files/users.json', 'r') as f:
    users = json.loads(f.read())
user_list = users

for user in user_list:
    book_usr = {}
    book_usr["name"] = user["name"]
    book_usr["gender"] = user["gender"]
    book_usr["address"] = user["address"]
    book_usr["books"] = [books.pop(0)] if len(books) > 0 else []
    result.append(book_usr)

# if len(user_list) <= len(books):
#     for user in user_list:
#         book_usr = {}
#         book_usr["name"] = user["name"]
#         book_usr["gender"] = user["gender"]
#         book_usr["address"] = user["address"]
#         book_usr["books"] = [books.pop(0)]
#         result.append(book_usr)
# else:
#     for user in user_list:
#         book_usr = {}
#         book_usr["name"] = user["name"]
#         book_usr["gender"] = user["gender"]
#         book_usr["address"] = user["address"]
#         book_usr["books"] = [books.pop(0)] if len(books) > 0 else []
#         result.append(book_usr)

# result = json.dumps(result)
# print(result)

with open("./hw_files/result.json", "w") as f:
    s = json.dumps(result, indent=4)
    f.write(s)
