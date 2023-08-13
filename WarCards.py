import random
import os

#Suit, rank, value

values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 11,
         'Queen': 12, 'King': 13, 'Ace': 14}

ranks = tuple(values.keys())

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

#Card Class
class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + ' of ' + self.suit

#Deck Class which holds and deals the cards
class Deck:
    
    def __init__(self):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.cards.append(created_card)
                
    def shuffle(self):
        random.shuffle(self.cards)
        
    def deal_one(self):
        return self.cards.pop()

#Player Class
class Player:
    
    def __init__(self, name):
        self.name = name
        self.cards = []
        
    def remove_one(self):
        return self.cards.pop(0)
        
    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.cards.extend(new_cards)
        else:
            self.cards.append(new_cards)
        
    def __str__(self):
        return f'Player {self.name} has {len(self.cards)} cards.'

#Proper function order for the game with logic
def gameStart():
    
    #creating players
    player_1 = Player('Two')
    player_2 = Player('One')

    #Create the deck
    new_deck = Deck()
    new_deck.shuffle()
        
    #Deal cards to the players
    for x in range(26):
        player_1.add_cards(new_deck.deal_one())
        player_2.add_cards(new_deck.deal_one())
        
    game_on = True
    round_no = 0

    os.system('cls')
    
    while game_on:
        round_no += 1
        print('-' * 30)
        print(f'Round {round_no}')
        
        #Check if a player has lost
        if len(player_1.cards) == 0:
            print('Player 1 out of cards!\nPlayer 2 wins!')
            game_on = False
            break
            
        if len(player_2.cards) == 0:
            print('Player 2 out of cards!\nPlayer 1 wins!')
            game_one = False
            break
        
        #Start a new round
        player_one_cards = []
        player_one_cards.append(player_1.remove_one())
        player_two_cards = []
        player_two_cards.append(player_2.remove_one())
        
        #Game Logic
        at_war = True
        
        while at_war:
            if player_one_cards[-1].value > player_two_cards[-1].value:
                print(f'Player one won the war! Taking home {len(player_two_cards)}')
                player_1.add_cards(player_one_cards)
                player_1.add_cards(player_two_cards)
                
                at_war = False
                
            elif player_one_cards[-1].value < player_two_cards[-1].value:
                print(f'Player two won the war! Taking home {len(player_one_cards)}')
                player_2.add_cards(player_one_cards)
                player_2.add_cards(player_two_cards)
                
                at_war = False
                
            else:
                print('WAR!')
                
                if len(player_1.cards) < 5:
                    print('Player one unable to declare war')
                    print('Player 2 wins!')
                    game_on = False
                    break
                    
                elif len(player_2.cards) < 5:
                    print('Player two unable to declare war')
                    print('Player 1 wins!')
                    game_on = False
                    break
                    
                else:
                    for num in range(5):
                        player_one_cards.append(player_1.remove_one())
                        player_two_cards.append(player_2.remove_one())

if __name__ == '__main__':
    gameStart()
