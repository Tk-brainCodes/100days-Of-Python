age_as_int = print(input("Enter your age: "));
age = int(age_as_int);
years_remaining = 90 - age;
weeks_remaining = 52 * years_remaining;
days_remaining = 362 * years_remaining;
months_remaining = 12 * years_remaining;

print(f"You have {years_remaining} years, {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} remaining")