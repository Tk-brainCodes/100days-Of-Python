import random
def deal_cards():
    """Returns a random card from the deck"""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10]
    random_cards = random.choice(cards)
    return random_cards

def calc_score(cards):
    """Calculate the sum"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

user_cards = []
computer_cards = []

for _ in range(2):
    new_cards = deal_cards()
    user_cards.append(new_cards)
    computer_cards.append(new_cards)

user_score = calc_score(user_cards)
computer_score = calc_score(computer_cards)
is_game_over = False

if user_score == 0 or computer_score == 0 or user_score > 21:
    is_game_over = True
else:
    user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")  
    if user_should_deal == "y":
          user_cards.append(deal_cards())
    else:
        is_game_over = True    

while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_cards())
    computer_score = calc_score(computer_cards)
    
print(f"Your cards: {user_cards}, and current score {user_score} ")
print(f"Computer's first card: {computer_score[0]}")    




