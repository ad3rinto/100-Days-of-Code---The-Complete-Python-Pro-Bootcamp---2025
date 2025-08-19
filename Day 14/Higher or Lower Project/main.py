import random
from art import logo, vs
from game_data import data

game_len = 3
print(logo)
User_score = 0

def check(data_list):
    item_in_focus = random.choice(data_list)
    compared = random.choice(data_list)
    print(f"compare A: {item_in_focus['name']}, a {item_in_focus['description']}, from {item_in_focus['country']}")
    print(vs)
    print(f"B: {compared['name']}, a {compared['description']}, from {compared['country']}\n")
    answer = input("Who has more followers? Type A or B:\n").upper()


while game_len > 0:
    check(data)
    game_len -= 1