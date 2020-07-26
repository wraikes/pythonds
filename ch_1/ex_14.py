import random

class Card:
    def __init__(self, suit, num):
        self.suit = suit #heart; diamond; club; spade
        self.num = num #2-10, J, Q, K, A

class Deck(Card):
    def __init__(self):
        self.deck = []
        self.suits = ['H', 'D', 'C', 'S']
        self.nums = [str(i) for i in range(2,11)] + ['J', 'Q', 'K', 'A']

    def populate_deck(self):
        for s in self.suits:
            for n in self.nums:
                self.deck.append(Card(s, n))

class War:
    def __init__(self, Decka, Deckb):
        self.player_a = 0
        self.player_b = 0

        self.Decka = Decka
        self.Deckb = Deckb


    def convert_card(self, card):
        value = 0

        if card.num == 'J':
            value = 11
        elif card.num == 'Q':
            value = 12
        elif card.num == 'K':
            value = 13
        elif card.num == 'A':
            value = 14
        else:
            value = int(card.num) 

        return value


    def round(self):
        deck_size = len(self.Decka.deck)

        #pull random int
        ran_a = random.randint(0, deck_size-1)
        ran_b = random.randint(0, deck_size-1)
    
        #pop card
        card_a = self.Decka.deck.pop(ran_a)
        card_b = self.Deckb.deck.pop(ran_b)

        #convert card into value
        card_a_val = self.convert_card(card_a)
        card_b_val = self.convert_card(card_b)

        #score
        if card_a_val < card_b_val:
            self.player_b += 1
        elif card_a_val > card_b_val:
            self.player_a += 1
        else:
            print('It is a tie.')

        print('Score player A: {}, B: {}'.format(self.player_a, self.player_b), end='\n\n')
    



if __name__=='__main__':
    d1 = Deck()
    d1.populate_deck()
    d2 = Deck()
    d2.populate_deck()

    war = War(d1, d2)
    for i in range(20):
        war.round()



