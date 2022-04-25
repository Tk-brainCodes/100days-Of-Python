print("Welcome to the tip calculator");
total_bill = float(input("What was the total bill? $"));
total_bill_in_dollars = print(total_bill);
perc_tip = print(int(input("What percentage tip would you like to give? 10, 12, or 15? ")));
calc_perc_tip = total_bill * (perc_tip / 100);
total_perc_tip = total_bill + calc_perc_tip;
split_bill = print(int(input("How many people to split the bill? ")));
split_amount = total_perc_tip / split_bill;
each_pay = print(f"Each person should pay:  ${split_amount}")