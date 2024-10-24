import random 
from random import shuffle
import os
import tkinter as tk
from pygame import mixer
balance = 1000

diceSetnum = [4, 6, 8, 10, 12, 20]
diceListnum = set(diceSetnum)
diceSet = ("dice game", "dice", "the dice game", "the dice")
coinSet = ("coin flip", "coinflip", "cf", "the coin flip" "the coinflip")
slotSet = ("the slot machines", "slot machines", "the slot machine", "slot machines", "slots")
BlackJSet = ("the blackjack table", "blackjack table", "blackjack")
OverUnderSet = ("over-under table", "the over-under table", "over under table", "the over under table", "over under", "over-under", "overunder")
c_list = {'higher': 1 , 'lower': 0}
ChipDeskSet = ("chip", "chips", "the chip desk", "chip desk")
diceList = set(diceSet)
slotsList = set(slotSet)
BlackJList = set(BlackJSet)
OverUnderList = set(OverUnderSet)
CoinList = set(coinSet)
ChipDeskList = set(ChipDeskSet)

def OUaskinputcheck(choice):
    if choice.lower() == "higher" or choice.lower() == "lower":
        OUrightanswerinput = True
    else:
        OUrightanswerinput = False
        print("This is an incorrect input, please type an appropriate answer in.")
    return OUrightanswerinput
def OUgame():
    score = 0
    cur_num = random.randint(1,10)
    old_num = cur_num
    print("Your starting number is " + str(cur_num))
    
    while True:
        while cur_num == old_num:
            cur_num = random.randint(1,100)
        choice = input("Is the next number 'higher' or 'lower': ")
         
        if (cur_num > old_num) == c_list[choice]:
            print("Good job! The new number is " + str(cur_num))
            score += 1
            old_num = cur_num
        else:
            print("you lose! New number is " + str(cur_num))
            break
    
    return score
def coin():
    return coin
def coin_face():
    return coin_face
def placeholderL():
    print("replace this with the actual location")
def betcheck(betamount):
    if betamount.isdigit() == True:
        betamount == int(betamount)
        rightbet = True
    else:
        rightbet = False
        print("Please enter a whole number, no decimals and a bet on or below the balance.")
    return rightbet
def betlimit(betamount):
    if betamount > balance:
        goodlimit = balance
        print("That bet is too high! - bet adjusted to ", goodlimit)
    else:
        goodlimit = betamount
    return goodlimit
def askinputcheckL(answerinputL):
    if answerinputL.lower() in slotsList or BlackJList or OverUnderList or ChipDeskList:
        rightanswerinputL = True
    else:
        rightanswerinputL = False
        print("This is an incorrect input, please type an appropriate answer in.")
    return rightanswerinputL
def Chip_DeskL():
    global balance
    chipRequest = input("Hello! How many chips would you like? ")
    if chipRequest.isdigit() == True:
        chipRequest = int(chipRequest) 
        if chipRequest > 1000:
            print("I can't give you more than 1000 chips at a time. ")
        if chipRequest < 1001:
            print(f"Here are your {chipRequest} chips, Good luck! ")
            balance = balance + chipRequest
            Casino_DoorsL()

    
    else:
        print("Okay, have a nice day!")
        Casino_DoorsL()
        print("Please enter a whole number.")
