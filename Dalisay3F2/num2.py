numbers = (1, 4, 7, 10, 13, 16)

odd_numbers = []
odd_sum = 0
odd_count = 0

for num in numbers:
    if num % 2 != 0:
        odd_numbers.append(num)
        odd_sum += num
        odd_count += 1

if odd_count > 0:
    odd_average = odd_sum / odd_count
    print("Odd numbers:", odd_numbers)
    print("Average of odd numbers:", odd_average)
else:
    print("No odd numbers found.")
