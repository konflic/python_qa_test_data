import csv

with open('files/users.csv', newline='') as f:
    reader = csv.reader(f)

    # Извлекаем заголовок
    header = next(reader)
    for row in reader:
        print(dict(zip(header, row)))
