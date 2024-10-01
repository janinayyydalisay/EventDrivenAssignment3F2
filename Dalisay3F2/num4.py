numbers = [1, 3, 2, 4, 3, 1, 2, 5, 10]

duplicates = []
for num in numbers:
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

if duplicates:
    print("Duplicate numbers:", duplicates)
else:
    print("No duplicate numbers found.")
