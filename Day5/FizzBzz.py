divisible = 0
for number in range(1,101):
    if number % 3 and 5 == 0:
         print("FizzBuzz")
    elif number % 5 == 0:
        print("buzz")
    elif number % 3:
         print("fizz")
    else:
        print(number)     

