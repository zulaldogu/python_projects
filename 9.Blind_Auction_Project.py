# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


import art
print(art.logo)
print("Welcome to the secret auction program!")
dictionary = {}
gameon = True
while gameon:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    dictionary[name] = bid
    restart = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if restart == "no":
        gameon = False
    elif restart == "yes":
        print("\n" * 100)
print(dictionary)
max_bid = 0
winner = ""
for name in dictionary:
    bid = dictionary[name]
    if bid > max_bid:
        max_bid = bid
        winner = name
print(f"The winner is {winner} with a bid of ${max_bid}")