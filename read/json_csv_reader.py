from csv import DictReader
from json import loads, dumps
from read.Book import Book
from read.User import UserBooks


books = []
userBooks = []
with open('../files/books.csv', 'r') as f:
    reader = DictReader(f)
    for row in reader:
        book = Book(row['Title'], row['Author'], row['Height'])
        books.insert(len(books), book.__dict__)


with open('../files/users.json', 'r') as file:
    j = file.read()
    reader = loads(j)
    for row in reader:
        userBook = UserBooks(row['name'], row['gender'], row['address'])
        userBooks.insert(len(userBooks), userBook.__dict__)


i = 0
for userBookRow in userBooks:
    if i < len(books):
        userBookRow['books'].insert(0, books[i])
        i = i+1
    else:
        break


with open('../files/result.json', 'w') as file:
    file.write(dumps(userBooks))









