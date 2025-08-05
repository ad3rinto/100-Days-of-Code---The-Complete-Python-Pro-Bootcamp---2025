import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_card = random.sample(cards, 2)
computer_card = random.sample(cards, 2)
print(player_card)
print(computer_card)




def check_score(score1, score2):
    """Takes player score and computer score and check which is highest"""
    player_score = 0
    for _ in player_card:
        player_score += _

    computer_score = 0
    for _ in computer_card:
        computer_score += _
    if score1 > score2:
        print("player wins")
    else:
        print("computer wins")


if 11 in computer_card:
    print("computer wins")
elif 11 in player_card and 11 not in computer_card:
    print("player wins")
else:
    check_score(player_card, player_card)
