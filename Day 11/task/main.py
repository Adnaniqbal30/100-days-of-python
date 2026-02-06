import random
import art
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    return random.choice(cards)

def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0

    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(u_score,c_score):
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def play_game():
    print(art.logo)
    user_cards=[]
    computer_cards=[]
    is_game_over=False
    computer_score=-1
    user_score=-1

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:

        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)
        print(f"Your hand:{user_cards} :Your Score {user_score}")
        print(f"Computer first hand : {computer_cards[0]}")

        if user_score==0 or computer_score==0 or user_score>21 or user_score==21:
            is_game_over=True
        else:
            user_should_deal=input("Type y to get another card and n to pass: ")
            if user_should_deal=="y":
                user_cards.append(deal_card())
                user_score=calculate_score(user_cards)
            else:
                is_game_over=True

    while computer_score!=0 and computer_score<17:
        computer_cards.append(deal_card())
        computer_score=calculate_score(computer_cards)
    print(f"Your final hand: {user_cards}, Your final score: {user_score}")
    print(f"Computer Final hand: {computer_cards}, Computer final score {computer_score}")
    print(f"{compare(user_score,computer_score)}")

while input("Do you want to play a game of BlackJack: yes or no: ")=="yes":
    print("\n"*20)
    play_game()






