import art
print(art.logo)
import random
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")

random_number=random.randint(1,100)
level=input("Choose a difficulty. Type 'easy' or 'hard': ")
guess_number=int(input("Make a Guess: "))
print(type(guess_number))

def number_guess(gen_num,input_num,attempt):
    lives = 0
    if attempt == "easy":
        lives = 10
    else:
        lives = 5

    while True:
        if gen_num==input_num:
            print("You won!")
            break
        elif gen_num>input_num:
            print("Too low")
            print("Guess Again")
            lives-=1
            print(f"You have {lives} attempts remaining to guess the number.")
        else :
            print("Too High")
            print("Guess Again")
            lives-=1
            print(f"You have {lives} attempts remaining to guess the number.")
        if lives==0:
            print(f"Oops! You ran out of lives, the number was {gen_num}. ")
            break
        input_num=int(input("Make a Guess: "))
number_guess(random_number,guess_number,level)



