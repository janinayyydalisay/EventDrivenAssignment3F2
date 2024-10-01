people = {'profile': {'John': 19, 'Emily': 21, 'Sarah': 25, 'Tom': 18}}

older_than_19 = []
below_or_equal_19 = []

for name, age in people['profile'].items():
    if age > 19:
        older_than_19.append(name)
    else:
        below_or_equal_19.append(name)

print("People older than 19:", older_than_19)
print("People 19 or younger:", below_or_equal_19)
