values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10,
         'Queen': 10, 'King': 10, 'Ace': 11}

ranks = tuple(values.keys())

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

import random

#Card class
class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + ' of ' + self.suit

#Deck class
class Deck:
    
    def __init__(self):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.cards.append(created_card)
                
    def shuffle(self):
        random.shuffle(self.cards)
        
    def deal_cards(self, amt=1):
        dealt_cards = []
        for i in range(amt):
            dealt_cards.append(self.cards.pop())
        
        return dealt_cards

class Bank:
    
    def __init__(self, name, amt):
        self.balance = amt
        self.account_holder = name
        
    def withdraw(self, amt):
        if self.balance >= amt:
            self.balance -= amt
            print(f'Remaining balance : {self.balance}')
        else:
            print('Insufficient funds!')
            
    def deposit(self, amt):
        self.balance += amt
        print(f'New Balance: {self.balance}')

#Player Class
class Player:
    
    def __init__(self, name, bank_account):
        self.name = name
        self.cards = []
        self.bank_account = bank_account
        
    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.cards.extend(new_cards)
        else:
            self.cards.append(new_cards)
            
    def total_value(self):
        hand_value = 0
        
        #Add all cards except ace
        for card in self.cards:
            if card.value <= 10:
                hand_value += card.value
                
        #Now add aces after all cards have been evaluated
        for card in self.cards:
            if card.value > 10:
                if hand_value <= (21 - 11):
                    hand_value += card.value
                else:
                    hand_value += (card.value - 10)
                    
        return hand_value
        
    def __str__(self):
        print_string = f'{self.name} has {len(self.cards)} cards\n'
        print_string += ('-' * 30)
        print_string += '\n'
        
        try:
            for card in self.cards:
                print_string += f'{str(card)}\n'
        except:
            print('Something went wrong! Are the cards dealt?')
                
        print_string += ('-' * 30)
        print_string += '\n'
        
        return print_string

#Dealer class
class Dealer:
    
    def __init__(self):
        self.cards = []
        
    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.cards.extend(new_cards)
        else:
            self.cards.append(new_cards)
            
    def total_value(self):
        hand_value = 0
        
        #Add all cards except ace
        for card in self.cards:
            if card.value <= 10:
                hand_value += card.value
                
        #Now add aces after all cards have been evaluated
        for card in self.cards:
            if card.value > 10:
                if hand_value <= (21 - 11):
                    hand_value += card.value
                else:
                    hand_value += (card.value - 10)
                    
        return hand_value
    
    def __str__(self):
        print_string = f'Dealer has {len(self.cards)} cards\n'
        print_string += ('-' * 30)
        print_string += '\n'
        
        try:
            for card in self.cards[1::]:
                print_string += f'{str(card)}\n'
        except:
            print('Something went wrong! Are the cards dealt?')
                
        print_string += ('-' * 30)
        print_string += '\n'
        
        return print_string

#Proper game order and game logic
import os

