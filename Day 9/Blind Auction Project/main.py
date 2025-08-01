# TODO-1: Ask the user for input
from art import logo
print(logo)

def find_highest_bidder(bid_data):
    for key in bid_data:
        highest_bid = 0
        if bid_data[key] > highest_bid:
            highest_bid = bid_data[key]
    print(f"The highest bid is £{highest_bid}, by {key}")


bid_on = True
bid_dic = {}
while bid_on:
    name = input("What is your name?")
    bid = int(input("What is your bid?"))
    bid_to_proceed = input("Would you like to proceed? (Y/N)").upper()
    print("\n" * 20)
    bid_dic[name] = bid
    if bid_to_proceed == "N":
        bid_on = False
        find_highest_bidder(bid_dic)




# TODO-2: Save data into dictionary {name: price}

# TODO-3: Whether if new bids need to be added


# TODO-4: Compare bids in dictionary
