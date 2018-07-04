import random

posruns = [1,2,3,4,6,0]

def bowling():
    runs = 0
    while True:
        run = random.choice(posruns)
        while True:
            guess = raw_input("Cricket! You are bowling, guess the number of runs: ")
            if guess != "" and int(guess) in posruns:
                break
            else:
                print("Please guess a valid Cricket score in this list: (0,1,2,3,4,6)")
        if run == int(guess):
            print("Computer scored! " + str(run) + " runs, you guessed " + str(guess))
            print("Computer is out! You guessed correctly")
            print("They scored " + str(runs) + " runs")
            break
        else:
            print("Computer scored! " + str(run) + " runs, you guessed " + str(guess))
            runs += run
    return int(runs)

def batting():
    runs = 0
    while True: 
        guess = random.choice(posruns)
        while True:
            run = raw_input("You are batting, how many runs do you hit: ")
            if run != "" and  int(run) in posruns:
                break
            else:
                print("Please guess a valid Cricket score in this list: (0,1,2,3,4,6)")
        if int(run) == guess:
            print("You scored! " + str(run) + " runs, computer guessed " + str(guess))
            print("Player is out! Computer guessed your runs")
            print("You scored " + str(runs) + " runs batting")
            break
        else:
            print("You scored! " + str(run) + " runs, computer guessed " + str(guess))
            runs += int(run)
    return int(runs)

while True:
    reply = str(raw_input("Do you want to Bat? (y/n): "))
    if reply[:1] == 'y':
        print("Your batting.")
        yourRuns = batting()
        print("Your turn to bowl.")
        compRuns = bowling()
        break
    elif reply[:1] == 'n':
        print("Your turn to bowl.")
        compRuns = bowling()
        print("Your batting.")
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
