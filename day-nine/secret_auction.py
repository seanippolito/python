
def highest_bidder(bids):
    highest_bid = 0
    winner = ""
    for bidder in bids:
        bid = bids[bidder]
        if bid > highest_bid:
            highest_bid = bid
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

input("Welcome to the secret auction program!")
bidding = True
bids = {}
while(bidding):
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bids[name] = bid
    bidding = input("Are there any other bidders? (y/n): ") == "y"

highest_bidder(bids)