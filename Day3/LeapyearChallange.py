year = input(int("Enter year to check"));

if year % 4 == 0:
    if year % 100 == 0: 
        if year % 400 == 0:
         print("Leap year");
        else:
            print("Not Leap year");
    else:
        print("Leap year");
else:
    print("Not leap year")