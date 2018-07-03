import random

reply = str(raw_input("Do you want to Bat? (y/n): "))

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
            print("The score was " + str(runs) + " runs")
            break
        else:
            print("Computer scored! " + str(run) + " runs, you guessed " + str(guess))
            runs += run

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
            print("The score was " + str(runs) + " runs")
            break
        else:
            print("You scored! " + str(run) + " runs, computer guessed " + str(guess))
            runs += int(run)

if reply[:1] == 'y':
    print("You chose to Bat, enter your number of runs: ")
    batting()
if reply[:1] == 'n':
    print("You chose to Bowl.")
    bowling()
