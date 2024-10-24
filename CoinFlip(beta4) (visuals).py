import random
from time import sleep
import os
balance = 1000
betlimit = balance
location = 'CoinFlipL'
flip_Symbols = ["──", "＼", "|", "／", "──"]
flip_Pick = 2
flip_Count = [8, 16, 20, 24]
flip_CountPick = random.randint(0,4)
flip_Num = flip_Count[flip_CountPick]
def clearConsole():
	command = 'clear'
	if os.name in ('nt','dos'):
		command = 'cls'
	os.system(command)
def coin_Up():
    print("\n \n", flip_Symbols[0])
    sleep(.090)
    clearConsole()
    print("\n", flip_Symbols[1])
    sleep(.090)
    clearConsole()
    print(flip_Symbols[2])
    clearConsole()
    sleep(.090)
def coin_Down():
    print(flip_Symbols[2])
    sleep(.090)
    clearConsole()
    print("\n", flip_Symbols[1])
    sleep(.090)
    clearConsole()
    print("\n \n", flip_Symbols[0])
    sleep(.090)
def coin_face():
    return coin_face
def coin_flip():
    balance = 1000
    def coin():
        return coin
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
            Call_Input = input("Please call heads or tails:")

            if Call_Input.lower().startswith("h"):
                coin_face = 0
               
            
            if Call_Input.lower().startswith("t"):
                coin_face = 1
            
            flip_Symbols = ["──", "＼", "|", "／", "──"]
            flip_Pick = 2
            flip_Count = [8, 16, 20, 24]
            flip_CountPick = random.randint(0,4)
            flip_Num = flip_Count[flip_CountPick]
            coin_Up()
            for i in range(flip_Num):
                print(flip_Symbols[flip_Pick])
                flip_Pick = flip_Pick + 1
                sleep(.075)
                clearConsole()
                if flip_Pick >= 4:
                    flip_Pick = 0
            coin_Down()
            coin = random.randint(0, 1)
            if coin == 0:
                print("Heads")
                print("   ___\n /     \ \n│ \(¯)/ │\n \ ___ /")
            else:
                print("Tails")
                print("   ___\n /  ∆  \ \n│ φ Ω φ │\n \ _ψ_ /")
            if coin == coin_face:
                cfwinnings = betamount 
                print(f"Congragulations!, you won! your winnings are {cfwinnings}")
                balance = balance + cfwinnings 
                print(f"You now have {balance} chips.")
            else: 
                balance = balance - betamount
                print(f"Aw Man, you lost, your balance is now {balance}")

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
print("Hi there user, welcome to the coin flip simulator.")
print(f"Your opening account has in it {balance}")
print("To win, just call what the coin lands on.")
print("Enter yes or no when prompted to finish or continue the program.")

while location == 'CoinFlipL':
    coin_flip()