print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
tip_value= bill*tip/100
people = int(input("How many people to split the bill? "))
amount_to_pay = (bill + tip_value)/people
print(f"Each person to pay {amount_to_pay}, cheers.")

15