def Casino_DoorsL():
    Casino_Location = 'Casino_Doors'
    print("Hello! Welcome to the Serpentine Casino! Please see the Chip Desk to recieve chips or to cash out!")
    if Casino_Location == "Casino_Doors":
        
        musicvalidask = False
        while musicvalidask == False:
            music_ask = input("Would you like to listen to music?: ")
            musicvalidask = askinputcheck(music_ask)
            musicvalidask = str(music_ask)
        if music_ask.lower().startswith("y"):
            music_askT = True


        if music_ask.lower().startswith("n"):
            music_askT = False


        if music_askT == True:
            class MusicPlayer:
                def __init__(self, master):
                    self.master = master
                    self.master.title("Music Player")
                
                    # Initialize pygame mixer
                    mixer.init()
                
                    # Create buttons for each song
                    self.song_folder = "EXAMPLE(G:\My Drive\Casino\Ready To Distribute\Casino\Casino_Gambling)"  # Change this to the path of your music folder
                    self.refresh_button = tk.Button(master, text="Refresh Songs", command=self.refresh_songs)
                    self.refresh_button.pack()

                    # Initial song list
                    self.songs = []
                    self.refresh_songs()

                def refresh_songs(self):
                    # Clear existing buttons
                    for widget in self.master.winfo_children():
                        if widget != self.refresh_button:
                            widget.destroy()

                    # Load songs from the folder
                    self.songs = [f for f in os.listdir(self.song_folder) if f.endswith(('.mp3', '.wav'))]

                    if not self.songs:
                        label = tk.Label(self.master, text="No music files found.")
                        label.pack()
                    else:
                        # Create buttons for each song
                        for song in self.songs:
                            button = tk.Button(self.master, text=song[:-4], command=lambda s=song: self.play_song(s))
                            button.pack()

                def play_song(self, song):
                    # Load and play the selected song
                    mixer.music.load(os.path.join(self.song_folder, song))
                    mixer.music.play()

            if __name__ == "__main__":
                root = tk.Tk()
                app = MusicPlayer(root)
                root.mainloop()
        if music_askT == False:
            print("Understood")
        
        validaskL = False
        while validaskL == False:
            askinputL = input("Where would you like to go first? The Chip Desk, the Coin Flip, the Slot Machines, the Blackjack Table, the Dice Game, or the Over-Under Table? ")
            askinputLL = askinputcheckL(askinputL)
            askinputLL = str(askinputL)
            askinputLL = askinputLL.lower()
            
            if askinputLL in CoinList:
                Casino_Location = "CoinFlipL"
                if Casino_Location == "CoinFlipL":
                    return Casino_Location
            if askinputLL in ChipDeskList:
                Casino_Location = "ChipDeskL"
                if Casino_Location == "ChipDeskL":
                    return Casino_Location
            if askinputLL in slotsList:
                Casino_Location = 'SlotMachinesL'
                if Casino_Location == 'SlotMachinesL':
                    return Casino_Location  
            if askinputLL in BlackJList:
                Casino_Location = "BlackjackL"
                if Casino_Location == "BlackjackL":
                    return Casino_Location
            if askinputLL in OverUnderList:
                Casino_Location = "OverUnderL"
                if Casino_Location == "OverUnderL":
                    return Casino_Location
            if askinputLL in diceList:
                Casino_Location = "DiceGameL"
                if Casino_Location == "DiceGameL":
                    return Casino_Location
def betlimit(betamount):
    if betamount > balance:
        goodlimit = balance
        print("That bet is too high! - bet adjusted to ", goodlimit)
    else:
        goodlimit = betamount
    return goodlimit
def askinputcheck(answerinput):
    if answerinput.lower().startswith('y') or answerinput.lower().startswith("n"):
        rightanswerinput = True
    else:
        rightanswerinput = False
        print("This is an incorrect input, please type an appropriate answer in.")
    return rightanswerinput
def spinning(reels, betamount):
    reelone, reeltwo, reelthree = reels[0], reels[1], reels[2]
    global balance
    winnings = 0
    if reelone[0] == "Ω" and reeltwo[0] == "Ω" and reelthree[0] == "Ω":
        winnings = int(betamount) * 10 + int(balance)
        print("You won the jackpot! Congragulations! This is how much your account contains $", winnings)
    elif reelone[0] == "Φ" and reeltwo[0] == "Φ" and reelthree[0] == "Φ":
        winnings = int(betamount) *5 + int(balance)
        print("You won a considerable return! Awesome! Your balance and wins are $", winnings)
    elif reelone[0] == "Δ" and reeltwo[0] == "Δ" and reelthree[0] == "Δ":
        winnings = int(betamount) *2 + int(balance)
        print("You won a good return! Its a conspiracy! This is all of your money total $", winnings)
    elif reelone[0] == "Φ" and reeltwo[0] == "Φ" and reelthree[0] == "Φ":
        winnings = int(balance) - int(betamount)
        print("Unfortunately you didn't win anything, bad luck! You rewards are $", winnings)
    else:
        winnings = int(balance) - int(betamount)
        print("Bad luck! Maybe next time you'll win! Your remaining cash is $", winnings)
    balance = winnings
    return reels
def rebalance(startagain):
    global balance
    if balance < 1 and startagain == True:
        unbalance = True
        Casino_Location = "Chip_DeskL"
        print("You ran out of money, Head to the Chip Desk")

    else:
        unbalance = False
        print("You still have money.")
    return unbalance
