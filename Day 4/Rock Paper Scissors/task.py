import random



options = {

    "rock" : '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''
,
    "paper": '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''
,
    "scissors" : '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''


}

robot = random.choice(["rock", "paper", "scissors"])
print("Computer has made a choice\n")
player1 = input("Now make yours : Rock, Paper, Scissors?\n").lower()
print(f"Computer's choice was {robot}\n")
print(options[robot])
print(f"Your choice was {player1}\n")
print(options[player1])
if robot == player1:
    print("This is a tie")
elif player1 == "rock" and robot == "scissors" or player1 == "scissors" and robot == "paper" or player1 == "paper" and robot == "rock":
    print("You win!")
else:
    print("You lose!")


