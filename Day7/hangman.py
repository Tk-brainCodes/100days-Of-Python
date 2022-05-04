import random

print('''888                                                           
888                                                           
888                                                           
88888b.  8888b. 88888b.  .d88b. 88888b.d88b.  8888b. 88888b.  
888 "88b    "88b888 "88bd88P"88b888 "888 "88b    "88b888 "88b 
888  888.d888888888  888888  888888  888  888.d888888888  888 
888  888888  888888  888Y88b 888888  888  888888  888888  888 
888  888"Y888888888  888 "Y88888888  888  888"Y888888888  888 
                             888                              
                        Y8b d88P                              
                         "Y88P" ''')






word_list = ["ardvark", "baboon", "carmel"]
chosen_word = random.choice(word_list)

end_of_game = False
display = []
chosen_word_len = len(chosen_word)
lives = 6

while not end_of_game:
    guess = input("Guess a letter: \n").lower()

    for dash in range(chosen_word_len):
        display += "_"
    for position in range(chosen_word_len):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
        if guess not in chosen_word:
            lives -= 1   
        if lives == 0:
            end_of_game = True
            print("you loose ):")    

    print(display)

    if "_" not in display:
            does_not_exist = True
            print("you win! (:")
   

 
      
      


