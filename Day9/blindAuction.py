user_name = input("Enter your name: \n")
bid_price = int(input("Enter price:  \n"))
yes = input("Enter your name")
yes_price = input("ENter your price: ")



def blind_Auction(name, price):
    new_dictionary = {}
    new_dictionary[name] = user_name
    new_dictionary[price] = bid_price

    if user_name and bid_price in new_dictionary:
        bidding_finished = False
        while bidding_finished:
            should_continue =  print("Are there any user who wants to bid?  type yes or no")
            if should_continue == "yes":
                print(yes)
                new_dictionary[name] = yes
                new_dictionary[price] = yes_price 
            else: 
                bidding_finished = True
    highest_bid = 0
    winner = ""        
    for bidder in new_dictionary:
          bid_amount = new_dictionary[bidder]
          if bid_amount > highest_bid:
              highest_bid = bid_amount
              winner = bidder
    print(f"The winner is {winner} with bid of ${highest_bid}")          


blind_Auction(user_name, bid_price)

         
