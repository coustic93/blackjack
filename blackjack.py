import random
import time
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
    time.sleep(1)
    if total(p_hand) == 21:
        print ("Congratulations! You got a Blackjack!\n")
        time.sleep(0.5)
        chip+= int(round(bet*1.5))
    elif total(d_hand) ==21:
        print ("Sorry, the dealer has a Blackjack. You lose.")
        time.sleep(0.5)
        chip-=bet
    print("Dealer does not have Blackjack")
    time.sleep(0.5)

def chip_count():
    chip = 100

def play_game():
    print("Welcome to Black Jack")
    time.sleep(0.5)
    print("Here are 100 free chips!")
    time.sleep(0.5)
    chip = 100

    while chip > 0:
        print("You currently have {0} chips.".format(chip))
        bet = int(input("How much would you like to bet?\n"))
        d_hand = deal(deck_cards)
        p_hand = deal(deck_cards)

        # display player hand
        print("You have a(n) " + str(p_hand[0][0]) + " of " + str(p_hand[0][1]) + " and a(n) " + \
              str(p_hand[1][0]) + " of " + str(p_hand[1][1]) + " for a total of " + str(total(p_hand)))
        time.sleep(1)
        # check blackjack
        blackjack(d_hand,p_hand)
        # display one card of dealer hand
        print("Dealer is showing a(n) " + str(d_hand[0][0]) + " of " + str(d_hand[0][1]))
        time.sleep(1)
        choice = input("[H] for hit, [S] for stand\n").lower()

        while choice != 's':

            hit(p_hand)
            time.sleep(0.5)
            print("You have hit a(n) " + str(p_hand[2][0]) + " of " + str(p_hand[2][1]) + " for a total of " + str(total(p_hand)))
            if total(p_hand) > 21:
                time.sleep(0.5)
                print("Sorry, you have busted.")
                chip -= bet
                break
            elif total(p_hand) == 21:
                time.sleep(0.5)
                print("Congratulations! You got a Blackjack!\n")
                chip += int(round(bet*1.5))
                break
            choice = input("[H] for hit, [S] for stand\n").lower()
        if choice == 's':
            print("Dealer reveals second card...")
            time.sleep(0.5)
            print("Dealer reveals a " + str(d_hand[1][0]) + " of " + str(d_hand[1][1]) + " for a total of " + str(total(d_hand)))
            time.sleep(0.5)
            # dealer's turn
            if total(d_hand) < 17:
                while total(d_hand) < total(p_hand):
                    hit(d_hand)
                    print("Dealer hits...")
                    time.sleep(0.5)
                    print("Dealer reveals a " + str(d_hand[-1][0]) + " of " + str(d_hand[-1][1]) + " for a total of " + str(
                        total(d_hand)))
                    time.sleep(0.5)
                    if total(d_hand) > 21:
                        print("Dealer busts. Congratulations! You've won\n")
                        time.sleep(0.5)
                        chip += bet
                    elif total(d_hand) == 21:
                        print("Dealer has won blackjack. Sorry, you lost \n")
                        time.sleep(0.5)
                        chip -= bet
            else:
                if total(p_hand) > total(d_hand):
                    print("You win!")
                    time.sleep(0.5)
                    chip += bet
                    break
                elif total(p_hand) == total(d_hand):
                    print("You've tied!")
                    time.sleep(0.5)
                    break
                else:
                    print("Sorry... You've lost")
                    time.sleep(0.5)
                    chip-=bet
                    break
    print("You've lost all your chips!")
    time.sleep(0.5)
    reset()


def reset():
    replay = input("Would you like to play again? (Y/N) \n").lower()
    if replay == 'y':
        play_game()
    else:
        exit()

if __name__ == "__main__":
    play_game()


