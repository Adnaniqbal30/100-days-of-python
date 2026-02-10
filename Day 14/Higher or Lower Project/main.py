from art import logo,vs
print(logo)
from game_data import data
import random
score=0

def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return (f"{account_name}, a {account_descr}, from {account_country}.")

account_a = random.choice(data)


while True:

    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Compare B: {format_data(account_b)}")

    ask_user=input("Who has more followers? Type 'A' or 'B': ").upper()
    account_followers_a = account_a["follower_count"]
    account_followers_b = account_b["follower_count"]

    if account_followers_a>account_followers_b and ask_user=="A":
        score+=1
        print(f"You are right, current score: {score}.")
    elif account_followers_a<account_followers_b and ask_user=="B":
        score+=1
        print(f"You are right, current score: {score}.")

    else:
        print(f"Sorry That's Wrong Final Score: {score}")
        break

    account_a=account_b


