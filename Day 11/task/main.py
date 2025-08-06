import art
import random
import time


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
        player_score += _
        if player_score > 21:
            player_score -= 10

    print(playercard)

    computer_score = 0
    for _ in computercard:
        computer_score += _
        if computer_score > 21:
            computer_score -= 10

def check_win(score1, score2):
    time.sleep(4)
    if score1 < score2:
        print("Computer wins - 1")
        print(computer_card)
    elif score1 == score2:
        print("This one na draw ooo")
        print(computer_card)
    else:
        print("Player wins")
        print(computer_card)
    print("\n" *2)


first_draw(player_card,computer_card)

if 11 in computer_card and 10 in computer_card:
    print("Blackjacks, computer wins")
    print(computer_card)
elif 11 in player_card and 10 in player_card:
    print("Blackjacks, player wins")
    print(computer_card)
elif 11 in player_card and 11 not in computer_card:
    print("player wins")
    print(computer_card)
else:
    check_win(player_card, computer_card)
