def squares(start, stop):
    for i in range(start, stop):
        # yield keyword is used!
        yield i * i


generator = squares(1, 10)

print(next(generator))
print(next(generator))
print(next(generator))

print(list(range(10)))
d = {'key': 'value'}
print(d)

print(next(generator))
print(next(generator))
print(next(generator))

print(list(range(10))[::-1])
d = {'key': 'value'}
print(d)

print(next(generator))
print(next(generator))
