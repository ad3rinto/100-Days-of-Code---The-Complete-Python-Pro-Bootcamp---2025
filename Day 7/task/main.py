import random

word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
word_to_guess = random.choice(word_list)
print(word_to_guess)
length = len(word_to_guess)
while length > 0:
# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = input("Guess a letter: ").lower()

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
#  is, "Wrong" if it's not.
    if guess in word_to_guess:
        print("Right")
    else:
        print("Wrong")
    length -= 1



