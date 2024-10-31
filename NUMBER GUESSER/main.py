import art
from random import randint


EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5

def check_answer(user_guess, actual_answer, turns):
    """checks answer to the guess and checks no of guesses remaining"""
    if user_guess>actual_answer:
        print("too high")
        return turns -1
    elif user_guess == actual_answer :
        print(f"You got it ! your answer was {actual_answer}")
    elif user_guess<actual_answer:
        print("too low")
        return turns-1


def set_difficulty():
    level=input("choose a difficulty 'easy' or 'hard'")
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print(art.logo)
    print("welcome to the guessing game")
    print("im thinking of a number between 1 and 100")
    answer=randint(1,100)
    print(f"psst,the correct answer is {answer}")

    turns = set_difficulty()

    guess=0
    while guess != answer:
        print(f"you have {turns} attempts remaining")
        guess = int(input("make a guess"))
        turns=check_answer(guess,answer,turns)
        if turns == 0:
            print("you've run out of attempts,you loose")
            return
        elif guess!=answer:
            print("guess again")

game()


