from art import logo
import random



def deal_cards():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
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
        return "Lose, Computer has a blackjack"
    elif u_score == 0:
        return "Win with a blackjack"
    elif u_score > 21:
        return "You went over the score, You lose"
    elif c_score > 21:
        return "Computer went over. You win"
    elif c_score > u_score:
        return "You lose. Computer score is greater than you"
    elif u_score > c_score:
        return "You Win. Your score is greater"

def playgame():
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_cards())
        #We cannot use += here because its an expression to extend
        #If we were to use += or .extend() we have to add list with a list not a single item into a list.
        computer_cards.append(deal_cards())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_cards())
            else:
                is_game_over = True
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)

        print(f"Your final cards: {user_cards}, final score: {user_score}")
        print(f"Computer final cards: {computer_cards}, final score: {computer_score}")
        print(compare(user_score, computer_score))

while input("Do you want to play a game of black jack ? Then type 'y' if not then 'n':").lower() == 'y':
    print('\n'* 20)
    playgame()