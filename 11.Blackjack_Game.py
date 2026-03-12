import random
import art

def deal_card():
    cards = [2,3,4,5,6,7,8,9,10,10,10,10,11]
    card = random.choice(cards)
    return card
def calculate_score(card_list):
    score = sum(card_list)
    if score == 21:
        score = 0
    elif score > 21 and 11 in card_list :
            card_list.remove(11)
            card_list.append(1)
    return score


def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "Opponent has a Blackjack. You lose!"
    elif u_score == 0:
        return "You have a Blackjack. You win!"
    elif u_score > 21:
        return "You went over.You lose!"
    elif c_score > 21:
        return "Opponent went over. You win!"
    elif u_score > c_score:
        return "You win!"
    elif c_score > u_score:
        return "You lose!"
    return None

def game():
    print(art.logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"User's cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if computer_score == 0 or user_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Do you want another card? Type y or n: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            elif user_should_deal == "n":
                is_game_over = True

    while computer_score < 17 and computer_score != 0:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

game()

while input("Do you want to play again? Type y or n: ") == "y":
    print("\n" * 100)
    game()
