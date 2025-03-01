d = {'a': 3, 'b': 5, 'c': 3, 'd': 7}
v = 3
count = 0
for value in d.values():
    if value == v:
        count += 1
print(count)
