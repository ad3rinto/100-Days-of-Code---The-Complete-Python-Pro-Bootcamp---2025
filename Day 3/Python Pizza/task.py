print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
#
bill = 0
if size == "S":
    bill+= 15
elif size == "M":
    bill+= 20
elif size == "L":
    bill+= 25
else:
    print("Please enter a valid size.")

if pepperoni == "Y":
    if size == "S":
        bill+= 2
    else:
        bill+= 3
if extra_cheese == "Y":
    bill+= 1

print(f"Your final bill is: ${bill}.")

print("Welcome to Python Pizza deliveries")
size = input("What size of Pizza do you want?: ").upper()
pepperoni = input("Do you want Pepperoni?: ")
extra_cheese = input("DO you want extra cheese?: ")

bill = 0
if size == "L":
    bill = 20
elif size == "M":
    bill = 15
elif size == "S":
    bill = 10
else:
    print("You have entered an invalid size")

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if extra_cheese == "Y":
    bill += 1

print(f"Your total bill is ${bill}")

