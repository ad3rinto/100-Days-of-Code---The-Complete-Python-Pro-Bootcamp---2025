import random
from art import logo, vs
from game_data import data

game_on = True
print(logo)
user_score = 0

def check(data_list):
    """ Function to compare answer provided by user, with the computer generated question"""
    global user_score
    global game_on
    # generate chose random choices from the list o
    item_in_focus = random.choice(data_list)
    compared = random.choice(data_list)
    a_score = item_in_focus['follower_count']
    b_score = compared['follower_count']
    print(f"compare A: {item_in_focus['name']}, a {item_in_focus['description']}, from {item_in_focus['country']}")
    print(vs)
    print(f"B: {compared['name']}, a {compared['description']}, from {compared['country']}\n")
    answer = input("Who has more followers? Type A or B:\n").upper()
    # Compare the follower count of option A to option B
    if a_score > b_score and answer == 'A':
        user_score += 1
        print(f"You are right! Your current score is  {user_score}.")
        print("\n"*5)
    else:
        game_on = False
        print(f"Sorry, that's wrong. Final score:{user_score} , game over")



while game_on:
    check(data)
