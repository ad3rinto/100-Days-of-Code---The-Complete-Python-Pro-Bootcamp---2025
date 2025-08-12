from art import logo
import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty level: easy or hard:\n:").lower()

is_game_over = False
guessed_number = random.randint(1, 100)
number_of_tries = 10

def set_difficulty():
    if difficulty == "easy":
        return 3
    elif difficulty == "hard":
        return 2
    else:
        return "Invalid difficulty"

def check_choice(gue, g_number, diff):
    if gue == g_number:
        print("You guessed correctly!")
    elif gue < g_number:
        print("You guessed too low!")
        diff -= 1
    else:
        print("You guessed too high!")
        diff -= 1


def game():
    global is_game_over
    global number_of_tries
    while not is_game_over and number_of_tries > 0:
        guess = int(input("Guess a number between 1 and 100: "))
        if guess == guessed_number:
            number_of_tries -= 1
            is_game_over = True
            print("You guessed the correct number!")
        else:
            if guess < guessed_number:
                print("Your guess is too low.")
            elif guess > guessed_number:
                print("Your guess is too high.")
            print("You did not guess the correct number, try again.")
            number_of_tries -= 1
            print(f"you have {number_of_tries} attempts left")
            game_play()





game()



