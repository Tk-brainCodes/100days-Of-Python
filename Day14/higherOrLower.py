from art import logo,vs
from game_data import data;
import random

print(logo)

score = 0

def check_answer(guess, a_follower, b_follower ):
    """Take the  users guess and follower and return if they got it right"""
    if a_follower > b_follower:
        return guess == "a"
    else:
        return guess == "b"    

def format_data(account):
    """Format data and make it readable"""
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc}, from {account_country}"

game_should_continue = True

account_b = random.choice(data)


while game_should_continue:

    account_a = account_b
    account_b  = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    guess = input("Who has more followers? A or B: ").lower()

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"] 

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1 
        print(f"Thats right! Current score {score}")
    else:
        game_should_continue = False 
        print(f"Sorry thats wrong. Final score {score}")  


