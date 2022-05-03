import random

selections = ["rock", "paper", "scissors"]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))
computer_choice = random.randint(0,2)

if user_choice >=3 or user_choice < 0: 
    print("you typed an invalid number you loose") 
elif user_choice == 0 and computer_choice == 2:
    print("you win!")
elif computer_choice > user_choice:
    print("you loose")    
elif computer_choice == user_choice:
    print("its a draw")
elif user_choice == 2 and computer_choice == 0:
    print("you loose")  
elif computer_choice < user_choice:
    print("you win")          
   