print("Welcome to the love Calculator! ")
name1 = input("What is your name \n")
name2 = input("What is their name \n")

combined_str = name1 + name2
combined_str_toLowercase = combined_str.lower()


t = combined_str_toLowercase.count("t")
r = combined_str_toLowercase.count("r")
u = combined_str_toLowercase.count("u")
e = combined_str_toLowercase.count("e")

true_score = t + r + u + e

l = combined_str_toLowercase.count("l")
o = combined_str_toLowercase.count("o")
v = combined_str_toLowercase.count("v")
e = combined_str_toLowercase.count("e")

love_score = l + o + v + e

total_love_score = int(str(true_score) + str( love_score))
int_num = int(total_love_score)
if (total_love_score < 10) or (total_love_score > 90):
    print(f"Your score is {total_love_score}, you go like coke and mentos ")
elif (total_love_score >= 40) and (total_love_score <= 50):
    print(f"your score is {total_love_score}, you alright together")
else:
    print(f"your score is {total_love_score}")    