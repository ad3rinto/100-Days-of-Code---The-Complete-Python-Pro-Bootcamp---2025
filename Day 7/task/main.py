import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

# TODO-1: - Use a while loop to let the user guess again.
while word_length > 0:
    guess = input("Guess a letter: ").lower()
    word_length -= 1

display = []

# TODO-2: Change the for loop so that you keep the previous correct letters in display.

for i in range(len(chosen_word) -1):
    if chosen_word[i] == guess:
        display[i] = guess
    else:
        display += "_"

print(display)
