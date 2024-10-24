import random
from time import sleep
import os
balance = 1000

print("Hi there user, welcome to the amazing slot machine simulator.")
print(f"Your opening account has in it ${balance}")
print("To win a jackpot, three Ωs must be in a row.")
print("Enter yes or no when prompted to finish or continue the program.")



Symbols = ["Ω", "Φ", "Δ", "Φ"]

def clearConsole():
	command = 'clear'
	if os.name in ('nt','dos'):
		command = 'cls'
	os.system(command)

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
    elif reelone[0] == "ψ" and reeltwo[0] == "ψ" and reelthree[0] == "ψ":
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
        balance = 1000
        print("You ran out of money, here is $1000")
    else:
        unbalance = False
        print("You still have money.")
    return unbalance


def my_mainloop():
    global balance
    while True:
        Validbet = False
        while Validbet == False:
            betamount = input("Please enter amount you wish to bet: ")
            Validbet = betcheck(betamount)

        betamount = int(betamount)

        betamount = betlimit(betamount)

        if betamount > 0:
            reelone = ["◘"]
            reeltwo = ["◘"]
            reelthree = ["◘"]
            slotStop = .35
            for i in range (3):
                
                sleep(slotStop)
                clearConsole()
                reelone = random.sample(["Ω", "Φ", "Φ", "Δ", "Δ", "Δ", "ψ", "ψ", "ψ", "ψ"],1)
                reels = [reelone,reeltwo,reelthree]
                print(f"__⌐┌=═≡ψφ═∆═Ω═∆═φψ≡═=┐¬__\n\  │«LUCK OF ΩLYMPUS»│  /\n╘╦═╧═════╤══════╤════╧═╦╛\n ╠{reels}╣\n ╠═══════╧══════╧══════╣\n ║▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓║\n ║═══≡∆≡φ≡ω=ψ=ω≡φ≡∆≡═══║\n ║┌─────┐              ║\n ║║    Θ┤              ║\n ║└─────┘  _._         ║\n ║       /     \       ║\n ║      │       │      ║\n ║    \__\     /__/    ║\n ║                     ║\n ╚═════════════════════╝")
                sleep(slotStop)
                slotStop = slotStop + .1
                clearConsole()
                reeltwo = random.sample(["Ω", "Φ", "Φ", "Δ", "Δ", "Δ", "ψ", "ψ", "ψ", "ψ"],1)
                reels = [reelone,reeltwo,reelthree]
                print(f"__⌐┌=═≡ψφ═∆═Ω═∆═φψ≡═=┐¬__\n\  │«LUCK OF ΩLYMPUS»│  /\n╘╦═╧═════╤══════╤════╧═╦╛\n ╠{reels}╣\n ╠═══════╧══════╧══════╣\n ║▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓║\n ║═══≡∆≡φ≡ω=ψ=ω≡φ≡∆≡═══║\n ║┌─────┐              ║\n ║║    Θ┤              ║\n ║└─────┘  _._         ║\n ║       /     \       ║\n ║      │       │      ║\n ║    \__\     /__/    ║\n ║                     ║\n ╚═════════════════════╝")
                sleep(slotStop)
                slotStop = slotStop + .1
                clearConsole()
                reelthree = random.sample(["Ω", "Φ", "Φ", "Δ", "Δ", "Δ", "ψ", "ψ", "ψ", "ψ"],1)
                reels = [reelone,reeltwo,reelthree]
                print(f"__⌐┌=═≡ψφ═∆═Ω═∆═φψ≡═=┐¬__\n\  │«LUCK OF ΩLYMPUS»│  /\n╘╦═╧═════╤══════╤════╧═╦╛\n ╠{reels}╣\n ╠═══════╧══════╧══════╣\n ║▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓║\n ║═══≡∆≡φ≡ω=ψ=ω≡φ≡∆≡═══║\n ║┌─────┐              ║\n ║║    Θ┤              ║\n ║└─────┘  _._         ║\n ║       /     \       ║\n ║      │       │      ║\n ║    \__\     /__/    ║\n ║                     ║\n ╚═════════════════════╝")
                slotStop = slotStop + .1
            clearConsole()
            reels = [reelone,reeltwo,reelthree]
            print(f"__⌐┌=═≡ψφ═∆═Ω═∆═φψ≡═=┐¬__\n\  │«LUCK OF ΩLYMPUS»│  /\n╘╦═╧═════╤══════╤════╧═╦╛\n ╠{reels}╣\n ╠═══════╧══════╧══════╣\n ║▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓║\n ║═══≡∆≡φ≡ω=ψ=ω≡φ≡∆≡═══║\n ║┌─────┐              ║\n ║║    Θ┤              ║\n ║└─────┘  _._         ║\n ║       /     \       ║\n ║      │       │      ║\n ║    \__\     /__/    ║\n ║                     ║\n ╚═════════════════════╝")
            slotspin = spinning(reels, betamount)



        validask = False
        while validask == False:
            answerinput = input("\nWould you like to play again?: ")
            validask = askinputcheck(answerinput)

        if answerinput.lower().startswith("y"):
            startagain = True
            print("You have $", balance)
        elif answerinput.lower().startswith("n"):
            startagain = False
            print("You ended the game with", balance)
            break
        else:
            print("This is an incorrect input, please answer yes or no.")


        if answerinput.lower().startswith("y") and balance < 1:
            rebalance(startagain)

if __name__ == "__main__":
    my_mainloop()