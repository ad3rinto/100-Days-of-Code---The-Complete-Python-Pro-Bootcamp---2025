
"""
(print("Welcome to the rollercoaster!"))
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
else:
    print("Sorry you have to grow taller before you can ride.")
"""

print("Welcome to the rollercoaster bus ride of the year")
your_height = int(input("What is your height in cm? "))

if your_height >= 120:
    print("You are good to go")
    age = int(input("What is your age? "))
    if age >= 18:
        print("Amount to pay is £30")
    elif age >= 12:
        print("amount to pay in £20")
    else:
        print("YOu go for free")
else:
    print("Sorry you have to grow taller before you can ride.")

