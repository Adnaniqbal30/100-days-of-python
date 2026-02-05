# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
import art
print(art.logo)
auction={}
while True:
     name = input("What is your name: ")
     bid_price = input("What's your bid: ")

     auction[name]=bid_price
     print("\n"*20)
     new_bid=input("Are there any other bidders, yes or no.").lower()

     if new_bid=="no":
         break

highest_value_key=max(auction, key=auction.get)
highest_value=max(auction.values())
print(f"The Winner is {highest_value_key} with a bid of {highest_value}.")