def game_start(new_player, new_dealer, new_deck, bank_account):
    
    bank_balance = bank_account.balance
    game_on = True
    actions = '1. Stay (Stop recieving cards)     | 2. Hit (Recieve one random card)         : '
    
    #How much is the player betting?
    if bank_balance > 0:
        while True:
            try:
                bet = int(input(f'How much are you betting? Your current account balance is {bank_balance}\n'))
                if bet <= bank_balance:
                    bank_account.withdraw(bet)
                else:
                    raise InvalidBet('Invalid number for your bet')
            except:
                print('Enter a valid number (within your bank balance)')
            else:
                break
    else:
        print('If you continue anymore you will be in debt.\nExiting the game...')
        return;
    
    while game_on:
        os.system('cls')
        #Show both dealer and player's cards
        print("Showing player's hands -->")
        print(new_player)
        print(f'Hand Value : {new_player.total_value()}\n')
        print('-'*10 + '*'*3 + '-'*10)
        print("Showing dealer's hands - hiding one -->")
        print(new_dealer)
        print()
        
        print("Player goes first")
    
        #Player's loop
        while True:
            choice = input(actions)
            if choice in ['1', 'Stay']:
                break
                
            elif choice in ['2', 'Hit']:
                new_card = new_deck.deal_cards(1)
                new_player.add_cards(new_card)
                print(new_player)
                print(f'Hand Value : {new_player.total_value()}')
                
                if new_player.total_value() > 21:
                    print('BUST!')
                    print('Player has exceeded the limit, dealer wins!')
                    game_on = False
                    break
                    
            else:
                print('Invalid choice!')
                
        #IF player lost
        if not game_on:
            break
            
        os.system('cls')
        print("Dealer's turn")
        #Dealer's loop
        while True:
            #100% draw if no risk
            if new_dealer.total_value() <= (11):
                print('Dealer says Hit and draws a card....')
                new_card = new_deck.deal_cards(1)
                print(f'Drew a {new_card[0]}')
                new_dealer.add_cards(new_card)
                print(new_dealer)
                
            #do a random call if risk is low
            elif new_dealer.total_value() <= (11 + 5):
                draw_card = random.randint(0, 100) > 30
                
                if draw_card:
                    print('Dealer says Hit and draws a card....')
                    new_card = new_deck.deal_cards(1)
                    print(f'Drew a {new_card[0]}')
                    new_dealer.add_cards(new_card)
                    print(new_dealer)
                else:
                    print('Dealer says Stay and ends his round....')
                    break
                    
            else:
                print('Dealer says Stay and ends his round....')
                break
                
            if new_dealer.total_value() > 21:
                print('BUST!')
                print('Dealer has exceeded the limit')
                
                print("Dealer's Cards")
                print('-'*30)
                for card in new_dealer.cards:
                    print(card)
                print('-'*30)
                
                print('Player wins!')
                print('Doubling his bet...')
                bank_account = new_player.bank_account
                bank_account.deposit(bet * 2)

                game_on = False
                break
        
        #IF dealer lost
        if not game_on:
            break
            
        choice = input('Press any key to continue: ')
        os.system('cls')
        #IF both player and dealer didnt bust
        print(new_player)
        print(f'Hand Value: {new_player.total_value()}\n')
        
        print("Dealer's Cards")
        print('-'*30)
        for card in new_dealer.cards:
            print(card)
        print('-'*30)
        print(f'Hand Value: {new_dealer.total_value()}\n')
        
        if new_player.total_value() > new_dealer.total_value():
            print('Player wins!')
            print('Doubling his bet...')
            bank_account = new_player.bank_account
            bank_account.deposit(bet * 2)
            
        elif new_player.total_value() < new_dealer.total_value():
            print('Dealer wins!')
            print('Player will lose the bet amt....')
            bank_account = new_player.bank_account
            print(f'Balance : {bank_account.balance}')
            
        else:
            print('Its a tie!')
            print('Player gets his bet money back!')
            bank_account = new_player.bank_account
            bank_account.deposit(bet)
            
        game_on = False

def main():
    player_name = input('Enter your name: ')
    try:
        bank_balance = int(input('Enter your starting balance: '))
    except:
        bank_balance = 50
        print('Invalid input! Hence you will be starting with the default balance in your account - 50$')
    else:
        print(f'Creating an account....\nWith balance {bank_balance}....')
        
    #Creating a bank account for the player
    bank_account = Bank(player_name, bank_balance)

    while True:
        choice = input('Start? Enter (Yes/y) to start or any other key to exit: ')
        if choice.lower() not in ['yes', 'y']:
            print('Checking for any debts....')
            print('Deleting your bank_account....\n')
            print('Deleting your game profile...\n')
            print('Exit successfull!')
            return;
            
        os.system('cls')

        #Creating a player and dealer object
        new_player = Player(player_name, bank_account)
        new_dealer = Dealer()
        
        #Creating the deck and shuffling it
        new_deck = Deck()
        new_deck.shuffle()
        
        #Dealing 2 cards for the start of the game
        new_player.add_cards(new_deck.deal_cards(2))
        new_dealer.add_cards(new_deck.deal_cards(2))

        game_start(new_player, new_dealer, new_deck, bank_account)

        if bank_account.balance > 0:
            choice = input('Play again? (Yes / y)')
            if choice.lower() not in ['yes', 'y']:
                return;
        else:
            print('If you continue anymore you will be in debt.\nExiting the game...')
            return;

if __name__ == '__main__':
    main()
