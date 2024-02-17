# This is the guess number game.

import random

print("Enter your name.")
name = input()
print("Hello! " + name + " Please guess the number between 1 to 20")
secretNumber = random.randint(1, 20)

# Player to guess the number upto 6 time only 
for guessTaken in range(1, 7):
    print("Take a guess.")
    guess = int(input())

    if guess > secretNumber:
        print("No. is so high.")
    elif guess < secretNumber :
        print("No. is so low.")
    else :
        break # This is for correct guess

if guess == secretNumber:
    print("Good job, " + name + " You find the number in " + str(guessTaken) + " guesses")
else :
    print("Nope, The number are ", str(secretNumber))
    
