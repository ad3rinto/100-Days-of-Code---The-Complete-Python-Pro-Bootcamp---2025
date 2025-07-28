print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input("You are at a cross road? Will you turn left or right?\n:").lower()
if choice1 == "left":
    print("Now you are at a lake, will you wait or swim? :")
    choice2 = input("Wait || Swim: ").lower()
    if choice2 == "swim":
        print("Eaten by crocodile, you die")
    elif choice2 == "wait":
        choice3 = input("You made the rIght decision, two busses have arrives, will you get in the white or blue bus ").lower()
        if choice3 == "white":
            print("YOu don enter gbomo gbomo moto, byeee")
        elif choice3 == "blue":
            print("You are heading home. Congratulations")
        else:
            print("invalid entry. Game over")
elif choice1 == "right":
    print("You lose!")
else:
    print("You entered an invalid choice.\nGoodbye!")
