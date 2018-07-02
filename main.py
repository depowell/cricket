import random

reply = str(raw_input("Do you want to Bat? (y/n): "))

posruns = [1,2,3,4,6,0]

def bowling():
    run = random.choice(posruns)
    guess = raw_input("Cricket! You are bowling, guess the number of runs: ")

    if run == guess:
        print("Player is out! You guessed correctly")
    else:
        print("Incorrect")

    print("The number of runs was: " + str(run))

def batting():
    guess = random.choice(posruns)
    run = int(raw_input("Cricket! You are batting, how many runs do you hit: "))

    if run == guess:
        print("Player is out! Computer guessed your runs")
    else:
        print("You scored! " + str(run) + " runs, computer guessed " + str(guess))

if reply[:1] == 'y':
    print("You chose to Bat, enter your number of runs: ")
    batting()
if reply[:1] == 'n':
    print("You chose to Bowl.")
    bowling()