Casino_Location = Casino_DoorsL()
if Casino_Location == "SlotMachinesL":
    while True:
        Validbet = False
        while Validbet == False:
            betamount = input("Please enter amount you wish to bet: ")
            Validbet = betcheck(betamount)

        betamount = int(betamount)

        betamount = betlimit(betamount)
        if betamount > 0:
            reelone = random.sample(["Ω", "Φ", "Φ", "Δ", "Δ", "Δ", "Φ", "Φ", "Φ", "Φ"],1)
            reeltwo = random.sample(["Ω", "Φ", "Φ", "Δ", "Δ", "Δ", "Φ", "Φ", "Φ", "Φ"],1)
            reelthree = random.sample(["Ω", "Φ", "Φ", "Δ", "Δ", "Δ", "Φ", "Φ", "Φ", "Φ"],1)

            reels = [reelone, reeltwo, reelthree]
            print( "\n",reels,"\n")
            slotspin = spinning(reels, betamount)



        validask = False
        while validask == False:
            answerinput = input("\nWould you like to play again?: ")
            validask = askinputcheck(answerinput)
            validask = str(answerinput)

        if answerinput.lower().startswith("y"):
            print(f"You have {balance} chips")

        if answerinput.lower().startswith("n"):
            print(f"You ended the game with {balance} chips")
            Casino_Location = "Casino_DoorsL"
            Casino_DoorsL()


        if answerinput.lower().startswith("y") and balance < 1:
            print("You're out of chips! You should go see the chip desk.")
            Chip_DeskL()
if Casino_Location == "BlackjackL":
    class Card:
        def __init__(self, rank, suit): 
            self.rank = rank
            self.suit = suit 
            
            self.value = rank if isinstance(rank, int) else (1 if rank == "A" else 10) 
        
        def __str__(self):
            return f"{self.rank} of {self.suit}"

    class Deck(list): 
        def __init__(self):
            suits = "Hearts", "Diamonds", "Clubs", "Spades"
            ranks = 2,3,4,5,6,7,8,9,10,"J","Q","K","A"
            for suit in suits:
                for rank in ranks:
                    card = Card(rank, suit)
                    self.append(card)

        def deal(self, player):  
            player.append(self.pop())
            return player[-1]

        def collect(self, player):
            self.extend(player)
            player.clear()
        
        def __str__(self):
            return ", ".join(map(str, self))


    class Player(Deck):  
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




    def my_mainBlackJ():
        global balance
        
        print("""Welcome to Blackjack! Here are the Rules
        Try to get as close to 21 without going over.
        Kings, Queens, and Jacks are worth 10 points.
        Aces are worth 1 or 11 points.
        Cards 2 through 10 are worth their face value.
        (H)it to take another card.
        (S)tand to stop taking cards.
        """)
        
        while True:
            Validbet = False
            while Validbet == False:
                betamount = input("Please enter amount you wish to bet: ")
                Validbet = betcheck(betamount) 

            betamount = int(betamount)

            if betamount > 0:
                deck = Deck()

                
                player = Player(input("What's your name? "), False)
                dealer = Player("Dealer", True)

                while True:
                    
                    deck.collect(player)
                    deck.collect(dealer)
            
                    shuffle(deck)
            
                    
                    deck.deal(player)
                    deck.deal(player)
                    deck.deal(dealer)
                    deck.deal(dealer)

                    
                    print()
                    print("New game:")
                    print(dealer)
                    print(player)
            
                    
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
                
                    
                    if player.score() > 21 or player.score() <= dealer.score() <= 21:
                        print(f"{dealer.name} won this round")
                    else:
                        print(f"{player.name}, you won this round!")
                        balance = betamount + balance
                        print(f"You now have {balance} Chips.")
                    validask = False
                    while validask == False:
                        answerinput = input("\nWould you like to play again?: ")
                        validask = askinputcheck(answerinput)
                        validask = str(answerinput)

                    if answerinput.lower().startswith("y"):
                        print(f"You have {balance} chips")

                    if answerinput.lower().startswith("n"):
                        print(f"You ended the game with {balance} chips")
                        Validbet = False
                        Casino_DoorsL()


                    if answerinput.lower().startswith("y") and balance < 1:
                        print("You're out of chips! You should go see the chip desk.")
                        Chip_DeskL()
    my_mainBlackJ()
