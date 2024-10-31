from art import logo,vs
from game_data import data
import random

def format_data(account):
    #format the account data into printable format
    account_name=account["name"]
    account_descr=account["description"]
    account_country=account["country"]
    return(f"{account_name},a {account_descr},from {account_country}")

def check_answer(user_guess,a_followers,b_followers):
        """ takes the guess and the follower accounts of a and b and return if they r right """
        if a_followers > b_followers:
            return user_guess == "a"  # returns true
        else:
            return user_guess == "b"  # returns true




print(logo)
score=0
game_should_continue=True
account_b=random.choice(data)

# make the game repeatable
while game_should_continue:

    #generate random accnt from game data

    # making accnt at position b as next accnt at a
    account_a = account_b
    account_b=random.choice(data)
    if account_a == account_b:    #to ensure both are different
        account_b=random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Compare B: {format_data(account_b)}.")

    #ask user for a guess
    guess=input("who has more followers?Type 'A' or 'B':").lower()

    #clear the screen
    print("\n"*20)
    print(logo)
     #check if user is correct
     #get follower count of each account
    a_follower_count=account_a["follower_count"]
    b_follower_count=account_b["follower_count"]
    is_correct = check_answer(guess,a_follower_count,b_follower_count)

    if is_correct:
        score += 1
        print(f"Your right! Current score {score}")

    else:
        print(f"Sorry,that's wrong! Final score : {score}")
        game_should_continue = False





