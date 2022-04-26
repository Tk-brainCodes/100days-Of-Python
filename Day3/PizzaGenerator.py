print("Welcome to Python Pizza Deliveries")
size = input("What size of pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese y or N")

pepperoni_for_small_pizza = 0
pepperoni_for_medium_or_large_pizza = 0
add_extra_cheese = 0

small_pizza = 15
medium_pizza = 20
large_pizza = 25

bill = 0


#for large pizza
if size == "L" and add_pepperoni == "Y" and extra_cheese == "Y":
    pepperoni_for_medium_or_large_pizza += 3
    add_extra_cheese += 1
    bill = large_pizza + pepperoni_for_medium_or_large_pizza + add_extra_cheese
    print(f"bill: ${bill}")
elif size == "L" and add_pepperoni == "N" and extra_cheese == "N":
    bill = large_pizza
    print(f"bill ${bill}")
elif size == "L" and add_pepperoni == "Y" and extra_cheese == "N":
    pepperoni_for_medium_or_large_pizza += 3
    bill = large_pizza + pepperoni_for_medium_or_large_pizza
    print(f"bill ${bill}")
elif size == "L" and add_pepperoni == "N" and extra_cheese == "Y":
    add_extra_cheese += 1
    bill = large_pizza + add_extra_cheese
    print(f"bill ${bill}")
else: 
    print("Please add pizza size");

#for medium pizza
if size == "M" and add_pepperoni == "Y" and extra_cheese == "Y":
    pepperoni_for_medium_or_large_pizza += 3
    add_extra_cheese += 1
    bill = medium_pizza + pepperoni_for_medium_or_large_pizza + add_extra_cheese
    print(f"bill: ${bill}")
elif size == "M" and add_pepperoni == "N" and extra_cheese == "N":
    bill = medium_pizza
    print(f"bill ${bill}")
elif size == "M" and add_pepperoni == "Y" and extra_cheese == "N":
    pepperoni_for_medium_or_large_pizza += 3
    bill = medium_pizza + pepperoni_for_medium_or_large_pizza
    print(f"bill ${bill}")
elif size == "M" and add_pepperoni == "N" and extra_cheese == "Y":
    add_extra_cheese += 1
    bill = medium_pizza + add_extra_cheese
    print(f"bill ${bill}")
else: 
    print("Please add pizza size");    
    
#for small pizza
if size == "S" and add_pepperoni == "Y" and extra_cheese == "Y":
    pepperoni_for_small_pizza += 2
    add_extra_cheese += 1
    bill = small_pizza + pepperoni_for_small_pizza + add_extra_cheese
    print(f"bill: ${bill}")
elif size == "S" and add_pepperoni == "N" and extra_cheese == "N":
    bill = small_pizza
    print(f"bill ${bill}")
elif size == "S" and add_pepperoni == "Y" and extra_cheese == "N":
    pepperoni_for_small_pizza += 2
    bill = small_pizza + pepperoni_for_small_pizza
    print(f"bill ${bill}")
elif size == "S" and add_pepperoni == "N" and extra_cheese == "Y":
    add_extra_cheese += 1
    bill = small_pizza + add_extra_cheese
    print(f"bill ${bill}")
else: 
    print("Please add pizza size");      
