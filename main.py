import random

posruns = [1,2,3,4,6,0]

print("Welcome to Cricket! the object of the game is to guess what score your opponent is going to hit out of these possible scores: (1,2,3,4,6,0) goodluck.")
print("The player with the highest score at the end of their innings will be the winner, the game is about to start, you will have to choose if you want to bat first or bowl.")

def bowling():
    runs = 0
    while True:
        run = random.choice(posruns)
        while True:
            guess = raw_input("Cricket! You are bowling, guess the number of runs: ")
            try:
                x = int(guess)
                if x in posruns:
                    break
            except ValueError:
                print("Please guess a valid Cricket score in this list: (0,1,2,3,4,6)")
            else:
                print("Please guess a valid Cricket score in this list: (0,1,2,3,4,6)")
        if run == int(guess):
            print("Computer scored! " + str(run) + " runs, you guessed " + str(guess))
            print("Computer is out! You guessed correctly")
            print("They scored " + str(runs) + " runs")
            break
        else:
            runs += run
            print("Computer scored! " + str(run) + " runs, you guessed " + str(guess) + " (Computer score: " + str(runs) + ")")
    return int(runs)

def batting():
    runs = 0
    while True: 
        guess = random.choice(posruns)
        while True:
            run = raw_input("You are batting, how many runs do you hit: ")
            try:
                x = int(run)
                if x in posruns:
                    break
            except ValueError:
                print("Please guess a valid Cricket score in this list: (0,1,2,3,4,6)")
            else:
                print("Please guess a valid Cricket score in this list: (0,1,2,3,4,6)")
        if int(run) == guess:
            print("You scored! " + str(run) + " runs, computer guessed " + str(guess))
            print("Player is out! Computer guessed your runs")
            print("You scored " + str(runs) + " runs batting")
            break
        else:
            runs += int(run)
            print("You scored! " + str(run) + " runs, computer guessed " + str(guess) + " (Your score: " + str(runs) + ")")
    return int(runs)

while True:
    reply = str(raw_input("Do you want to Bat? (y/n): "))
    if reply[:1] == 'y':
        print("You are batting.")
        yourRuns = batting()
        print("Your turn to bowl.")
        compRuns = bowling()
        break
    elif reply[:1] == 'n':
        print("Your turn to bowl.")
        compRuns = bowling()
        print("You are batting.")
        yourRuns = batting()
        break
    else: 
        print("Please answer yes(y) or no(n)")

if yourRuns > compRuns:
    print("CONGRATULATIONS YOU WIN THE GAME!!! :D")
elif yourRuns < compRuns:
    print("Computer wins the game! Shit")
else:
    print("It was a draw... ")
