import random

reply = str(raw_input("Do you want to Bat? (y/n): "))

posruns = [1,2,3,4,6,0]

def bowling():
    runs = 0
    while True:
        run = random.choice(posruns)
        guess = int(raw_input("Cricket! You are bowling, guess the number of runs: "))
        while True:
            if guess in posruns:
                break
            else:
                print("Please guess a valid Cricket score in this list: (0,1,2,3,4,6)")
                guess = int(raw_input("Cricket! You are bowling, guess the number of runs: "))

        if run == guess:
            print("Computer scored! " + str(run) + " runs, you guessed " + str(guess))
            print("Computer is out! You guessed correctly")
            print("The score was " + str(runs) + " runs")
            break
        else:
            print("Computer scored! " + str(run) + " runs, you guessed " + str(guess))
            runs += run

def batting():
    runs = 0
    while True: 
        guess = random.choice(posruns)
        run = int(raw_input("You are batting, how many runs do you hit: "))
        while True:
            if run in posruns:
                break
            else:
                print("Please guess a valid Cricket score in this list: (0,1,2,3,4,6)")
                run = int(raw_input("You are batting, how many runs do you hit: "))
        if run == guess:
            print("You scored! " + str(run) + " runs, computer guessed " + str(guess))
            print("Player is out! Computer guessed your runs")
            print("The score was " + str(runs) + " runs")
            break
        else:
            print("You scored! " + str(run) + " runs, computer guessed " + str(guess))
            runs += run

if reply[:1] == 'y':
    print("You chose to Bat, enter your number of runs: ")
    batting()
if reply[:1] == 'n':
    print("You chose to Bowl.")
    bowling()
