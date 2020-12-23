import random

# create a deck of cards
num = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
suit = ["Hearts", "Diamonds", "Spades", "Clubs"]
deck_cards = []
for i in suit:
    for j in num:
        deck_cards.append((i, j))
random.shuffle(deck_cards)

def deal(deck_cards):
    hand = []
    for i in range(2):
        card = deck_cards.pop()
        suit, num = card
        if num == 11:
            num = "J"
        elif num == 12:
            num = "Q"
        elif num == 13:
            num = "K"
        elif num == 14:
            num = "A"
        card = (num, suit)
        hand.append(card)
    return hand

def total(hand):
    # calculate value of hand
    hand_tot = 0
    for i in hand:
        num, suit = i
        if num =="J" or num == "Q" or num == "K":
            hand_tot += 10
        elif num == "A":
            if hand_tot >= 11:
                hand_tot +=1
            else:
                hand_tot += 11
        else:
            hand_tot += num
    return hand_tot

def hit(hand):
    card = deck_cards.pop()
    suit, num = card
    if num == 11:
        num = "J"
    elif num == 12:
        num = "Q"
    elif num == 13:
        num = "K"
    elif num == 14:
        num = "A"
    card = (num, suit)
    hand.append(card)

def blackjack(d_hand, p_hand):
    print("Dealer is checking for Blackjack...")
    if total(p_hand) == 21:
        print ("Congratulations! You got a Blackjack!\n")
        reset()
    elif total(d_hand) ==21:
        print ("Sorry, the dealer has a Blackjack. You lose.")
        reset()
    print("Dealer does not have Blackjack")


def play_game():
    print("Welcome to Black Jack")
    d_hand = deal(deck_cards)
    p_hand = deal(deck_cards)

    # display player hand
    print("You have a(n) " + str(p_hand[0][0]) + " of " + str(p_hand[0][1]) + " and a(n) " + \
          str(p_hand[1][0]) + " of " + str(p_hand[1][1]) + " for a total of " + str(total(p_hand)))
    # check blackjack
    blackjack(d_hand,p_hand)
    # display one card of dealer hand
    print("Dealer is showing a(n) " + str(d_hand[0][0]) + " of " + str(d_hand[0][1]))

    choice = input("[H] for hit, [S] for stand").lower()
    while choice != 's':
    #if choice == 'h':
        hit(p_hand)
        print("You have hit a(n) " + str(p_hand[2][0]) + " of " + str(p_hand[2][1]) + " for a total of " + str(total(p_hand)))
        if total(p_hand) > 21:
            print("Sorry, you have busted.")
            reset()
        elif total(p_hand) == 21:
            print("Congratulations! You got a Blackjack!\n")
            reset()
        choice = input("[H] for hit, [S] for stand").lower()

    print("Dealer reveals second card...")
    print("Dealer reveals a " + str(d_hand[1][0]) + " of " + str(d_hand[1][1]) + " for a total of " + str(total(d_hand)))
    if total(d_hand) < 17:
        while total(d_hand) <= 21:
            print("Dealer hits...")
            hit(d_hand)
            if total(d_hand) > 21:
                print("Dealer busts. Congratulations! You've won\n")
                reset()
            elif total(d_hand) == 21:
                print("Dealer has won blackjack. Sorry, you lost \n")
                reset()
    else:
        if total(p_hand) > total(d_hand):
            print("You win!")
            reset()
        elif total(p_hand) == total(d_hand):
            print("You've tied!")
            reset()
        else:
            print("Sorry... You've lost")
            reset()


def reset():
    replay = input("Would you like to play again? (Y/N) ").lower()
    if replay == 'y':
        play_game()
    else:
        exit()

if __name__ == "__main__":
    play_game()

