print("Welcome to Treasure Island.")
d = print(input("left or right? ").lower())
dec = print(input("swim or wait").lower())
wait = print(input("which door? ").lower())
red = print("Game over")
blue = print("Game over")
yellow = print("You win!")

if d == "right":
    print("Game over")
else:
    print(dec)

if dec == "swim":
    print("Game over")
else:
    print(wait)   

if red == "red":
    print("Game over")
elif blue == "blue":
    print("Game over!")
elif yellow == "yellow":
    print("You Win!")
else:
    print("Game over")    
