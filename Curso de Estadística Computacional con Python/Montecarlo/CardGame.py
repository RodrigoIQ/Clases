# we will siulate a game of cards to calculate the probabilityes of difrent games 
import random
import collections

SUITS = ['♣','♥','♠','♦']
RANKS = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

#Function that generates cards the 52 cards in a deck 

def creat_cards():
    cards = []
    for suit in SUITS:
        for rank in RANKS:
            cards.append((suit,rank))
    
    return cards

# Funktion that returns a hand
def generate_hand(deck,num_of_cards):
    hand = random.sample(deck,num_of_cards)
    return hand 

def games(amount_of_cards_in_hand,num_draws):
    deck = creat_cards()
    hands = []
    for _ in range(num_draws):
        hand = generate_hand(deck,amount_of_cards_in_hand)
        hands.append(hand)

    pairs = 0
    for hand in hands:
        values =[]
        for card in hand:
            values.append(card[1])
        
        counter = dict(collections.Counter(values))
        for card_value in counter.values():
            if card_value == 2:
                pairs += 1
                break

    probability_of_pairs = pairs/num_draws
    print(f'the amount of pairs was {pairs} the probability {probability_of_pairs}')

    
    



if __name__ == "__main__":
    
    amount_of_cards_in_hand = int(input('How many cards will a hand have? '))
    num_draws = int(input('How many times do ou want to generate new deck? '))

    games(amount_of_cards_in_hand,num_draws)