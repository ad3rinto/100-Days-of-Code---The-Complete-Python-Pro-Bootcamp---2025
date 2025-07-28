import random

dice_1 = random.randint(1, 6)
dice_2 = random.randint(1, 6)

dice_throw = (dice_1, dice_2)
print(dice_throw)

numbers = [1, 2, 3, 4, 5, 6]
random_samples = random.sample(numbers, 2)
print(f"random samples are {random_samples}")