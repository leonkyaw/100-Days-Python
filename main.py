import random
from art import logo

# TODO 1: Determine the rule of the game

# TODO 2: Set the condition for dealer ( combination of card < 17, draw)

# TODO 3: Set the card change for 1 or 11. depend on the total combination. (less than 10 set 11, greater set 1)

# TODO 4: show the second card of what they are holding.


def card_check(holding):
    if 11 in holding and sum(holding) > 21:
        holding.remove(11)
        holding.append(1)

    return sum(holding)


def draw_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)

    return card


def comparison(dealer_card_no, player_card_no):
    if dealer_card_no == player_card_no:
        return "Draw"
    elif dealer_card_no == 21:
        return "You lose"
    elif player_card_no == 21:
        return "You win"
    elif player_card_no > 21:
        return "You lose"
    elif dealer_card_no > 21:
        return "You win"
    elif dealer_card_no > player_card_no:
        return "You lose"
    else:
        return "You Win"


# Initial Draws (2 cards each)
def blackjack():
    player = []
    dealer = []
    for pick in range(2):
        player.append(draw_card())
        dealer.append(draw_card())

    player_card_no = card_check(player)
    dealer_card_no = card_check(dealer)

    print(f"Your current cards are {player} and your current score is {player_card_no},\n"
          f" Dealer's second card is {dealer[1]}.")

    while True:
        want_draw = input(f"Do you want to draw more? Y/N").upper()

        if want_draw == "Y":
            player.append(draw_card())
            player_card_no = card_check(player)
            print(f"your cards are {player}, your total score is {player_card_no}")
        else:
            break

    while True:
        if dealer_card_no < 17:
            dealer.append(draw_card())
            dealer_card_no = card_check(dealer)
        else:
            break

    print(f"Your final cards are {player}, your total score is {player_card_no}")
    print(f"Dealer final cards are {dealer}, dealer total score is {dealer_card_no}")
    print(comparison(dealer_card_no, player_card_no))


while True:
    play = input("Do you want to play blackjack again? Y/N").upper()

    if play == "Y":
        print(logo)
        blackjack()
    else:
        print("Sorry to see you go")
        break
