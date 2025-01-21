# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

from Blind_auction_art import logo

print(logo)


def name_input(user_name, bid_amount):

    bidder[user_name] = bid_amount
    # print(bidder)


new_bidder = True
bidder = {}

while new_bidder:

    name = input("What is your name?").lower()
    bid = input("What is your bid amount: $").lower()

    name_input(user_name=name, bid_amount=bid)

    new_yes_no = input("is there anymore bidder?Y/N")

    if new_yes_no == "N":
        new_bidder = False
        result = max(bidder, key=bidder.get)  # obtain the key corresponding to max value.
        print(f"The winner is {result} with a bid of ${bidder[result]}")
    elif new_yes_no == "Y":
        print("\n"*20)
