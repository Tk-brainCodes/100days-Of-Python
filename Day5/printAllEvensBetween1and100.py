total_evens = 0

for number in range(1, 101):
    if number % 2 == 0:
        total_evens += number
print(f"Sum of all evens: {total_evens}")