if Casino_Location == "CoinFlipL":

    print("Hi there user, welcome to the coin flip Table.")
    print("To win, just call what the coin lands on.")
    print("Enter yes or no when prompted to finish or continue playing.")
    while True:
        Validbet = False
        while Validbet == False:
            betamount = input("Please enter amount you wish to bet: ")
            Validbet = betcheck(betamount) 

        betamount = int(betamount)

        if betamount > 0:
            Call_Input = input("Please call heads or tails:")

            if Call_Input.lower().startswith("h"):
                coin_face = 0
            
            
            if Call_Input.lower().startswith("t"):
                coin_face = 1

            coin = random.randint(0, 1)
            if coin == 0:
                print("Heads")
            else:
                print("Tails")
            if coin == coin_face:
                cfwinnings = betamount 
                print(f"Congragulations!, you won! your winnings are {cfwinnings}")
                balance = balance + cfwinnings 
                print(f"You now have {balance} chips.")
            else: 
                balance = balance - betamount
                print(f"Aw Man, you lost, your balance is now {balance} chips")

                locask = input("would you like to play again? ")
                if locask.lower().startswith("y") and balance < 1:
                    chipdeskask = input("you are out of chips, would you like to go to the chip desk? ")
                    if chipdeskask.lower().startswith("y"):
                        Chip_DeskL()
                    if chipdeskask.lower().startswith("n"):
                        Casino_DoorsL()
                if locask.lower().startswith("y") and balance > 1:
                    Casino_Location == "Coin_FlipL"
                if locask.lower().startswith("n"):
                    Casino_DoorsL()
                else:
                    print("This is an incorrect input, please answer yes or no.")
if Casino_Location == "DiceGameL":

    print("welcome to the dice game, the rules are simple.")
    print("call a number on the die that you pick, and if you win,")
    print("you win your bet multipied by the amount of sides on the die.")
    print("Your options for the amount of sides are 4, 6, 8, 10, 12, and 20")
    diceLoop = False
    while diceLoop == False:

        diceSideNum = False
        while diceSideNum == False:
                sides = int(input("how many sides do you want to use?"))
                if sides not in diceListnum:
                    print("Thats not an option for sides.")
                if sides in diceListnum:
                    diceSideNum = True
        while diceLoop == False:
            diceCall = int(input(f"and What number would you like to call on the {sides} sided die?"))
            if diceCall > sides:
                print(f"thats not a number on a die with {sides} sides")
            else:
                diceLoop = True
        while True:
            Validbet = False
            while Validbet == False:
                betamount = input("Please enter amount you wish to bet: ")
                Validbet = betcheck(betamount) 

            betamount = int(betamount)

            if betamount > 0:
                if diceLoop == True:
                    dealerDiceRoll = random.randint(1,sides)

                if dealerDiceRoll == diceCall:
                    print("Nice! You Won! Here are your winnings.")
                    balance = balance - betamount
                    balance = (betamount * sides) + balance
                    print(f"you have {balance} chips")
                if dealerDiceRoll != diceCall:
                    print("Touch luck, Kid.")
                    balance = balance - betamount
                    print(f"you now have {balance} chips.")
                validask = False
                while validask == False:
                    answerinput = input("\nWould you like to play again?: ")
                    validask = askinputcheck(answerinput)
                    validask = str(answerinput)

                if answerinput.lower().startswith("y"):
                    print(f"You have {balance} chips")


                if answerinput.lower().startswith("n"):
                    print(f"You ended the game with {balance} chips")
                    Casino_DoorsL()



                if answerinput.lower().startswith("y") and balance < 1:
                    print("You're out of chips! You should go see the chip desk.")
                    Chip_DeskL()
if Casino_Location == "OverUnderL":

    print("Welcome to the Higher/Lower game!\n")
    print("The rules of the game are simple.")
    print("You start off with a number, and you have to guess if the next number is 'higher' or 'lower'.")
    print("You will need to reply back with either 'higher' or lower'.")
    print("The numbers are between 1-100 inclusive. For each correct answer, you get a point.")
    print("The goal is to get as many points as possible without getting a wrong answer. Good luck!\n")

    high_score = 0

    while True:
        Validbet = False
        while Validbet == False:
            betamount = input("Please enter amount you wish to bet: ")
            Validbet = betcheck(betamount) 

        betamount = int(betamount)

        if betamount > 0:
            cur_score = OUgame()
            if cur_score > high_score:
                high_score = cur_score
            print("Your score is " + str(cur_score))
            inp = "o"
            while inp not in ['Y', 'y', 'N', 'n']:
                inp = input("Want to continue? (Y/N): ")
                balance = balance + (betamount * cur_score)
                print(f"you have {balance} chips")
            if inp in ['N', 'n']:
                break
            else:
                print("Start of new game.")

    print("End of game. Your highest score is " + str(high_score))
    print(f"Your balance is now {balance} Chips")
if Casino_Location == "ChipDeskL":
    Chip_DeskL()