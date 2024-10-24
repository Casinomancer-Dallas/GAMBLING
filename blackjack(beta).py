from random import shuffle

class Card:
    def __init__(self, rank, suit): 
        self.rank = rank
        self.suit = suit 
        # Add a value to use in the blackjack scoring
        self.value = rank if isinstance(rank, int) else (1 if rank == "A" else 10) 
    
    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck(list):  # Inherit from list as a deck is mostly a list
    def __init__(self):
        suits = "Hearts", "Diamonds", "Clubs", "Spades"
        ranks = 2,3,4,5,6,7,8,9,10,"J","Q","K","A"
        for suit in suits:
            for rank in ranks:
                card = Card(rank, suit)
                self.append(card)

    def deal(self, player):  # Pass player as argument so to act on deck & player
        player.append(self.pop())
        return player[-1]

    def collect(self, player):
        self.extend(player)
        player.clear()
    
    def __str__(self):
        return ", ".join(map(str, self))


class Player(Deck):  # Inherit from Deck, as a player really is a deck with a name
    def __init__(self, name, isdealer):
        self.name = name
        self.isdealer = isdealer

    def score(self):
        total = 0
        hasAce = False
        for card in self:
            total += card.value
            hasAce = hasAce or card.value == 1
        return total + 10 if hasAce and total < 12 else total
    
    def __str__(self):
        return f"{self.name} has {self.score()} ({super().__str__()})"




def main():
    balance = 1000
    # Welcome the player and explain the rules
    print("""Welcome to Blackjack! Here are the Rules
      Try to get as close to 21 without going over.
      Kings, Queens, and Jacks are worth 10 points.
      Aces are worth 1 or 11 points.
      Cards 2 through 10 are worth their face value.
      (H)it to take another card.
      (S)tand to stop taking cards.
      The dealer stops hitting at 17
      """)
    def betcheck(betamount):
        if betamount.isdigit() == True:
            betamount == int(betamount)
            rightbet = True
        else:
            rightbet = False
            print("Please enter a whole number, no decimals and a bet on or below the balance.")
        return rightbet
    
    while True:
        Validbet = False
        while Validbet == False:
            betamount = input("Please enter amount you wish to bet: ")
            Validbet = betcheck(betamount) 

        betamount = int(betamount)

        if betamount > 0:
            deck = Deck()

            # Make player 1 and the dealer
            player = Player(input("What's your name? "), False)
            dealer = Player("Dealer", True)

            while True:
                # return cards to the deck
                deck.collect(player)
                deck.collect(dealer)
        
                shuffle(deck)
        
                # Deal 2 cards to the players
                deck.deal(player)
                deck.deal(player)
                deck.deal(dealer)
                deck.deal(dealer)

                # Loop: display hands and scores
                print()
                print("New game:")
                print(dealer)
                print(player)
        
                # Ask them to hit or stand.
                while player.score() <= 21:
                    choice = input(f"{player.name}, do you want to [h]it, [s]tand or [q]uit? ").upper()
                    if choice == "Q":
                        return
                    if choice == "S":
                        break
                    if choice == "H":
                        print(f"{player.name}, you receive {deck.deal(player)}")
                        print(player)
    
                while dealer.score() <= 16:
                    print(f"{dealer.name} receives {deck.deal(dealer)}")
                    print(dealer)
            
                # Determine Winner
                if player.score() > 21 or player.score() <= dealer.score() <= 21:
                    print(f"{dealer.name} won this round")
                else:
                    print(f"{player.name}, you won this round!")
                    balance = betamount + balance
                    print(f"You now have {balance} Chips.")
                locask = input("would you like to play again? ")
                if locask.lower().startswith("y") and balance < 1:
                    chipdeskask = input("you are out of chips, would you like to go to the chip desk? ")
                    if chipdeskask.lower().startswith("y"):
                        quit()
                    if chipdeskask.lower().startswith("n"):
                        quit()
                if locask.lower().startswith("y") and balance > 1:
                    break 
                if locask.lower().startswith("n"):
                    quit()
                else:
                    print("This is an incorrect input, please answer yes or no.")                


if __name__ == '__main__':
    main()