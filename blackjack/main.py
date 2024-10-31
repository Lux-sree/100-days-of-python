import random
def deal_card():
    """returns random card from the deck"""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """take list of cards and return scores calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "lose,opponent has a blackjack"
    elif u_score == 0:
        return "win with a blackjack"
    elif u_score > 21:
        return "you went over,u lose"
    elif c_score > 21:
        return "opponent went over,u win"
    elif u_score > c_score:
        return "you win"
    else:
        return "you lose"
def play_game():
    user_card = []
    computer_card = []
    computer_score = -1
    user_score = -1
    is_gameover = False

    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())
    while not is_gameover:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)
        print(f"Your cards : {user_card},current score :{user_score}")
        print(f"Computers first card:{computer_card[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_gameover = True
        else:
            user_should_deal = input("Type 'y' to get another card,Type 'n' to pass:")
            if user_should_deal == 'y':
                user_card.append(deal_card())
            else:
                is_gameover = True

    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)
    print(f"your final hand : {user_card},final score : {user_score}")
    print(f"computers final hand : {computer_card},final score : {computer_score}")
    print(compare(user_score, computer_score))


while input("do you want to play a game of blackjack? Type 'y' or 'n' :") == 'y':
    print("\n" * 20)
    play_game()






