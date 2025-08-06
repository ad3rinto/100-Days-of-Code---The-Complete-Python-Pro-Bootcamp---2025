import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_card = random.sample(cards, 2)
computer_card = random.sample(cards, 2)

print(art.logo)

# print(player_card)
# print(computer_card)

def first_draw(playercard,computercard):
    """Takes player score and computer score and check which is highest"""
    player_score = 0
    for _ in playercard:
        print(_)
        player_score += _

    computer_score = 0
    for _ in computercard:
        print(_)
        computer_score += _

def check_win(score1, score2):
    if score1 < score2:
        print("Computer wins - 1")
    elif score1 == score2:
        print("This one na draw ooo")
    else:
        print("Player wins")
    print("\n" *2)


first_draw(player_card,computer_card)

if 11 in computer_card and 10 in computer_card:
    print("Blackjacks, computer wins")
elif 11 in player_card and 10 in player_card:
    print("Blackjacks, player wins")
elif 11 in player_card and 11 not in computer_card:
    print("player wins")
else:
    check_win(player_card, computer_card)
